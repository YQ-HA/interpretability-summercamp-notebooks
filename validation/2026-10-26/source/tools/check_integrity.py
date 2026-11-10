"""Inspect the repaired source and preserved notes without scientific imports."""
import argparse
import ast
import builtins
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import symtable
ROOT = Path(__file__).resolve().parents[1]

def notes(notebook):
    return Counter(line.strip() for cell in notebook['cells'] for line in ''.join(cell['source']).splitlines()
                   if line.lstrip().startswith('#'))

def globals_used(table):
    names = {s.get_name() for s in table.get_symbols() if s.is_global() and s.is_referenced()}
    for child in table.get_children(): names |= globals_used(child)
    return names

def check(require_data=False):
    errors=[]; counts={'notebooks':0,'code_cells':0,'archived_files':0,'data_files':0,'preserved_comment_lines':0,'preserved_double_hash_lines':0}
    def require(ok,message):
        if not ok: errors.append(message)
    manifest=json.loads((ROOT/'docs/notebook-manifest.json').read_text(encoding='utf-8'))
    for entry in manifest['archives']:
        p=ROOT/entry['file']
        require(hashlib.sha256(p.read_bytes()).hexdigest()==entry['sha256'],f'Archive changed: {p.name}')
        counts['archived_files']+=1
    for session in manifest['sessions']:
        path=ROOT/session['notebook']; n=json.loads(path.read_text(encoding='utf-8'))
        raw=json.loads((ROOT/session['original']).read_text(encoding='utf-8'))
        old=notes(raw); new=notes(n)
        require(not old-new,f'{path.name}: missing classroom comments {list((old-new).elements())[:3]}')
        counts['preserved_comment_lines']+=sum(old.values())
        counts['preserved_double_hash_lines']+=sum(v for k,v in old.items() if k.startswith('##'))
        indices=[c['metadata']['classroom_original_cell'] for c in n['cells'] if 'classroom_original_cell' in c['metadata']]
        require(sorted(indices)==list(range(len(raw['cells']))),f'{path.name}: original cell mapping incomplete')
        require(len({c['id'] for c in n['cells']})==len(n['cells']),f'{path.name}: duplicate IDs')
        available=set(dir(builtins))|{'__name__','__file__'}; combined=[]
        for c in n['cells']:
            if c['cell_type']!='code': continue
            source=''.join(c['source']);label=f"{path.name}:{c['id']}"
            try:
                compile(source,label,'exec');table=symtable.symtable(source,label,'exec')
                bound={s.get_name() for s in table.get_symbols() if s.is_assigned() or s.is_imported()}
                reads={s.get_name() for s in table.get_symbols() if s.is_referenced()}
                missing=reads-available-bound
                require(not missing,f'{label}: used before definition {sorted(missing)}')
                available |= bound; combined.append(source)
            except SyntaxError as exc: errors.append(f'{label}: {exc}')
            require(not c['outputs'] and c['execution_count'] is None,f'{label}: inherited outputs')
            counts['code_cells']+=1
        table=symtable.symtable('\n\n'.join(combined),path.name,'exec')
        bound={s.get_name() for s in table.get_symbols() if s.is_assigned() or s.is_imported()}
        require(not globals_used(table)-bound-set(dir(builtins)),f'{path.name}: unresolved function globals {sorted(globals_used(table)-bound-set(dir(builtins)))}')
        counts['notebooks']+=1
    missing=[]
    for entry in json.loads((ROOT/'data/manifest.json').read_text(encoding='utf-8')):
        p=ROOT/'data'/entry['file']
        if not p.exists(): missing.append(entry['file']);continue
        require(hashlib.sha256(p.read_bytes()).hexdigest()==entry['sha256'],f'Data changed: {p.name}')
        counts['data_files']+=1
    require(not require_data or not missing,'Required data files missing')
    for p in [ROOT/'README.md',*(ROOT/'docs').glob('*.md')]:
        for target in re.findall(r'\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
            if '://' not in target and not target.startswith('#'):require((p.parent/target.strip('<>').split('#')[0]).exists(),f'Broken link: {p.name}: {target}')
    for p in [*(ROOT/'tools').glob('*.py'),*(ROOT/'tests').glob('*.py')]:compile(p.read_text(encoding='utf-8'),str(p),'exec')
    for p in (ROOT/'validation').glob('*.ipynb'):
        for c in json.loads(p.read_text(encoding='utf-8'))['cells']:
            if c['cell_type']=='code':compile(''.join(c['source']),str(p),'exec')
    return {'status':'passed' if not errors else 'failed','scope':'static only; repaired notebooks await fresh Colab execution','counts':counts,'missing_data':missing,'errors':errors}

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--require-data',action='store_true');parser.add_argument('--report',type=Path)
    args=parser.parse_args();report=check(args.require_data)
    if args.report:args.report.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(report,indent=2));return 0 if report['status']=='passed' else 1
if __name__=='__main__':raise SystemExit(main())
