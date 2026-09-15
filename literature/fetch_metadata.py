"""Retrieve Crossref records and BibTeX for the papers used in the introduction."""
import concurrent.futures
import json
import pathlib
import requests

ROOT = pathlib.Path(__file__).resolve().parent
PAPERS = {
    'deng2017': '10.1016/j.corsci.2017.08.010',
    'deng2021apt': '10.1038/s41598-020-80600-x',
    'kuang2022': '10.1016/j.corsci.2022.110187',
    'wang2022': '10.1016/j.actamat.2022.118408',
    'wang2023': '10.1016/j.actamat.2023.119340',
    'du2026': '10.1016/j.corsci.2025.113424',
    'kadambi2025': '10.1016/j.commatsci.2025.113895',
    'lach2025': '10.1016/j.corsci.2025.113106',
}

def get(item):
    key, doi = item
    cached = ROOT / 'metadata' / (key + '_crossref.json')
    manual = ROOT / 'metadata' / (key + '_verified.json')
    if cached.exists():
        data = json.loads(cached.read_text())
    elif manual.exists():
        data = json.loads(manual.read_text())
    else:
        r = requests.get('https://api.crossref.org/works/' + doi, timeout=35)
        r.raise_for_status()
        data = r.json()['message']
        cached.write_text(json.dumps(data, indent=2, ensure_ascii=False))
    authors = ' and '.join(a.get('family', '') + ', ' + a.get('given', '') for a in data['author'])
    year = data.get('published-print', data['published'])['date-parts'][0][0]
    fields = {'author': authors, 'title': '{' + data['title'][0] + '}', 'journal': data['container-title'][0], 'year': str(year), 'volume': data.get('volume', ''), 'pages': data.get('page', data.get('article-number', '')), 'doi': doi}
    bib = '@article{' + key + ',\n' + '\n'.join('  ' + k + ' = {' + v.replace('–', '--') + '},' for k, v in fields.items() if v) + '\n}\n'
    return key, bib

if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        records = list(pool.map(get, PAPERS.items()))
    (ROOT / 'introduction.bib').write_text('\n'.join(bib for _, bib in records))
    for key, _ in records:
        print(key, 'metadata and BibTeX saved')
