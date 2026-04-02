# Static Site Generator

A lightweight Python-based static site generator that converts Markdown content into HTML using customizable templates.

## Features

- **Markdown to HTML conversion**: Automatically converts all Markdown files to HTML
- **Recursive content processing**: Handles nested directory structures seamlessly
- **Static asset management**: Copies CSS, images, and other static files to output
- **Template-based rendering**: Uses HTML templates with variable substitution
- **Built-in HTTP server**: Includes a test server for local development
- **Flexible basepath support**: Configure base URL paths for different deployment scenarios

## Project Structure

```
.
├── content/               # Markdown content files
│   ├── index.md
│   ├── blog/
│   │   ├── glorfindel/
│   │   ├── majesty/
│   │   └── tom/
│   └── contact/
├── static/                # Static assets (CSS, images, etc.)
│   ├── index.css
│   └── images/
├── docs/                  # Generated HTML output
├── src/                   # Python source code
│   ├── main.py
│   ├── generate_pages_recursive.py
│   ├── generate_page.py
│   ├── copy_static.py
│   ├── htmlnode.py
│   ├── textnode.py
│   ├── text_to_nodes.py
│   ├── markdown_to_blocks.py
│   └── [test files]
├── template.html          # HTML template for page generation
├── main.sh                # Main entry point script
├── build.sh               # Build script
├── test.sh                # Test script
└── README.md

```

## Installation

### Requirements

- Python 3.6+

### Setup

1. Clone or download the project
2. No external dependencies required (uses Python standard library)

## Usage

### Build the Site

Run the main build script:

```bash
./main.sh
```

Or directly with Python:

```bash
python3 src/main.py
```

To specify a custom base path (useful for subdirectory deployments):

```bash
python3 src/main.py /your-base-path
```

### View the Generated Site

After building, start the development server:

```bash
cd docs && python3 -m http.server 8888
```

The site will be available at `http://localhost:8888`

### Testing

Run the test suite:

```bash
./test.sh
```

## How It Works

### 1. Content Structure

Organize your Markdown files in the `content/` directory:

```
content/
├── index.md          # Home page
├── about.md
├── blog/
│   ├── post1.md
│   └── post2.md
└── contact.md
```

Each directory will be created in the output with its own `index.html`.

### 2. Template System

The generator uses `template.html` to render pages. It supports the following template variables:

- `{{ Title }}` - Page title (extracted from Markdown metadata)
- `{{ Content }}` - Generated HTML content from Markdown

Example template:

```html
<!doctype html>
<html>
  <head>
    <title>{{ Title }}</title>
    <link href="/index.css" rel="stylesheet" />
  </head>
  <body>
    <article>{{ Content }}</article>
  </body>
</html>
```

### 3. Static Assets

All files in the `static/` directory are copied to the output directory:

```
static/
├── index.css
└── images/
```

These are available at the root path in your generated site (e.g., `/index.css`).

### 4. Build Process

The generator performs these steps:

1. **Delete output**: Removes the existing `docs/` directory
2. **Copy static files**: Recursively copies all static assets to `docs/`
3. **Generate pages**: Converts Markdown files to HTML using the template

### Write Content

Create `.md` files in the `content/` directory and they'll automatically be converted to HTML on the next build.

## License

See LICENSE file for details.
