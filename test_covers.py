#!/usr/bin/env python3
"""
Test script to demonstrate AI-driven cover generation
Shows different color schemes for different book genres
"""

from ebook_maker import EbookMaker

# Test cases - different genres/themes
test_books = [
    {
        "title": "The Courage to be Disliked",
        "author": "Ichiro Kishimi",
        "expected_scheme": "philosophical (navy)"
    },
    {
        "title": "Love in the Time of Code",
        "author": "Sarah Chen",
        "expected_scheme": "romantic (rose)"
    },
    {
        "title": "Python Algorithms Mastery",
        "author": "John Smith",
        "expected_scheme": "technical (steel blue)"
    },
    {
        "title": "The Mystery of the Dark Tower",
        "author": "Edgar Blackwood",
        "expected_scheme": "mystery (purple)"
    },
    {
        "title": "Journey to the Wild",
        "author": "Maria Adventure",
        "expected_scheme": "adventure (brown)"
    }
]

print("Testing AI-driven cover generation...")
print("=" * 60)

for i, book_info in enumerate(test_books, 1):
    print(f"\n{i}. Creating: {book_info['title']}")
    print(f"   Author: {book_info['author']}")
    print(f"   Expected scheme: {book_info['expected_scheme']}")
    
    # Create book
    book = EbookMaker(
        title=book_info['title'],
        author=book_info['author'],
        language='en'
    )
    
    # Add a sample chapter
    book.add_chapter(
        "Chapter 1",
        "This is a sample chapter content for testing purposes."
    )
    
    # Save with auto-generated cover
    output_file = f"output/test_cover_{i}.epub"
    book.save(output_file, auto_generate_cover=True)
    
    # Also generate standalone cover for preview
    cover_img = book.generate_cover()
    if cover_img:
        preview_file = f"output/test_cover_{i}_preview.jpg"
        cover_img.save(preview_file, quality=95)
        print(f"   ✓ EPUB: {output_file}")
        print(f"   ✓ Preview: {preview_file}")

print("\n" + "=" * 60)
print("All test covers generated!")
print("Check the output/ directory for results.")
