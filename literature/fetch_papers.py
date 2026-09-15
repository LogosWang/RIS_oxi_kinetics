"""Download public papers, preserve provenance, and extract page-labelled text."""
import concurrent.futures
import datetime
import hashlib
import json
import pathlib
import sys
import requests

ROOT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, '/private/tmp/ris_pdf_tools')
from pypdf import PdfReader

def fetch(item):
    name, url = item
    record = {'id': name, 'url': url, 'retrieved': datetime.datetime.now(datetime.timezone.utc).isoformat()}
    try:
        response = requests.get(url, timeout=50)
        record.update(status=response.status_code, final_url=response.url)
        if response.content.startswith(b'%PDF'):
            path = ROOT / 'pdfs' / (name + '.pdf')
            path.write_bytes(response.content)
            reader = PdfReader(path)
            content = '\n\n'.join(f'===== PDF PAGE {i+1} =====\n{page.extract_text()}' for i, page in enumerate(reader.pages)).replace('\x00', '')
            (ROOT / 'text' / (name + '.txt')).write_text(content)
            record.update(result='pdf', pages=len(reader.pages), bytes=len(response.content), sha256=hashlib.sha256(response.content).hexdigest())
        else:
            record.update(result='not_pdf', bytes=len(response.content))
            (ROOT / 'metadata' / (name + '.response.html')).write_text(response.text)
    except Exception as exc:
        record.update(result='error', error=str(exc))
    (ROOT / 'metadata' / (name + '.json')).write_text(json.dumps(record, indent=2))
    return record

if __name__ == '__main__':
    items = json.loads(pathlib.Path(sys.argv[1]).read_text())
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for record in executor.map(fetch, items):
            print(json.dumps(record), flush=True)
