import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_KEY'))

def generate_business_ideas(abstracts):
    ideas = []
    for paper in abstracts:
        title = paper['title']
        summary = paper['summary']

        prompt = (
            f"Paper Title: {title}\n\n"
            f"Abstract: {summary}\n\n"
            "Based on the abstract above, list 3 potential business ideas or applications that could arise from this research. "
            "Provide concise bullet points in format: |- TITLE: IDEA, but do not use any other markdown. Each bullet point should have less than 250 chars."
        )

        response = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[{'role': 'user', 'content': prompt}],
            max_tokens=200,
            temperature=0.7,
        )

        business_ideas = response.choices[0].message.content.strip()
        ideas.append({'title': title, 'summary':summary, 'business_ideas': business_ideas})
    return ideas
