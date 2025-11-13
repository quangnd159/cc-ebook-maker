#!/usr/bin/env python3
"""
Professional Ebook Maker - Create beautiful EPUB files
Using EbookLib with professional typography and CSS best practices
Designed to be used programmatically by Claude Code agents
"""

import re
from pathlib import Path
from ebooklib import epub
import requests
from bs4 import BeautifulSoup


class EbookMaker:
    """
    Professional EPUB creator with excellent typography and formatting.
    Uses EbookLib with CSS best practices for e-readers.
    """

    # Professional CSS stylesheet optimized for modern e-readers
    # Designed for KOReader's html5.css (HTML standard rendering) mode
    # Follows best practices: line-height on body only, no inline styles
    DEFAULT_CSS = '''
@namespace epub "http://www.idpf.org/2007/ops";

/* Base styles - line-height on body only (Kobo best practice) */
body {
    font-family: Georgia, serif;
    line-height: 1.7;
    margin: 5%;
    text-align: justify;
}

/* Headings inherit line-height from body */
h1, h2, h3, h4, h5, h6 {
    font-family: Georgia, serif;
    text-align: left;
    font-weight: normal;
    margin-top: 2em;
    margin-bottom: 1em;
}

h1 {
    font-size: 1.4em;
    border-bottom: 0.1em solid #333;
    padding-bottom: 0.3em;
}

h2 {
    font-size: 1.2em;
}

h3 {
    font-size: 1.1em;
}

/* Paragraphs */
p {
    margin: 0;
    text-indent: 0;
    margin-bottom: 0.5em;
}

/* Bilingual content */
.original-text {
    font-size: 1.05em;
    margin-bottom: 0.3em;
    color: #000;
}

.translation {
    font-size: 1em;
    font-style: italic;
    margin-bottom: 1.8em;
    color: #333;
}

/* Glossary styling */
.glossary-term {
    margin: 1.5em 0;
}

.term-original {
    font-weight: bold;
    font-size: 1.1em;
    color: #000;
}

.term-arrow {
    color: #666;
}

.term-translation {
    color: #666;
    font-weight: bold;
}

.term-explanation {
    margin-top: 0.3em;
    color: #666;
}
'''

    def __init__(self, title, author="Unknown", language="en", publisher="", description=""):
        """
        Initialize a new EPUB book.

        Args:
            title: Book title
            author: Author name (can be added multiple times)
            language: Book language code (e.g., 'en', 'vi', 'zh')
            publisher: Publisher name
            description: Book description
        """
        self.book = epub.EpubBook()

        # Set metadata
        self.book.set_identifier(f'{title.lower().replace(" ", "-")}-001')
        self.book.set_title(title)
        self.book.set_language(language)
        self.book.add_author(author)

        if publisher:
            self.book.add_metadata('DC', 'publisher', publisher)
        if description:
            self.book.add_metadata('DC', 'description', description)

        # Create and add CSS stylesheet
        self.css = epub.EpubItem(
            uid="style_main",
            file_name="style/style.css",
            media_type="text/css",
            content=self.DEFAULT_CSS
        )
        self.book.add_item(self.css)

        # Track chapters for spine
        self.chapters = []
        self.chapter_counter = 1

    def set_custom_css(self, css):
        """
        Override the default CSS with custom styles.

        Args:
            css: Custom CSS string
        """
        self.css.content = css

    def add_chapter(self, title, content, content_is_html=False, lang=None):
        """
        Add a chapter to the book.

        Args:
            title: Chapter title
            content: Chapter content (plain text or HTML)
            content_is_html: If True, content is treated as complete HTML
            lang: Language code for this chapter (optional)

        Returns:
            The created EpubHtml chapter object
        """
        # Create filename
        filename = f'chapter_{self.chapter_counter}.xhtml'
        self.chapter_counter += 1

        # Create chapter
        chapter = epub.EpubHtml(
            title=title,
            file_name=filename,
            lang=lang or self.book.language
        )

        # Build HTML content
        if content_is_html:
            html_content = content
        else:
            # Convert plain text to HTML
            html_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head>
    <title>{title}</title>
    <link rel="stylesheet" href="style/style.css" type="text/css"/>
</head>
<body>
    <h2>{title}</h2>
'''
            # Convert paragraphs
            paragraphs = content.split('\n\n')
            for para in paragraphs:
                if para.strip():
                    html_content += f'    <p>{para.strip()}</p>\n'

            html_content += '</body>\n</html>'

        # Set content
        chapter.set_content(html_content.encode('utf-8'))

        # Link CSS to chapter
        chapter.add_item(self.css)

        # Add to book
        self.book.add_item(chapter)
        self.chapters.append(chapter)

        return chapter

    def add_bilingual_chapter(self, title, text_pairs, original_lang='zh', translation_lang='vi'):
        """
        Add a chapter with bilingual content (original + translation).

        Args:
            title: Chapter title
            text_pairs: List of tuples [(original_text, translation_text), ...]
            original_lang: Language code for original text
            translation_lang: Language code for translation

        Returns:
            The created EpubHtml chapter object
        """
        filename = f'chapter_{self.chapter_counter}.xhtml'
        self.chapter_counter += 1

        chapter = epub.EpubHtml(
            title=title,
            file_name=filename,
            lang=original_lang
        )

        # Build HTML
        html_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head>
    <title>{title}</title>
    <link rel="stylesheet" href="style/style.css" type="text/css"/>
</head>
<body>
    <h2>{title}</h2>

'''

        # Add text pairs
        for original, translation in text_pairs:
            html_content += f'    <p class="original-text">{original}</p>\n'
            html_content += f'    <p class="translation">{translation}</p>\n\n'

        html_content += '</body>\n</html>'

        chapter.set_content(html_content.encode('utf-8'))
        chapter.add_item(self.css)
        self.book.add_item(chapter)
        self.chapters.append(chapter)

        return chapter

    def add_glossary(self, terms, title="Glossary"):
        """
        Add a glossary chapter.

        Args:
            terms: List of dicts with keys: 'term', 'translation', 'explanation'
            title: Glossary chapter title

        Returns:
            The created glossary chapter
        """
        filename = f'glossary.xhtml'

        glossary = epub.EpubHtml(
            title=title,
            file_name=filename,
            lang=self.book.language
        )

        html_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops">
<head>
    <title>{title}</title>
    <link rel="stylesheet" href="style/style.css" type="text/css"/>
</head>
<body>
    <h1>{title}</h1>

'''

        for term_data in terms:
            html_content += f'''    <div class="glossary-term">
        <p class="term-original">{term_data['term']}</p>
        <p><span class="term-arrow">→</span> <span class="term-translation">{term_data['translation']}</span></p>
        <p class="term-explanation">{term_data['explanation']}</p>
    </div>

'''

        html_content += '</body>\n</html>'

        glossary.set_content(html_content.encode('utf-8'))
        glossary.add_item(self.css)
        self.book.add_item(glossary)
        self.chapters.insert(0, glossary)  # Put glossary first

        return glossary

    def load_from_file(self, file_path):
        """Read text content from a file"""
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()

    def fetch_from_url(self, url, extract_method='paragraphs'):
        """
        Fetch content from a URL.

        Args:
            url: URL to fetch
            extract_method: 'paragraphs', 'article', or 'raw'

        Returns:
            Extracted text content
        """
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        if extract_method == 'paragraphs':
            paragraphs = soup.find_all('p')
            return '\n\n'.join([p.get_text().strip() for p in paragraphs if p.get_text().strip()])
        elif extract_method == 'article':
            article = soup.find('article') or soup.find('main') or soup.find('body')
            return article.get_text(separator='\n\n', strip=True) if article else soup.get_text()
        else:  # raw
            return soup.get_text(separator='\n\n', strip=True)

    def save(self, output_path):
        """
        Save the EPUB file.

        Args:
            output_path: Path where to save the EPUB file

        Returns:
            Absolute path to the saved file
        """
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Build table of contents
        self.book.toc = tuple(
            epub.Link(chapter.file_name, chapter.title, chapter.id)
            for chapter in self.chapters
        )

        # Add navigation files
        self.book.add_item(epub.EpubNcx())
        self.book.add_item(epub.EpubNav())

        # Define spine (reading order)
        self.book.spine = ['nav'] + self.chapters

        # Write the EPUB
        epub.write_epub(str(output_path), self.book, {})

        return str(output_path.absolute())


# Utility functions

def format_text_with_headings(text, heading_pattern=r'^#+\s+(.+)$'):
    """
    Parse text with markdown-style headings and convert to chapters.
    Returns a list of chapter dicts.
    """
    lines = text.split('\n')
    chapters = []
    current_chapter = None

    for line in lines:
        match = re.match(heading_pattern, line, re.MULTILINE)
        if match:
            if current_chapter:
                chapters.append(current_chapter)
            current_chapter = {
                'title': match.group(1).strip(),
                'content': ''
            }
        elif current_chapter is not None:
            current_chapter['content'] += line + '\n'

    if current_chapter:
        chapters.append(current_chapter)

    return chapters


if __name__ == '__main__':
    print("Professional Ebook Maker")
    print("This module is designed to be used programmatically.")
    print("See examples/ directory for usage examples.")
