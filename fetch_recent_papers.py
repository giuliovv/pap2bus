import requests
import xmltodict
from datetime import datetime, timedelta

def fetch_recent_papers(category='cs.AI', max_results=5, past_days=1):
    # Calculate the date range for the last day
    yesterday = datetime.utcnow() - timedelta(days=past_days)
    date_from = yesterday.strftime('%Y%m%d0000')
    date_to = datetime.utcnow().strftime('%Y%m%d2359')

    # Construct the arXiv API query
    query = f'search_query=cat:{category}+AND+submittedDate:[{date_from}+TO+{date_to}]&start=0&max_results={max_results}&sortBy=submittedDate&sortOrder=descending'

    # Send the request
    url = f'http://export.arxiv.org/api/query?{query}'
    response = requests.get(url)

    # Parse the XML response
    data = xmltodict.parse(response.content)

    # Extract abstracts
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