# Summarize the most recent Simon Willison article with Gemini.

import os
from datetime import datetime, timedelta, timezone

import feedparser
from dotenv import load_dotenv
from google import genai

from fetch_feeds import DAYS_BACK, REQUEST_HEADERS, is_recent

SIMON_FEED_URL = "https://simonwillison.net/atom/everything/"


def get_article_text(entry):
    if "content" in entry:
        return entry.content[0].value
    return entry.summary


def main():
    cutoff = datetime.now(timezone.utc) - timedelta(days=DAYS_BACK)

    parsed = feedparser.parse(SIMON_FEED_URL, request_headers=REQUEST_HEADERS)
    entry = next((e for e in parsed.entries if is_recent(e, cutoff)), None)

    if entry is None:
        print("No recent entry found.")
        return

    article_text = get_article_text(entry)

    load_dotenv()  # reads GEMINI_API_KEY from .env
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

    prompt = (
        "Summarize the following article in 3-4 sentences in English. "
        "Explain the main idea clearly, simplify any jargon, "
        "but keep the key technical point.\n\n"
        f"Title: {entry.title}\n\n"
        f"Text: {article_text}"
    )

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt,
    )

    print(entry.title)
    print(entry.link)
    print(response.text)


if __name__ == "__main__":
    main()
