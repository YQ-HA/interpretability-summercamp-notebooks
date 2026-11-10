"""Execute one repaired classroom notebook in a fresh kernel."""
import argparse
import hashlib
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--session', type=int, choices=range(1, 9), required=True)
    args = parser.parse_args()
    import nbformat
    from nbclient import NotebookClient
    from nbclient.exceptions import CellExecutionError
    sessions = json.loads((ROOT/'docs/notebook-manifest.json').read_text(encoding='utf-8'))['sessions']
    session = sessions[args.session - 1]
    path = ROOT/session['notebook']
    output = ROOT/'results'/f'session-{args.session:02d}'
    output.mkdir(parents=True, exist_ok=True)
    notebook = nbformat.read(path, as_version=4)
    record = {'session': args.session, 'source': session['notebook'],
              'source_sha256': hashlib.sha256(path.read_bytes()).hexdigest()}
    (output/'input.json').write_text(json.dumps(record, indent=2), encoding='utf-8')
    client = NotebookClient(notebook, timeout=-1, kernel_name='python3', allow_errors=False,
                            resources={'metadata': {'path': str(path.parent)}})
    print(f"Executing session {args.session:02d}: {path.name}", flush=True)
    try:
        client.execute()
    except CellExecutionError:
        nbformat.write(notebook, output/('FAILED-' + path.name))
        raise
    nbformat.write(notebook, output/path.name)
    print('Saved executed notebook:', output/path.name)

if __name__ == '__main__':
    main()
