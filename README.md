# Professional Ebook Maker

An intelligent EPUB generator powered by Claude Code with **professional typography and formatting**. Create beautiful, readable ebooks from any text source using natural language instructions.

## Professional Features

Built with **EbookLib** and following EPUB best practices:

✓ **Georgia serif font** - Industry-standard for e-book readability
✓ **Optimal line-height (1.7)** - Comfortable reading experience
✓ **5% margins** - Perfect for all e-readers (Kindle, Kobo, Apple Books)
✓ **Clean CSS** - No complex layouts that break on different devices
✓ **Full EPUB3 compliance** - Works everywhere
✓ **Beautiful bilingual support** - Original text + italicized translations
✓ **Professional glossaries** - Styled term explanations
✓ **Optimized for html5.css** - Modern HTML standard rendering

### KOReader Users (Kobo, Kindle, etc.)

For best results with KOReader:
- Go to **Style** settings
- Select **"HTML standard rendering (html5.css)"**
- This is the modern standard that our CSS is optimized for
- Legacy "epub.css" mode may not display styles correctly

## How It Works

This tool is designed to work with Claude Code agents. Instead of using command-line arguments, you interact with Claude Code in natural language:

1. **Provide content** - Paste text, provide a file path, or ask Claude Code to fetch from the web
2. **Describe formatting** - Tell Claude Code how you want the book structured
3. **Get your EPUB** - Claude Code generates a custom Python script and creates a beautiful ebook

## Installation

```bash
pip install -r requirements.txt
```

## Example Workflows

### Simple Book from Pasted Text
> "Create an EPUB called 'My Story' by John Doe with this text: [paste text]. Split it into 3 chapters."

### Bilingual Book from File
> "Create a bilingual Chinese-Vietnamese EPUB from this file. Put Vietnamese translations in italics below each paragraph."

### Book from Web with Glossary
> "Fetch this article from the web and create an EPUB. Include a glossary of difficult terms at the beginning."

### Multi-Chapter Book
> "Create a book from these 5 text files, each one as a separate chapter with a table of contents."

## Key Features

### Professional Typography
- **Georgia serif** - Most readable font for long-form text
- **Responsive sizing** - Uses em/% units for device compatibility
- **Optimal spacing** - Line-height and margins tuned for comfort

### Bilingual Support
- Original text in regular font
- Translations in italics for clear distinction
- Proper spacing between paragraph pairs
- Built-in `add_bilingual_chapter()` method

### Glossary Support
- Professional styling with subtle backgrounds
- Term highlighting and explanations
- Automatically placed at the beginning

### Flexible Content Sources
- Plain text or HTML
- Local files
- Web URLs with smart extraction
- Mixed sources in one book

## API Examples

See the `examples/` directory for usage:
- `bilingual_example.py` - Create bilingual editions
- `basic_usage.py` - Simple EPUB from text
- `web_fetch.py` - Fetch content from URLs
- `auto_split_chapters.py` - Auto-split text into chapters

## For Developers

The `EbookMaker` class provides:

```python
from ebook_maker import EbookMaker

# Create book
maker = EbookMaker(title="My Book", author="Author", language="en")

# Add chapters
maker.add_chapter("Chapter 1", "Content here...")

# Add bilingual content
maker.add_bilingual_chapter("Title", [
    ("Original text", "Translation"),
    ("More original", "More translation")
])

# Add glossary
maker.add_glossary([
    {'term': 'Word', 'translation': 'Từ', 'explanation': 'Meaning...'}
])

# Save
maker.save("output.epub")
```

## CSS Customization

Override the default CSS if needed:

```python
maker.set_custom_css("""
body {
    font-family: "Times New Roman", serif;
    line-height: 1.8;
}
""")
```
