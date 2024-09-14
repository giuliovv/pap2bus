import requests
import xmltodict
from datetime import datetime, timedelta

def fetch_recent_papers(category='cs.AI', max_results=5, past_days=1):
    yesterday = datetime.utcnow() - timedelta(days=past_days)
    date_from = yesterday.strftime('%Y%m%d0000')
    date_to = datetime.utcnow().strftime('%Y%m%d2359')

    query = f'search_query=cat:{category}+AND+submittedDate:[{date_from}+TO+{date_to}]&start=0&max_results={max_results}&sortBy=submittedDate&sortOrder=descending'

    url = f'http://export.arxiv.org/api/query?{query}'
    response = requests.get(url)

    data = xmltodict.parse(response.content)

    abstracts = []
    if 'feed' in data and 'entry' in data['feed']:
        entries = data['feed']['entry']
        if isinstance(entries, dict):
            entries = [entries]
        for entry in entries:
            title = entry.get('title', '').replace('\n', ' ').strip()
            summary = entry.get('summary', '').replace('\n', ' ').strip()
            abstracts.append({'title': title, 'summary': summary})
    return abstracts

if __name__ == "__main__":
    print(fetch_recent_papers())