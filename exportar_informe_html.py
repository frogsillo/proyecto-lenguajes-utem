import os
import re

REPO_DIR = '/home/frog/.gemini/antigravity/scratch/proyecto_lenguajes'
MD_PATH = os.path.join(REPO_DIR, 'INFORME_FINAL_LISTO.md')
HTML_PATHS = [
    os.path.join(REPO_DIR, 'INFORME_FINAL_LISTO.html'),
    os.path.join(REPO_DIR, 'docs/INFORME_FINAL_UTEM.html'),
    os.path.join(REPO_DIR, 'docs/INFORME_FINAL_LISTO.html')
]

with open(MD_PATH, 'r', encoding='utf-8') as f:
    md_content = f.read()

lines = md_content.splitlines()
html_lines = []
in_code = False
code_lang = ""
code_buffer = []

def escape_html(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

html_lines.append("""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Informe Final Tarea 1 - Lenguajes de Programación UTEM</title>
    <style>
        @page {
            size: letter;
            margin: 3.0cm;
        }
        body {
            font-family: 'Calibri', 'Segoe UI', Arial, sans-serif;
            font-size: 12pt;
            line-height: 1.5;
            color: #1a1a1a;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
        }
        h1 {
            font-size: 18pt;
            color: #0b3b60;
            border-bottom: 2px solid #0b3b60;
            padding-bottom: 6px;
            margin-top: 28pt;
            page-break-before: always;
        }
        h2 {
            font-size: 15pt;
            color: #1864ab;
            margin-top: 20pt;
            page-break-after: avoid;
        }
        h3 {
            font-size: 13pt;
            color: #2b8a3e;
            margin-top: 14pt;
            page-break-after: avoid;
        }
        h4 {
            font-size: 12pt;
            color: #c92a2a;
            margin-top: 10pt;
            font-weight: bold;
        }
        p, li {
            text-align: justify;
            margin-bottom: 6pt;
        }
        pre {
            background-color: #f1f3f5;
            border: 1px solid #ced4da;
            border-radius: 4px;
            padding: 10px 14px;
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 9.5pt;
            line-height: 1.25;
            overflow-x: auto;
            white-space: pre-wrap;
            word-wrap: break-word;
            margin: 10pt 0;
            page-break-inside: avoid;
        }
        code {
            font-family: 'Consolas', 'Courier New', monospace;
            font-size: 10pt;
            background-color: #e9ecef;
            padding: 2px 4px;
            border-radius: 3px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 14pt 0;
            font-size: 11pt;
            page-break-inside: avoid;
        }
        th, td {
            border: 1px solid #adb5bd;
            padding: 6px 10px;
            text-align: left;
        }
        th {
            background-color: #e7f5ff;
            color: #1864ab;
            font-weight: bold;
        }
        blockquote {
            border-left: 4px solid #1864ab;
            padding: 6px 14px;
            margin: 10pt 0;
            background-color: #f8f9fa;
            font-style: italic;
        }
        hr {
            border: none;
            border-top: 1px solid #ced4da;
            margin: 20pt 0;
        }
    </style>
</head>
<body>
""")

for line in lines:
    if line.startswith("```"):
        if in_code:
            in_code = False
            html_lines.append(f"<pre><code>{escape_html(chr(10).join(code_buffer))}</code></pre>")
            code_buffer = []
        else:
            in_code = True
            code_lang = line[3:].strip()
        continue
    
    if in_code:
        code_buffer.append(line)
        continue

    # Encabezados
    if line.startswith("# "):
        html_lines.append(f"<h1>{escape_html(line[2:])}</h1>")
    elif line.startswith("## "):
        html_lines.append(f"<h2>{escape_html(line[3:])}</h2>")
    elif line.startswith("### "):
        html_lines.append(f"<h3>{escape_html(line[4:])}</h3>")
    elif line.startswith("#### "):
        html_lines.append(f"<h4>{escape_html(line[5:])}</h4>")
    elif line.startswith("> "):
        html_lines.append(f"<blockquote>{escape_html(line[2:])}</blockquote>")
    elif line.strip() == "---":
        html_lines.append("<hr>")
    elif line.startswith("|") and line.endswith("|"):
        parts = [p.strip() for p in line.split("|")[1:-1]]
        if all(re.match(r"^:?-+:?$", p) for p in parts):
            continue
        if "<table" not in html_lines[-1] and "<tr" not in html_lines[-1]:
            html_lines.append("<table>")
            html_lines.append("<tr>" + "".join(f"<th>{escape_html(p)}</th>" for p in parts) + "</tr>")
        else:
            html_lines.append("<tr>" + "".join(f"<td>{escape_html(p)}</td>" for p in parts) + "</tr>")
    else:
        if html_lines and html_lines[-1].startswith("<tr"):
            html_lines.append("</table>")
        if line.strip():
            l = escape_html(line)
            l = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", l)
            l = re.sub(r"\*(.*?)\*", r"<em>\1</em>", l)
            l = re.sub(r"`(.*?)`", r"<code>\1</code>", l)
            html_lines.append(f"<p>{l}</p>")

if in_code:
    html_lines.append(f"<pre><code>{escape_html(chr(10).join(code_buffer))}</code></pre>")

if html_lines and html_lines[-1].startswith("<tr"):
    html_lines.append("</table>")

html_lines.append("</body></html>")

html_full_text = "\n".join(html_lines)
for p in HTML_PATHS:
    with open(p, 'w', encoding='utf-8') as f:
        f.write(html_full_text)
    print(f"HTML generado en: {p}")
