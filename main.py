from fetch_recent_papers import fetch_recent_papers
from generate_ideas import generate_business_ideas
from twitter import post_to_twitter

def main():
    abstracts = fetch_recent_papers(past_days=3)
    ideas = generate_business_ideas(abstracts)
    post_to_twitter(ideas)


if __name__ == "__main__":
    main()