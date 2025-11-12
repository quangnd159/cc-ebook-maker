#!/usr/bin/env python3
"""
Example: Fetch content from the web and create EPUB
"""

import sys
sys.path.insert(0, '..')
from ebook_maker import EbookMaker

# Create ebook
maker = EbookMaker(
    title="Web Content Collection",
    author="Various Authors",
    language="en"
)

# Fetch content from a URL
try:
    content = maker.fetch_from_url(
        "https://example.com/article",
        extract_method='paragraphs'
    )
    maker.add_chapter("Article from the Web", content)
except Exception as e:
    print(f"Error fetching content: {e}")

# Save the EPUB
output_path = maker.save("output/web_content.epub")
print(f"Book created: {output_path}")
