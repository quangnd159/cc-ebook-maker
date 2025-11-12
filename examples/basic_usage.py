#!/usr/bin/env python3
"""
Example: Basic EPUB creation from pasted text
"""

import sys
sys.path.insert(0, '..')
from ebook_maker import EbookMaker

# Create ebook
maker = EbookMaker(
    title="My First Book",
    author="John Doe",
    language="en"
)

# Add a simple chapter with pasted text
text = """
This is the first paragraph of my book.

This is the second paragraph with more content.

And here's a third paragraph to make it interesting.
"""

maker.add_chapter("Chapter 1: Introduction", text)

# Add another chapter
maker.add_chapter("Chapter 2: The Journey", "Another chapter's content here...")

# Save the EPUB
output_path = maker.save("output/basic_book.epub")
print(f"Book created: {output_path}")
