#!/usr/bin/env python3
"""
Example: Create a bilingual EPUB using the add_bilingual_chapter method
"""

import sys
sys.path.insert(0, '..')
from ebook_maker import EbookMaker

# Create ebook
maker = EbookMaker(
    title="Sample Bilingual Book",
    author="Author Name",
    language="vi",
    description="English-Vietnamese bilingual edition"
)

# Add glossary (optional)
glossary_terms = [
    {
        'term': 'Philosophy (Triết học)',
        'translation': 'Triết học',
        'explanation': 'The study of fundamental questions about existence, knowledge, and ethics.'
    },
    {
        'term': 'Courage (Dũng khí)',
        'translation': 'Dũng khí',
        'explanation': 'Mental strength to face difficulty or danger.'
    }
]
maker.add_glossary(glossary_terms, title="Bảng Thuật Ngữ / Glossary")

# Add bilingual chapter with text pairs
text_pairs = [
    ("Once upon a time, there was a philosopher.", "Ngày xưa, có một vị triết gia."),
    ("He believed the world was simple.", "Ông tin rằng thế giới rất đơn giản."),
    ("A young person came to challenge him.", "Một người trẻ đến để thách thức ông."),
]

maker.add_bilingual_chapter(
    title="Chapter 1",
    text_pairs=text_pairs,
    original_lang='en',
    translation_lang='vi'
)

# Save
output_path = maker.save("../output/bilingual_example.epub")
print(f"✓ Bilingual EPUB created: {output_path}")
