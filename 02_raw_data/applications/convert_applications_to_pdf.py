"""
Convert all Markdown application documents in 02_raw_data/applications/
into publication-grade, professional PDF documents using xhtml2pdf and markdown.
Includes robust table formatting with explicit column widths to prevent overlapping text.
"""

import os
import re
import markdown
from bs4 import BeautifulSoup
from xhtml2pdf import pisa

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CSS_STYLE = """
@page {
    size: a4 portrait;
    margin-top: 2.2cm;
    margin-bottom: 2.2cm;
    margin-left: 2.0cm;
    margin-right: 2.0cm;
    
    @top-left {
        content: "University of Europe for Applied Sciences | Potsdam Campus";
        font-family: Helvetica, Arial, sans-serif;
        font-size: 7.5pt;
        color: #64748b;
        border-bottom: 0.5pt solid #cbd5e1;
        padding-bottom: 4px;
    }
    @top-right {
        content: "Research Data Access Application (FDZ)";
        font-family: Helvetica, Arial, sans-serif;
        font-size: 7.5pt;
        color: #64748b;
        border-bottom: 0.5pt solid #cbd5e1;
        padding-bottom: 4px;
    }
    @bottom-left {
        content: "Applicant: Cristhian David C\u00e1ceres Mateus (ID: 93515346)";
        font-family: Helvetica, Arial, sans-serif;
        font-size: 7.5pt;
        color: #64748b;
        border-top: 0.5pt solid #cbd5e1;
        padding-top: 4px;
    }
    @bottom-right {
        content: "Page " counter(page) " of " counter(pages);
        font-family: Helvetica, Arial, sans-serif;
        font-size: 7.5pt;
        color: #64748b;
        border-top: 0.5pt solid #cbd5e1;
        padding-top: 4px;
    }
}

body {
    font-family: Helvetica, Arial, sans-serif;
    font-size: 9.5pt;
    line-height: 1.45;
    color: #1e293b;
}

h1 {
    font-size: 15.5pt;
    font-weight: bold;
    color: #0f2e5a;
    margin-top: 0;
    margin-bottom: 4px;
    line-height: 1.25;
}

h2 {
    font-size: 12pt;
    font-weight: bold;
    color: #1e3a8a;
    margin-top: 10px;
    margin-bottom: 8px;
    border-bottom: 1.5pt solid #0f2e5a;
    padding-bottom: 3px;
}

h3 {
    font-size: 10.5pt;
    font-weight: bold;
    color: #1e40af;
    margin-top: 10px;
    margin-bottom: 4px;
}

h4 {
    font-size: 9.5pt;
    font-weight: bold;
    color: #334155;
    margin-top: 8px;
    margin-bottom: 2px;
}

p {
    margin-top: 4px;
    margin-bottom: 6px;
    text-align: justify;
}

ul, ol {
    margin-top: 3px;
    margin-bottom: 6px;
    padding-left: 20px;
}

li {
    margin-bottom: 3px;
}

blockquote {
    margin-left: 0;
    margin-right: 0;
    margin-top: 6px;
    margin-bottom: 8px;
    padding: 8px 12px;
    background-color: #f8fafc;
    border-left: 3.5pt solid #0f2e5a;
    font-style: italic;
    color: #334155;
}

table {
    width: 100%;
    margin-top: 8px;
    margin-bottom: 12px;
}

th {
    background-color: #f1f5f9;
    color: #0f2e5a;
    font-weight: bold;
    font-size: 8pt;
    padding: 5px 6px;
    border: 0.5pt solid #cbd5e1;
    text-align: left;
}

td {
    padding: 4.5px 6px;
    border: 0.5pt solid #e2e8f0;
    font-size: 8pt;
    vertical-align: top;
    line-height: 1.35;
}

hr {
    border: 0;
    border-top: 0.5pt solid #cbd5e1;
    margin-top: 10px;
    margin-bottom: 10px;
}

code {
    font-family: Courier, monospace;
    font-size: 8pt;
    background-color: #f1f5f9;
    padding: 1px 3px;
    color: #0f2e5a;
}

pre {
    font-family: Courier, monospace;
    font-size: 7.5pt;
    background-color: #f8fafc;
    border: 0.5pt solid #cbd5e1;
    padding: 6px;
    margin-top: 6px;
    margin-bottom: 6px;
}

.avoid-break {
    page-break-inside: avoid;
}
"""

def clean_latex_math(text: str) -> str:
    """Transform LaTeX math into clean, readable text/HTML for PDF rendering."""
    replacements = [
        (r'\$\\text\{AR\}_\{2026\} = 42,52\\\$', '<b>AR<sub>2026</sub> = EUR 42.52</b>'),
        (r'\$\\text\{DE\}_\{2026\} = 51\.944\\\$', '<b>DE<sub>2026</sub> = EUR 51,944</b>'),
        (r'\$\\text\{BBG\} = 101\.400\\\$', '<b>BBG = EUR 101,400</b>'),
        (r'\$Rente = EP \\times ZF \\times AR\$', '<i>Rente = EP * ZF * AR</i>'),
        (r'\$S\^\*\$', '<i>S*</i>'),
        (r'\$\\text\{EP\}_\{\\text\{max\}\} = 1\.9521\$', 'EP<sub>max</sub> = 1.9521'),
        (r'\$\\beta_\{\\text\{residence\}\} > 0, \\beta_\{\\text\{residence\}\^2\} < 0\$', 'beta<sub>residence</sub> &gt; 0, beta<sub>residence^2</sub> &lt; 0'),
        (r'\$\\text\{IHS\}\(W_i\) = \\ln\\left\(W_i \+ \\sqrt\{W_i\^2 \+ 1\}\\right\)\$', '<b>IHS(W<sub>i</sub>) = ln(W<sub>i</sub> + sqrt(W<sub>i</sub>^2 + 1))</b>'),
        (r'\$\\text\{Net Wealth\} = \\text\{Assets\} - \\text\{Liabilities\}\$', '<b>Net Wealth = Assets - Liabilities</b>'),
        (r'\$\\ln\(\\text\{Wage\}_\{it\}\) = \\alpha \+ \\beta_1 \\text\{Duration\}_\{it\} \+ \\beta_2 \\text\{Duration\}_\{it\}\^2 \+ \\beta_3 \\text\{Tertiary\}_i \+ \\beta_4 \\text\{German\\_B2C2\}_\{it\} - \\beta_5 \\text\{Deskilling\}_\{it\} \+ \\mathbf\{X\}_\{it\}\'\\boldsymbol\{\\gamma\} \+ \\varepsilon_\{it\}\$', '<b>ln(Wage<sub>it</sub>) = alpha + beta<sub>1</sub> Duration<sub>it</sub> + beta<sub>2</sub> Duration<sub>it</sub>^2 + beta<sub>3</sub> Tertiary<sub>i</sub> + beta<sub>4</sub> German_B2C2<sub>it</sub> - beta<sub>5</sub> Deskilling<sub>it</sub> + X<sub>it</sub>\'gamma + epsilon<sub>it</sub></b>'),
    ]
    for pattern, repl in replacements:
        text = re.sub(pattern, repl, text)
    
    # Generic math cleanup
    def repl_display_math(match):
        inner = match.group(1).strip()
        inner = inner.replace(r'\text{', '').replace('}', '')
        inner = inner.replace(r'\ln', 'ln').replace(r'\sqrt', 'sqrt')
        inner = inner.replace(r'\alpha', 'alpha').replace(r'\beta', 'beta').replace(r'\gamma', 'gamma').replace(r'\varepsilon', 'epsilon')
        inner = inner.replace(r'\times', '*').replace(r'\le', '&lt;=').replace(r'\ge', '&gt;=')
        return f"<div style='text-align:center; margin:8px 0; font-style:italic; font-weight:bold;'>{inner}</div>"
    
    text = re.sub(r'\$\$(.*?)\$\$', repl_display_math, text, flags=re.DOTALL)
    
    def repl_inline_math(match):
        inner = match.group(1).strip()
        inner = inner.replace(r'\text{', '').replace('}', '')
        inner = inner.replace(r'\times', '*').replace(r'\le', '&lt;=').replace(r'\ge', '&gt;=')
        inner = inner.replace(r'\alpha', 'alpha').replace(r'\beta', 'beta').replace(r'\gamma', 'gamma')
        return f"<i>{inner}</i>"
    
    text = re.sub(r'\$(.*?)\$', repl_inline_math, text)
    
    # Direct unicode character replacements for standard Type 1 fonts
    unicode_map = {
        '≥': '&gt;=',
        '≤': '&lt;=',
        '√': 'sqrt',
        '²': '^2',
        '³': '^3',
        'β': 'beta',
        'α': 'alpha',
        'γ': 'gamma',
        'ε': 'epsilon',
        '₁': '1',
        '₂': '2',
        '₃': '3',
        '₄': '4',
        '₅': '5',
        '×': '*',
        '–': '-',
        '—': '--',
        '“': '"',
        '”': '"',
        '‘': "'",
        '’': "'",
        '→': '-&gt;',
        '€': 'EUR ',
    }
    for char, rep in unicode_map.items():
        text = text.replace(char, rep)
        
    return text

def format_html_tables(html_content: str) -> str:
    """Ensure explicit column widths and wrap cells to prevent text overlapping in xhtml2pdf."""
    soup = BeautifulSoup(html_content, 'html.parser')
    for table in soup.find_all('table'):
        # Enforce table attributes
        table['style'] = 'width: 100%; margin-top: 8px; margin-bottom: 12px;'
        
        # Check column count
        rows = table.find_all('tr')
        if not rows:
            continue
            
        first_row_cells = rows[0].find_all(['th', 'td'])
        num_cols = len(first_row_cells)
        
        if num_cols == 7:
            widths = ['12%', '24%', '14%', '14%', '8%', '10%', '18%']
        elif num_cols == 5:
            widths = ['18%', '20%', '21%', '21%', '20%']
        elif num_cols == 4:
            widths = ['25%', '27%', '24%', '24%']
        elif num_cols == 3:
            widths = ['25%', '35%', '40%']
        elif num_cols == 2:
            widths = ['32%', '68%']
        else:
            widths = [f"{100 // num_cols}%"] * num_cols if num_cols > 0 else []
            
        # Assign explicit width attribute to all cells in each row
        for row in rows:
            cells = row.find_all(['th', 'td'])
            for idx, cell in enumerate(cells):
                if idx < len(widths):
                    cell['width'] = widths[idx]
                
                # Replace inline code tags inside tables with regular styled spans to avoid wide Courier
                for code_tag in cell.find_all('code'):
                    code_tag.name = 'span'
                    code_tag['style'] = 'font-family: Courier, monospace; font-size: 7.5pt; color: #0f2e5a;'

    return str(soup)

def convert_md_to_pdf(md_path: str, pdf_path: str):
    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # Pre-process math and font characters
    processed_text = clean_latex_math(md_text)
    
    # Convert Markdown to HTML
    raw_html_body = markdown.markdown(
        processed_text,
        extensions=['tables', 'fenced_code', 'nl2br']
    )
    
    # Fix table widths and cell wrapping with BeautifulSoup
    html_body = format_html_tables(raw_html_body)

    full_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
{CSS_STYLE}
</style>
</head>
<body>
{html_body}
</body>
</html>
"""
    try:
        with open(pdf_path, 'wb') as f_out:
            pisa_status = pisa.CreatePDF(full_html, dest=f_out)
            if pisa_status.err:
                print(f"Error converting {os.path.basename(md_path)}: {pisa_status.err}")
            else:
                print(f"Successfully generated: {os.path.basename(pdf_path)}")
    except PermissionError:
        alt_path = pdf_path.replace('.pdf', '_updated.pdf')
        with open(alt_path, 'wb') as f_out:
            pisa_status = pisa.CreatePDF(full_html, dest=f_out)
            if pisa_status.err:
                print(f"Error converting {os.path.basename(md_path)} to alt: {pisa_status.err}")
            else:
                print(f"File is currently open in your viewer: Generated updated version at {os.path.basename(alt_path)}")

def main():
    files = [
        "DATA_REQUEST_SPECIFICATION.md",
        "00_DATA_REQUEST_MASTER_GUIDE.md",
        "01_FDZ_RV_Antrag_Datennutzung_VSKT.md",
        "02_Bundesbank_RDSC_Application_PHF.md",
        "03_IAB_FDZ_Antrag_SUF_Refugees_SOEP.md",
        "04_Destatis_FDZ_Antrag_Mikrozensus_EVS.md",
        "05_Betreuerbefuerwortung_Supervisor_Endorsement_Letter.md",
    ]
    
    for f in files:
        md_path = os.path.join(BASE_DIR, f)
        pdf_name = f.replace('.md', '.pdf')
        pdf_path = os.path.join(BASE_DIR, pdf_name)
        if os.path.exists(md_path):
            convert_md_to_pdf(md_path, pdf_path)
            
    # Also convert the official data foundation report
    reports_dir = os.path.normpath(os.path.join(BASE_DIR, "..", "..", "08_outputs", "reports"))
    foundation_md = os.path.join(reports_dir, "OFFICIAL_DATA_FOUNDATION_AND_URL_GUIDE.md")
    if os.path.exists(foundation_md):
        foundation_pdf = os.path.join(reports_dir, "OFFICIAL_DATA_FOUNDATION_AND_URL_GUIDE.pdf")
        convert_md_to_pdf(foundation_md, foundation_pdf)

if __name__ == "__main__":
    main()
