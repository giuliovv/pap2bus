import os

from dotenv import load_dotenv

import openai

load_dotenv()
openai.api_key = os.getenv('OPENAI_KEY')

def generate_business_ideas(abstracts):
    ideas = []
    for paper in abstracts:
        title = paper['title']
        summary = paper['summary']

        prompt = (
            f"Paper Title: {title}\n\n"
            f"Abstract: {summary}\n\n"
            "Based on the abstract above, list potential business ideas or applications that could arise from this research. "
            "Provide concise bullet points."
        )

        response = openai.ChatCompletion.create(
            model='gpt-4',
            messages=[{'role': 'user', 'content': prompt}],
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.7,
        )

        business_ideas = response.choices[0].message.content.strip()
        ideas.append({'title': title, 'business_ideas': business_ideas})
    return ideas
