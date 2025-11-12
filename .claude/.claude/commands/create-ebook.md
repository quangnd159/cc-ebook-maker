---
description: Create a beautiful, professionally-formatted EPUB ebook from various sources with bilingual support
argument-hint: [requirements] [source-path-or-url]
allowed-tools: Read, Write, Bash(source venv/bin/activate:*), Bash(python3:*), Bash(pip3 install:*), WebFetch, WebSearch, Task(general-purpose:*), Glob, Grep, TodoWrite
---

# Create Professional EPUB Ebook

You are an expert ebook creator using the professional ebook-maker system located in `/Users/quangnguyendang/ebook-maker/`.

## Your Task

Create a beautiful EPUB ebook based on the user's requirements and source content.

## Step-by-Step Workflow

### 1. Parse Requirements

Extract from the user's input:
- **Book title** (required)
- **Author name** (default: "Unknown")
- **Language** (default: "en")
- **Bilingual?** If yes, identify source and target languages
- **Glossary?** Should difficult terms be explained?
- **Chapter structure** How should the content be organized?
- **Any special formatting** needs

### 2. Extract Content from Source

The user can provide content in multiple ways:

**Text File (.txt, .md)**
- Use Read tool to load the file
- Parse the content directly

**PDF File (.pdf)**
- Let the user know PDFs require special handling
- Ask if they can provide the text content another way, or use a PDF-to-text tool

**Website/URL**
- Use WebFetch tool to retrieve the content
- Extract main text from HTML using paragraph extraction

**Pasted Text**
- The user may paste the text directly in their message
- Extract it from the conversation

**Multiple Sources**
- Handle each source separately
- Combine into chapters

### 3. Translation (If Bilingual)

If the user wants a bilingual ebook:
1. Split the text into logical sections (3-5 sections for parallel processing)
2. Use Task tool with `subagent_type=general-purpose` to translate EACH section in PARALLEL
3. Collect translations from all agents
4. Identify 10-15 difficult/philosophical terms
5. Create glossary with term translations and explanations

**Important**: Run translation agents in PARALLEL for speed - make ONE message with MULTIPLE Task tool calls.

### 4. Generate Python Script

Create a Python script in `/Users/quangnguyendang/ebook-maker/` that:
1. Imports from `ebook_maker` module
2. Creates `EbookMaker` instance with proper metadata
3. Adds glossary (if requested) using `add_glossary()`
4. For bilingual books:
   - Builds proper HTML with `.original-text` and `.translation` CSS classes
   - Adds chapter using `add_chapter()` with `content_is_html=True`
5. For regular books:
   - Adds chapters using `add_chapter()` with plain text or HTML
6. Saves to `output/` directory

### 5. Execute and Deliver

1. Change to the ebook-maker directory
2. Activate virtual environment: `source venv/bin/activate`
3. Run the generated script: `python3 script_name.py`
4. Verify the EPUB was created
5. Tell the user the location of their new ebook

## Important Notes

**Professional Formatting:**
- The system uses EbookLib with Georgia serif font, 1.7 line-height, 5% margins
- Bilingual content: original text regular, translation in italics
- All EPUBs will be beautiful and professional automatically

**Bilingual Best Practices:**
- Original language in `<p class="original-text">`
- Translation in `<p class="translation">`
- Keep original formatting (speaker names, emphasis, etc.)
- NO added headings - preserve exact original structure

**Error Handling:**
- If venv doesn't exist, create it and install requirements
- If source file not found, ask user for correct path
- If translation fails, offer to continue with original text only

**Output Location:**
- Always save EPUBs to: `/Users/quangnguyendang/ebook-maker/output/`
- Give user the full absolute path when done

## Example Workflows

**Simple book from file:**
```
User: Create an ebook "My Story" from story.txt
→ Read story.txt
→ Generate script with add_chapter()
→ Execute and deliver
```

**Bilingual book:**
```
User: Make a Chinese-Vietnamese bilingual epub from courage.md with glossary
→ Read courage.md
→ Launch 3 parallel translation agents
→ Identify difficult terms
→ Generate script with glossary + bilingual HTML
→ Execute and deliver
```

**Book from website:**
```
User: Create epub from https://example.com/article title "Web Article"
→ WebFetch the URL
→ Extract clean text
→ Generate script
→ Execute and deliver
```

## Code Example Structure

```python
from ebook_maker import EbookMaker

maker = EbookMaker(
    title="Book Title",
    author="Author Name",
    language="vi",
    description="Description"
)

# Add glossary if needed
glossary_terms = [
    {'term': 'Original (Translation)', 'translation': 'Translation', 'explanation': 'Explanation...'}
]
maker.add_glossary(glossary_terms, title="Glossary Title")

# Add bilingual chapter
html_content = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>Chapter Title</title>
    <link rel="stylesheet" href="style/nav.css" type="text/css"/>
</head>
<body>
    <h2>Chapter Title</h2>
    <p class="original-text">Original paragraph</p>
    <p class="translation">Translated paragraph</p>
</body>
</html>'''

maker.add_chapter("Chapter Title", html_content, content_is_html=True)
maker.save("output/book.epub")
```

## User Communication

- Use TodoWrite to track progress
- Keep user informed of each step
- Show translation progress when using parallel agents
- Provide the final EPUB path prominently
- Suggest they can adjust requirements if needed

Now process the user's request following this workflow!
