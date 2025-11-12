#!/usr/bin/env python3
"""
Example: Automatically split text into chapters based on patterns
Useful when Claude Code receives a large text and user specifies how to split it
"""

import sys
sys.path.insert(0, '..')
from ebook_maker import EbookMaker, format_text_with_headings

# Create ebook
maker = EbookMaker(
    title="My Multi-Chapter Book",
    author="Jane Smith",
    language="en"
)

# Example 1: Split by triple newlines
long_text = """
First chapter content here.
More content.


Second chapter content starts here.
Even more content.


Third chapter begins.
Final content.
"""

maker.add_chapters_from_text(
    long_text,
    chapter_titles=["Introduction", "Development", "Conclusion"],
    split_pattern=r'\n\n\n+'
)

# Save
output_path = maker.save("output/auto_split.epub")
print(f"Book with auto-split chapters created: {output_path}")

# Example 2: Parse markdown-style headings
markdown_text = """
# Introduction

This is the introduction chapter.

Some more intro text.

# Chapter 1: The Beginning

This is where our story begins.

# Chapter 2: The Middle

The plot thickens here.
"""

maker2 = EbookMaker(title="Markdown Book", author="Author")
chapters = format_text_with_headings(markdown_text)
maker2.add_chapters_from_list(chapters)
maker2.save("output/markdown_book.epub")
print("Markdown-based book created: output/markdown_book.epub")
