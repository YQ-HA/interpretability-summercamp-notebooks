"""Audit the preserved October 26 classroom executions without running models."""
import argparse
import hashlib
import json
from pathlib import Path
import zipfile
ROOT=Path(__file__).resolve().parents[1]

def code_cells(notebook):
    return [c for c in notebook['cells'] if c['cell_type']=='code']

def source(cell):
    return ''.join(cell['source'])

def without_completion_labels(cell):
    return ''.join(line for line in source(cell).splitlines(keepends=True)
                   if not line.lstrip().startswith('# Course completion:'))

def audit():
    errors=[]
    def require(condition,message):
        if not condition:errors.append(message)
    evidence=ROOT/'validation/2026-10-26'
    manifest=json.loads((evidence/'manifest.json').read_text(encoding='utf-8'))
    for item in manifest['snapshot_files']+manifest['result_files']+manifest['raw_result_archives']:
        require(hashlib.sha256((ROOT/item['file']).read_bytes()).hexdigest()==item['sha256'],f"Evidence changed: {item['file']}")
    for item in manifest['raw_result_archives']:
        with zipfile.ZipFile(ROOT/item['file']) as archive:require(archive.testzip() is None,f"ZIP CRC failed: {item['file']}")
    sessions=json.loads((ROOT/'docs/notebook-manifest.json').read_text(encoding='utf-8'))['sessions']
    rows=[];total=0;executed=0;blank=0
    for session in sessions:
        number=session['session'];phase='cpu' if number<8 else 'gpu'
        frozen_path=evidence/'source'/session['notebook']
        frozen=json.loads(frozen_path.read_text(encoding='utf-8'))
        current=json.loads((ROOT/session['notebook']).read_text(encoding='utf-8'))
        saved_path=ROOT/'results'/f'session-{number:02d}'/Path(session['notebook']).name
        saved=json.loads(saved_path.read_text(encoding='utf-8'))
        a=code_cells(frozen);b=code_cells(current);c=code_cells(saved)
        require(len(a)==len(b)==len(c),f'Session {number}: code cell count changed')
        require(all(without_completion_labels(frozen_cell) == source(current_cell)
                    for frozen_cell, current_cell in zip(a, b)),
                f'Session {number}: current code differs beyond completion labels')
        require(len(frozen['cells'])==len(saved['cells']) and all(''.join(x['source'])==''.join(y['source']) for x,y in zip(frozen['cells'],saved['cells'])),f'Session {number}: saved execution differs from frozen source')
        nonempty=[cell for cell in c if ''.join(cell['source']).strip()]
        require(all(cell.get('execution_count') is not None for cell in nonempty),f'Session {number}: unexecuted nonempty cell')
        require(not any(o.get('output_type')=='error' for cell in c for o in cell.get('outputs',[])),f'Session {number}: error output')
        record=json.loads((ROOT/'results/validation'/phase/f'session-{number:02d}.json').read_text(encoding='utf-8'))
        require(record['status']=='passed' and record['returncode']==0,f'Session {number}: failed command')
        source_record=json.loads((saved_path.parent/'input.json').read_text(encoding='utf-8'))
        require(source_record['source_sha256']==hashlib.sha256(frozen_path.read_bytes()).hexdigest(),f'Session {number}: source hash mismatch')
        total+=len(c);executed+=len(nonempty);blank+=len(c)-len(nonempty)
        rows.append({'session':number,'notebook':Path(session['notebook']).name,'status':record['status'],'elapsed_seconds':record['elapsed_seconds'],'executed_nonempty_cells':len(nonempty),'blank_cells':len(c)-len(nonempty),'computational_source_and_notes_match':True,'executed_notebook':saved_path.relative_to(ROOT).as_posix()})
    for phase in ['cpu','gpu']:
        runtime=json.loads((ROOT/'results/validation'/phase/'runtime.json').read_text(encoding='utf-8'))
        for path,digest in runtime['sources_sha256'].items():
            require(hashlib.sha256((evidence/'source'/path).read_bytes()).hexdigest()==digest,f'{phase} runtime source snapshot mismatch: {path}')
    test_record=json.loads((ROOT/'results/validation/cpu/unit-tests.json').read_text(encoding='utf-8'))
    test_log=(ROOT/'results/validation/cpu/unit-tests.log').read_text(encoding='utf-8')
    require(test_record['returncode']==0 and 'Ran 6 tests' in test_log and '\nOK' in test_log,'Numerical tests did not pass')
    require((ROOT/'tests/test_methods.py').read_text(encoding='utf-8')==(evidence/'source/tests/test_methods.py').read_text(encoding='utf-8'),'Numerical test definitions changed')
    trace=json.loads((ROOT/'results/session-08/trace_status.json').read_text(encoding='utf-8'))
    return {'status':'passed' if not errors else 'failed','validation_date':'2026-10-26','scope':'Audit of maintainer-executed Colab artifacts; no model rerun','counts':{'sessions':len(rows),'code_cells':total,'executed_nonempty_cells':executed,'blank_cells':blank,'numerical_tests':6,'figures':len(list((ROOT/'results').glob('session-*/*.png'))),'csv_tables':len(list((ROOT/'results').glob('session-*/*.csv'))),'preserved_source_files':len(manifest['snapshot_files']),'preserved_result_files':len(manifest['result_files'])},'sessions':rows,'trace_status':trace,'limits':['Session 08 analysis completed on a truncated reasoning trace.','Working notebooks received navigation updates and had completion labels removed from restored code. Executable code and classroom notes match the validated snapshot.','The outer executed validation companion was not supplied; all eight executed lesson notebooks and runtime/test logs were supplied.'],'errors':errors}

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--report',type=Path)
    args=parser.parse_args();report=audit()
    if args.report:args.report.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(report,indent=2));return 0 if report['status']=='passed' else 1
if __name__=='__main__':raise SystemExit(main())
