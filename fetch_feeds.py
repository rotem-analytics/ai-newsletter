"""Fetch recent articles from a list of RSS feeds and print their titles and links."""

from datetime import datetime, timedelta, timezone

import feedparser

FEEDS = [
    "https://blog.google/technology/ai/rss/",
    "https://news.mit.edu/rss/topic/artificial-intelligence2",
    "https://towardsdatascience.com/feed",
    "https://simonwillison.net/atom/everything/",
]

DAYS_BACK = 7

# Some feeds (e.g. KDnuggets) reject requests without a browser-like User-Agent.
REQUEST_HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; ai-newsletter-bot/1.0)"}


def is_recent(entry, cutoff):
    published = entry.get("published_parsed") or entry.get("updated_parsed")
    if published is None:
        return False
    published_dt = datetime(*published[:6], tzinfo=timezone.utc)
    return published_dt >= cutoff


def main():
    cutoff = datetime.now(timezone.utc) - timedelta(days=DAYS_BACK)

    for feed_url in FEEDS:
        parsed = feedparser.parse(feed_url, request_headers=REQUEST_HEADERS)
        print(f"\n=== {parsed.feed.get('title', feed_url)} ===")

        for entry in parsed.entries:
            if is_recent(entry, cutoff):
                print(f"- {entry.title}")
                print(f"  {entry.link}")


if __name__ == "__main__":
    main()
