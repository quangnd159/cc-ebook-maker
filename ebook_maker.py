#!/usr/bin/env python3
"""
Professional Ebook Maker - Create beautiful EPUB files
Using EbookLib with professional typography and CSS best practices
Designed to be used programmatically by Claude Code agents
"""

import re
import random
import io
from pathlib import Path
from ebooklib import epub
import requests
from bs4 import BeautifulSoup

try:
    from PIL import Image, ImageDraw, ImageFont
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False


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

    def generate_cover(self, width=1600, height=2400, custom_subtitle=None):
        """
        Generate a beautiful book cover with AI-designed aesthetics.
        AI decides: background style, layout, decorative elements, everything!
        Only title and author are fixed - all design decisions are AI-driven.

        Args:
            width: Cover width in pixels (default 1600)
            height: Cover height in pixels (default 2400)
            custom_subtitle: Optional subtitle/tagline to add to cover

        Returns:
            PIL Image object (or None if PIL not available)
        """
        if not PIL_AVAILABLE:
            print("Warning: PIL/Pillow not installed. Cannot generate cover.")
            return None

        # Get book metadata
        title = self.book.title
        authors = self.book.get_metadata('DC', 'creator')
        author_text = ' & '.join([a[0] for a in authors]) if authors else ""

        # NO SEED - AI makes completely fresh creative decisions each time!
        print(f"  AI designing cover for: {title[:40]}...")

        # ==========================================
        # AI DECISION 1: Choose overall aesthetic
        # ==========================================
        aesthetics = ['minimalist', 'bold', 'elegant', 'modern', 'classic', 'artistic']
        chosen_aesthetic = random.choice(aesthetics)
        print(f"  AI chose aesthetic: {chosen_aesthetic}")

        # ==========================================
        # AI DECISION 2: Pick color palette
        # ==========================================
        # Generate base color from title
        color_palettes = [
            # Dark & moody
            [(15, 20, 30), (25, 35, 50), (40, 50, 70)],
            [(30, 15, 20), (50, 25, 35), (70, 40, 50)],
            [(20, 15, 30), (35, 25, 50), (50, 40, 70)],
            # Vibrant
            [(100, 20, 40), (140, 30, 60), (180, 50, 80)],
            [(20, 80, 60), (30, 110, 85), (50, 140, 110)],
            [(60, 40, 100), (85, 60, 130), (110, 85, 160)],
            # Earthy & warm
            [(80, 50, 30), (110, 70, 45), (140, 95, 65)],
            [(50, 60, 40), (70, 85, 60), (95, 110, 85)],
            # Cool & professional
            [(30, 40, 50), (45, 60, 75), (65, 85, 105)],
            [(35, 35, 45), (50, 50, 65), (70, 70, 90)],
        ]

        colors = random.choice(color_palettes)
        accent_color = (random.randint(180, 255), random.randint(180, 255), random.randint(100, 200))
        print(f"  AI chose color palette: RGB{colors[0]}")

        # ==========================================
        # AI DECISION 3: Background style
        # ==========================================
        bg_styles = ['solid', 'gradient_vertical', 'gradient_diagonal', 'gradient_radial', 'two_tone']
        bg_style = random.choice(bg_styles)
        print(f"  AI chose background: {bg_style}")

        img = Image.new('RGB', (width, height), colors[0])
        draw = ImageDraw.Draw(img)

        if bg_style == 'solid':
            # Solid color - already set
            pass

        elif bg_style == 'gradient_vertical':
            for y in range(height):
                ratio = y / height
                if ratio < 0.5:
                    blend = ratio * 2
                    r = int(colors[0][0] * (1 - blend) + colors[1][0] * blend)
                    g = int(colors[0][1] * (1 - blend) + colors[1][1] * blend)
                    b = int(colors[0][2] * (1 - blend) + colors[1][2] * blend)
                else:
                    blend = (ratio - 0.5) * 2
                    r = int(colors[1][0] * (1 - blend) + colors[2][0] * blend)
                    g = int(colors[1][1] * (1 - blend) + colors[2][1] * blend)
                    b = int(colors[1][2] * (1 - blend) + colors[2][2] * blend)
                draw.line([(0, y), (width, y)], fill=(r, g, b))

        elif bg_style == 'gradient_diagonal':
            for y in range(height):
                for x in range(width):
                    ratio = (x + y) / (width + height)
                    if ratio < 0.5:
                        blend = ratio * 2
                        r = int(colors[0][0] * (1 - blend) + colors[1][0] * blend)
                        g = int(colors[0][1] * (1 - blend) + colors[1][1] * blend)
                        b = int(colors[0][2] * (1 - blend) + colors[1][2] * blend)
                    else:
                        blend = (ratio - 0.5) * 2
                        r = int(colors[1][0] * (1 - blend) + colors[2][0] * blend)
                        g = int(colors[1][1] * (1 - blend) + colors[2][1] * blend)
                        b = int(colors[1][2] * (1 - blend) + colors[2][2] * blend)
                    if x % 5 == 0:  # Optimize - only draw every 5th pixel
                        draw.rectangle([(x, y), (x+5, y)], fill=(r, g, b))

        elif bg_style == 'gradient_radial':
            center_x, center_y = width // 2, height // 2
            max_dist = ((center_x ** 2) + (center_y ** 2)) ** 0.5
            for y in range(height):
                for x in range(width):
                    dist = ((x - center_x) ** 2 + (y - center_y) ** 2) ** 0.5
                    ratio = dist / max_dist
                    blend = min(1.0, ratio)
                    r = int(colors[0][0] * (1 - blend) + colors[2][0] * blend)
                    g = int(colors[0][1] * (1 - blend) + colors[2][1] * blend)
                    b = int(colors[0][2] * (1 - blend) + colors[2][2] * blend)
                    if x % 10 == 0:  # Optimize
                        draw.rectangle([(x, y), (x+10, y)], fill=(r, g, b))

        elif bg_style == 'two_tone':
            split_point = random.randint(int(height * 0.3), int(height * 0.7))
            draw.rectangle([(0, 0), (width, split_point)], fill=colors[0])
            draw.rectangle([(0, split_point), (width, height)], fill=colors[1])

        # ==========================================
        # AI DECISION 4: Decorative elements
        # ==========================================
        decoration_styles = ['none', 'top_border', 'frame', 'corner_accents', 'geometric_shapes']
        decoration = random.choice(decoration_styles)
        print(f"  AI chose decoration: {decoration}")

        if decoration == 'top_border':
            border_height = random.randint(5, 15)
            draw.rectangle([(0, 0), (width, border_height)], fill=accent_color)
            draw.rectangle([(0, height-border_height), (width, height)], fill=accent_color)

        elif decoration == 'frame':
            frame_width = random.randint(15, 40)
            draw.rectangle([(0, 0), (width, frame_width)], fill=accent_color)
            draw.rectangle([(0, height-frame_width), (width, height)], fill=accent_color)
            draw.rectangle([(0, 0), (frame_width, height)], fill=accent_color)
            draw.rectangle([(width-frame_width, 0), (width, height)], fill=accent_color)

        elif decoration == 'corner_accents':
            size = random.randint(80, 150)
            # Top corners
            draw.rectangle([(0, 0), (size, 3)], fill=accent_color)
            draw.rectangle([(0, 0), (3, size)], fill=accent_color)
            draw.rectangle([(width-size, 0), (width, 3)], fill=accent_color)
            draw.rectangle([(width-3, 0), (width, size)], fill=accent_color)
            # Bottom corners
            draw.rectangle([(0, height-3), (size, height)], fill=accent_color)
            draw.rectangle([(0, height-size), (3, height)], fill=accent_color)
            draw.rectangle([(width-size, height-3), (width, height)], fill=accent_color)
            draw.rectangle([(width-3, height-size), (width, height)], fill=accent_color)

        elif decoration == 'geometric_shapes':
            # Random geometric accent
            num_shapes = random.randint(2, 5)
            for _ in range(num_shapes):
                shape_x = random.randint(100, width-100)
                shape_y = random.randint(100, height-100)
                shape_size = random.randint(50, 200)
                opacity = random.randint(10, 40)
                shape_color = tuple(min(255, c + opacity) for c in colors[2])
                draw.ellipse([(shape_x, shape_y), (shape_x+shape_size, shape_y+shape_size)],
                           fill=shape_color)

        # ==========================================
        # AI DECISION 5: Typography & Layout
        # ==========================================
        title_size = random.randint(90, 150)
        author_size = random.randint(50, 85)

        # AI chooses layout position
        layout_styles = ['centered', 'top_heavy', 'bottom_heavy', 'split']
        layout = random.choice(layout_styles)
        print(f"  AI chose layout: {layout}")

        # Load fonts
        try:
            title_font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Georgia.ttf', title_size)
            author_font = ImageFont.truetype('/System/Library/Fonts/Supplemental/Georgia.ttf', author_size)

            # CJK support
            subtitle_font = None
            cjk_font_paths = ['/System/Library/Fonts/PingFang.ttc', '/System/Library/Fonts/Hiragino Sans GB.ttc']
            for font_path in cjk_font_paths:
                try:
                    subtitle_font = ImageFont.truetype(font_path, 60)
                    break
                except:
                    continue
            if subtitle_font is None:
                subtitle_font = title_font
        except:
            title_font = ImageFont.load_default()
            author_font = ImageFont.load_default()
            subtitle_font = ImageFont.load_default()

        # Text wrapping helper
        margin = int(width * 0.1)
        max_width = width - (2 * margin)

        def wrap_text(text, font, max_width):
            words = text.split()
            lines = []
            current_line = []
            for word in words:
                current_line.append(word)
                test_line = ' '.join(current_line)
                bbox = draw.textbbox((0, 0), test_line, font=font)
                if bbox[2] - bbox[0] > max_width:
                    if len(current_line) == 1:
                        lines.append(test_line)
                        current_line = []
                    else:
                        current_line.pop()
                        lines.append(' '.join(current_line))
                        current_line = [word]
            if current_line:
                lines.append(' '.join(current_line))
            return lines

        # AI decides text positioning based on layout
        if layout == 'centered':
            title_y = int(height * 0.35)
            author_y = int(height * 0.7)
        elif layout == 'top_heavy':
            title_y = int(height * 0.2)
            author_y = int(height * 0.8)
        elif layout == 'bottom_heavy':
            title_y = int(height * 0.55)
            author_y = int(height * 0.85)
        elif layout == 'split':
            title_y = int(height * 0.15)
            author_y = int(height * 0.65)

        # AI decides whether to use shadows
        use_shadow = random.choice([True, False])
        shadow_offset = random.randint(3, 6) if use_shadow else 0

        # Draw title
        title_lines = wrap_text(title, title_font, max_width)
        current_y = title_y
        text_color = (255, 255, 255) if colors[0][0] < 100 else (255, 255, 255)

        for line in title_lines:
            bbox = draw.textbbox((0, 0), line, font=title_font)
            line_width = bbox[2] - bbox[0]
            x = (width - line_width) // 2

            if use_shadow:
                draw.text((x + shadow_offset, current_y + shadow_offset), line,
                         font=title_font, fill=(0, 0, 0, 100))
            draw.text((x, current_y), line, font=title_font, fill=text_color)
            current_y += (bbox[3] - bbox[1]) + 15

        # AI decides on separator (or none)
        use_separator = random.choice([True, False])
        if use_separator and author_text:
            sep_y = current_y + 30
            sep_width = random.randint(int(width * 0.2), int(width * 0.5))
            sep_x1 = (width - sep_width) // 2
            draw.rectangle([(sep_x1, sep_y), (sep_x1 + sep_width, sep_y + 3)], fill=accent_color)

        # Draw author (if exists)
        if author_text:
            author_lines = wrap_text(author_text, author_font, max_width)
            for line in author_lines:
                bbox = draw.textbbox((0, 0), line, font=author_font)
                line_width = bbox[2] - bbox[0]
                x = (width - line_width) // 2

                if use_shadow:
                    draw.text((x + shadow_offset, author_y + shadow_offset), line,
                             font=author_font, fill=(0, 0, 0, 100))
                draw.text((x, author_y), line, font=author_font, fill=(230, 230, 230))
                author_y += (bbox[3] - bbox[1]) + 10

        # Optional subtitle (if provided)
        if custom_subtitle:
            subtitle_lines = wrap_text(custom_subtitle, subtitle_font, max_width)
            subtitle_y = int(height * 0.55)

            for line in subtitle_lines:
                bbox = draw.textbbox((0, 0), line, font=subtitle_font)
                line_width = bbox[2] - bbox[0]
                x = (width - line_width) // 2

                # Subtle accent color for subtitle
                subtitle_color = tuple(int(c * 0.8) for c in accent_color)
                draw.text((x, subtitle_y), line, font=subtitle_font, fill=subtitle_color)
                subtitle_y += (bbox[3] - bbox[1]) + 20

        return img

    def add_cover(self, cover_image_path=None, auto_generate=True, custom_subtitle=None):
        """
        Add a cover to the EPUB.

        Args:
            cover_image_path: Path to existing cover image (optional)
            auto_generate: If True and no image provided, generate a cover (default True)
            custom_subtitle: Optional subtitle for auto-generated covers

        Returns:
            True if cover was added, False otherwise
        """
        if cover_image_path:
            # Use provided cover image
            with open(cover_image_path, 'rb') as f:
                cover_bytes = f.read()
            self.book.set_cover('cover.jpg', cover_bytes)
            return True

        elif auto_generate and PIL_AVAILABLE:
            # Auto-generate beautiful cover
            cover_img = self.generate_cover(custom_subtitle=custom_subtitle)
            if cover_img:
                # Convert to bytes
                img_byte_arr = io.BytesIO()
                cover_img.save(img_byte_arr, format='JPEG', quality=95)
                cover_bytes = img_byte_arr.getvalue()
                self.book.set_cover('cover.jpg', cover_bytes)
                return True

        return False

    def save(self, output_path, auto_generate_cover=True, custom_subtitle=None):
        """
        Save the EPUB file.

        Args:
            output_path: Path where to save the EPUB file
            auto_generate_cover: Auto-generate a beautiful cover (default True)
            custom_subtitle: Optional subtitle for the cover

        Returns:
            Absolute path to the saved file
        """
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Auto-generate cover if requested and not already added
        if auto_generate_cover:
            # Check if cover already exists
            has_cover = False
            for item in self.book.get_items():
                if item.get_name() == 'cover.jpg':
                    has_cover = True
                    break

            if not has_cover:
                self.add_cover(auto_generate=True, custom_subtitle=custom_subtitle)

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
