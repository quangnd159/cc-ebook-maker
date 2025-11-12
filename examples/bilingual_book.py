#!/usr/bin/env python3
"""
Example: Create a bilingual EPUB with parallel text
This demonstrates how Claude Code can fetch content in multiple languages
and combine them into a single book
"""

import sys
sys.path.insert(0, '..')
from ebook_maker import EbookMaker

# Create bilingual ebook
maker = EbookMaker(
    title="The Great Gatsby - Chapter 1 (Bilingual Edition)",
    author="F. Scott Fitzgerald",
    language="en",
    description="English-Spanish bilingual edition"
)

# English version (would be fetched from web by Claude Code)
english_text = """
In my younger and more vulnerable years my father gave me some advice
that I've been turning over in my mind ever since.

"Whenever you feel like criticizing any one," he told me, "just remember
that all the people in this world haven't had the advantages that you've had."
"""

# Spanish version (would be fetched or translated by Claude Code)
spanish_text = """
En mis años más jóvenes y vulnerables, mi padre me dio un consejo
que he estado reflexionando desde entonces.

"Siempre que sientas ganas de criticar a alguien", me dijo, "recuerda
que no todas las personas en este mundo han tenido las ventajas que tú has tenido."
"""

# Create bilingual HTML content
bilingual_content = f"""
<h1>Chapter 1 / Capítulo 1</h1>

<div style="border: 1px solid #ccc; padding: 10px; margin: 10px 0;">
<h2>English</h2>
{english_text.replace(chr(10) + chr(10), '</p><p>').replace(chr(10), '<br/>')}
</div>

<div style="border: 1px solid #ccc; padding: 10px; margin: 10px 0;">
<h2>Español</h2>
{spanish_text.replace(chr(10) + chr(10), '</p><p>').replace(chr(10), '<br/>')}
</div>
"""

maker.add_chapter("Chapter 1 / Capítulo 1", bilingual_content, content_is_html=True)

# Save the EPUB
output_path = maker.save("output/bilingual_gatsby.epub")
print(f"Bilingual book created: {output_path}")
