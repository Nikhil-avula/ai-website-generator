# AI Website Generator

This project is a Streamlit-based application that generates complete, functional websites from a single natural language prompt using a Large Language Model.

The application automatically creates separate HTML, CSS, and JavaScript files and packages them into a downloadable ZIP file.

---

## Features

- Generate complete websites from a single text prompt
- Produces clean and production-ready HTML, CSS, and JavaScript
- Enforces strict output structure for reliable file generation
- Automatically saves generated files with UTF-8 encoding
- Packages all files into a downloadable ZIP archive
- Simple and intuitive Streamlit user interface

---

## Tech Stack

- Python
- Streamlit
- LangChain
- Google Gemini API (2.5 Flash)
- HTML, CSS, JavaScript
- Git

---

## How It Works

1. User enters a website or game description as a prompt.
2. The prompt is sent to Google Gemini using LangChain with a strict system instruction.
3. The model returns structured code output for HTML, CSS, and JavaScript.
4. The application parses and saves each file separately.
5. All files are bundled into a ZIP file for download.

---

