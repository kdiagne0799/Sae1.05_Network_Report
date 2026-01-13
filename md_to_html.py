import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
os.chdir(BASE_DIR)


def simple_md_to_html(input_md: str, output_html: str) -> None:
    """
    Convertit un Markdown simple en rapport HTML stylé.
    """
    try:
        md_path = Path(input_md)

        if not md_path.exists():
            print(f"[ERREUR] Fichier introuvable : {md_path}")
            return

        with md_path.open("r", encoding="utf-8") as f:
            lines = f.readlines()

        html_content = []
        in_table = False

        for raw_line in lines:
            line = raw_line.strip()

            # Titres
            if line.startswith("# "):
                html_content.append(f"<h1>{line[2:]}</h1>")
            elif line.startswith("## "):
                html_content.append(f"<h2>{line[3:]}</h2>")

            # Listes
            elif line.startswith("- "):
                html_content.append(f"<li>{line[2:]}</li>")

            # Tableaux simples
            elif "|" in line:
                if not in_table:
                    html_content.append('<table class="table table-striped table-bordered table-sm">')
                    in_table = True

                if ":---" in line or "---" in line:
                    continue

                cells = line.split("|")[1:-1]
                tag = "th" if any(
                    col_name in line
                    for col_name in (
                        "Timestamp",
                        "Source",
                        "IP Src",
                        "Src Port",
                        "IP Dest",
                        "Dest Port",
                        "Flags",
                        "Length",
                        "Info",
                    )
                ) else "td"
                row = "".join(f"<{tag}>{c.strip()}</{tag}>" for c in cells)
                html_content.append(f"<tr>{row}</tr>")

            else:
                if in_table:
                    html_content.append("</table>")
                    in_table = False

                if line:
                    html_content.append(f"<p>{line}</p>")

        if in_table:
            html_content.append("</table>")

        body_html = "\n".join(html_content)

        full_page = f"""<!DOCTYPE html>
<html lang="fr" data-theme="dark">
<head>
    <meta charset="UTF-8">
    <title>Rapport réseau</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link 
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" 
        rel="stylesheet"
    >
    <style>
        :root {{
            --bg-gradient-dark: radial-gradient(circle at top, #1d4ed8 0, #020617 45%, #020617 100%);
            --bg-gradient-light: radial-gradient(circle at top, #eff6ff 0, #dbeafe 40%, #e5e7eb 100%);
            --card-bg-dark: rgba(15, 23, 42, 0.92);
            --card-bg-light: rgba(255, 255, 255, 0.9);
            --card-border-dark: rgba(148, 163, 184, 0.6);
            --card-border-light: rgba(148, 163, 184, 0.4);
            --accent: #38bdf8;
            --accent-soft: rgba(56, 189, 248, 0.24);
            --text-main-dark: #e5e7eb;
            --text-main-light: #0f172a;
            --text-muted-dark: #9ca3af;
            --text-muted-light: #6b7280;
        }}

        * {{
            box-sizing: border-box;
        }}

        body {{
            min-height: 100vh;
            margin: 0;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 32px 16px;
            font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
            transition: background-image 0.35s ease, color 0.25s ease;
        }}

        html[data-theme="dark"] body {{
            background-image: var(--bg-gradient-dark);
            color: var(--text-main-dark);
        }}

        html[data-theme="light"] body {{
            background-image: var(--bg-gradient-light);
            color: var(--text-main-light);
        }}

        .report-shell {{
            width: 100%;
            max-width: 1080px;
        }}

        .report-card {{
            position: relative;
            border-radius: 20px;
            padding: 30px 26px;
            overflow: hidden;
            transition: box-shadow 0.35s ease, background 0.35s ease;
        }}

        html[data-theme="dark"] .report-card {{
            background: radial-gradient(circle at top left, rgba(15, 23, 42, 0.92), rgba(15, 23, 42, 0.9));
            box-shadow:
                0 25px 70px rgba(15, 23, 42, 0.85),
                0 0 0 1px rgba(15, 23, 42, 0.9);
        }}

        html[data-theme="light"] .report-card {{
            background: radial-gradient(circle at top left, #ffffff, #e5e7eb);
            box-shadow:
                0 22px 60px rgba(15, 23, 42, 0.15),
                0 0 0 1px rgba(148, 163, 184, 0.25);
        }}

        .report-card::before {{
            content: "";
            position: absolute;
            inset: -40%;
            background:
                radial-gradient(circle at top left, rgba(56, 189, 248, 0.18), transparent 55%),
                radial-gradient(circle at bottom right, rgba(34, 197, 94, 0.18), transparent 50%);
            opacity: 0.9;
            z-index: 0;
            pointer-events: none;
        }}

        .report-inner {{
            position: relative;
            z-index: 1;
            border-radius: 16px;
            padding: 24px 22px 20px;
            backdrop-filter: blur(18px);
            transition: background 0.35s ease, border-color 0.35s ease;
        }}

        html[data-theme="dark"] .report-inner {{
            background: linear-gradient(135deg, rgba(15, 23, 42, 0.96), rgba(15, 23, 42, 0.88));
            border: 1px solid var(--card-border-dark);
        }}

        html[data-theme="light"] .report-inner {{
            background: linear-gradient(135deg, rgba(255, 255, 255, 0.96), rgba(248, 250, 252, 0.9));
            border: 1px solid var(--card-border-light);
        }}

        .report-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 18px;
            margin-bottom: 16px;
        }}

        .report-title-block h1 {{
            font-size: 1.55rem;
            font-weight: 700;
            letter-spacing: 0.03em;
            margin: 0 0 4px;
        }}

        html[data-theme="dark"] .report-title-block h1 {{
            color: #f9fafb;
        }}

        html[data-theme="light"] .report-title-block h1 {{
            color: #0f172a;
        }}

        .report-title-block p {{
            margin: 0;
            font-size: 0.85rem;
        }}

        html[data-theme="dark"] .report-title-block p {{
            color: var(--text-muted-dark);
        }}

        html[data-theme="light"] .report-title-block p {{
            color: var(--text-muted-light);
        }}

        .report-badge {{
            padding: 6px 12px;
            border-radius: 999px;
            font-size: 0.75rem;
            letter-spacing: 0.11em;
            text-transform: uppercase;
            display: flex;
            align-items: center;
            gap: 8px;
            white-space: nowrap;
        }}

        html[data-theme="dark"] .report-badge {{
            border: 1px solid rgba(148, 163, 184, 0.55);
            background: radial-gradient(circle at top left, rgba(56, 189, 248, 0.18), rgba(15, 23, 42, 0.9));
            color: #e5e7eb;
        }}

        html[data-theme="light"] .report-badge {{
            border: 1px solid rgba(148, 163, 184, 0.45);
            background: radial-gradient(circle at top left, rgba(59, 130, 246, 0.12), #f9fafb);
            color: #0f172a;
        }}

        .report-badge-dot {{
            width: 7px;
            height: 7px;
            border-radius: 999px;
            background: #22c55e;
            box-shadow: 0 0 0 4px rgba(34, 197, 94, 0.35);
        }}

        .header-right {{
            display: flex;
            flex-direction: column;
            align-items: flex-end;
            gap: 8px;
        }}

        .clock {{
            font-size: 0.82rem;
            letter-spacing: 0.08em;
        }}

        html[data-theme="dark"] .clock {{
            color: var(--text-muted-dark);
        }}

        html[data-theme="light"] .clock {{
            color: var(--text-muted-light);
        }}

        .theme-toggle-btn {{
            border-radius: 999px;
            border: 1px solid rgba(148, 163, 184, 0.55);
            padding: 5px 11px;
            font-size: 0.8rem;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            cursor: pointer;
            background: transparent;
            transition: background 0.25s ease, border-color 0.25s ease, color 0.25s ease;
        }}

        html[data-theme="dark"] .theme-toggle-btn {{
            color: #e5e7eb;
        }}

        html[data-theme="light"] .theme-toggle-btn {{
            color: #0f172a;
            border-color: rgba(148, 163, 184, 0.6);
        }}

        .theme-toggle-dot {{
            width: 10px;
            height: 10px;
            border-radius: 999px;
            background: #fbbf24;
            box-shadow: 0 0 0 4px rgba(251, 191, 36, 0.35);
            transition: background 0.25s ease, box-shadow 0.25s ease;
        }}

        html[data-theme="dark"] .theme-toggle-dot {{
            background: #38bdf8;
            box-shadow: 0 0 0 4px rgba(56, 189, 248, 0.35);
        }}

        h1 {{
            font-size: 1.45rem;
            margin: 18px 0 6px;
        }}

        h2 {{
            font-size: 1.08rem;
            margin-top: 20px;
            margin-bottom: 8px;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }}

        h2::before {{
            content: "";
            display: inline-block;
            width: 9px;
            height: 9px;
            border-radius: 999px;
            background: var(--accent);
            box-shadow: 0 0 0 6px var(--accent-soft);
        }}

        p {{
            line-height: 1.6;
            margin-bottom: 0.65rem;
            font-size: 0.95rem;
        }}

        html[data-theme="dark"] p {{
            color: var(--text-main-dark);
            opacity: 0.92;
        }}

        html[data-theme="light"] p {{
            color: var(--text-main-light);
            opacity: 0.96;
        }}

        ul {{
            padding-left: 1.4rem;
            margin-bottom: 0.75rem;
        }}

        li {{
            margin-bottom: 0.25rem;
            font-size: 0.94rem;
        }}

        html[data-theme="dark"] li {{
            color: var(--text-main-dark);
            opacity: 0.95;
        }}

        html[data-theme="light"] li {{
            color: var(--text-main-light);
            opacity: 0.97;
        }}

        table {{
            width: 100%;
            margin-top: 0.85rem;
            font-size: 0.86rem;
            border-collapse: collapse;
            overflow: hidden;
            border-radius: 12px;
        }}

        html[data-theme="dark"] table {{
            background: rgba(15, 23, 42, 0.96);
        }}

        html[data-theme="light"] table {{
            background: #f9fafb;
        }}

        th, td {{
            border: 1px solid rgba(148, 163, 184, 0.5);
            padding: 7px 9px;
            text-align: left;
        }}

        html[data-theme="dark"] th,
        html[data-theme="dark"] td {{
            color: #e5e7eb;
        }}

        html[data-theme="light"] th,
        html[data-theme="light"] td {{
            color: #0f172a;
        }}

        html[data-theme="dark"] th {{
            background: linear-gradient(135deg, rgba(15, 23, 42, 0.98), rgba(15, 23, 42, 0.92));
        }}

        html[data-theme="light"] th {{
            background: linear-gradient(135deg, #e5e7eb, #d1d5db);
        }}

        tr:nth-child(even) td {{
            background-color: rgba(148, 163, 184, 0.08);
        }}

        tr:nth-child(odd) td {{
            background-color: transparent;
        }}

        tr:hover td {{
            background-color: rgba(56, 189, 248, 0.13);
        }}

        .report-footer {{
            display: flex;
            justify-content: flex-end;
            margin-top: 16px;
            font-size: 0.78rem;
        }}

        html[data-theme="dark"] .report-footer {{
            color: var(--text-muted-dark);
        }}

        html[data-theme="light"] .report-footer {{
            color: var(--text-muted-light);
        }}

        @media (max-width: 768px) {{
            body {{
                padding: 24px 12px;
            }}
            .report-card {{
                padding: 20px 16px;
                border-radius: 16px;
            }}
            .report-inner {{
                padding: 18px 14px 14px;
                border-radius: 14px;
            }}
            .report-header {{
                flex-direction: column;
                align-items: flex-start;
            }}
            .header-right {{
                align-items: flex-start;
            }}
            .report-title-block h1 {{
                font-size: 1.3rem;
            }}
        }}
    </style>
</head>
<body>
    <div class="report-shell">
        <div class="report-card">
            <div class="report-inner">
                <header class="report-header">
                    <div class="report-title-block">
                        <h1>Network Security Report</h1>
                        <p>Génération automatique depuis le fichier <strong>{input_md}</strong></p>
                    </div>
                    <div class="header-right">
                        <div id="clock" class="clock">--:--:--</div>
                        <button id="themeToggle" class="theme-toggle-btn" type="button">
                            <span class="theme-toggle-dot"></span>
                            <span id="themeLabel">Mode sombre</span>
                        </button>
                    </div>
                </header>

                {body_html}

                <footer class="report-footer">
                    <span>Généré automatiquement en HTML – Markdown to Report</span>
                </footer>
            </div>
        </div>
    </div>

    <script>
        // Gestion du thème clair/sombre avec localStorage
        (function() {{
            const html = document.documentElement;
            const btn = document.getElementById('themeToggle');
            const label = document.getElementById('themeLabel');

            function applyTheme(theme) {{
                html.setAttribute('data-theme', theme);
                localStorage.setItem('reportTheme', theme);
                label.textContent = theme === 'dark' ? 'Mode sombre' : 'Mode clair';
            }}

            const saved = localStorage.getItem('reportTheme') || 'dark';
            applyTheme(saved);

            btn.addEventListener('click', function () {{
                const current = html.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
                applyTheme(current);
            }});
        }})();

        // Horloge digitale en haut à droite
        (function() {{
            const clockEl = document.getElementById('clock');

            function updateClock() {{
                const now = new Date();
                let h = now.getHours().toString().padStart(2, '0');
                let m = now.getMinutes().toString().padStart(2, '0');
                let s = now.getSeconds().toString().padStart(2, '0');
                clockEl.textContent = h + ':' + m + ':' + s;
            }}

            updateClock();
            setInterval(updateClock, 1000);
        }})();
    </script>
</body>
</html>"""

        with open(output_html, "w", encoding="utf-8") as f:
            f.write(full_page)

        print(f"[OK] Rapport généré : {output_html}")

    except Exception as e:
        print(f"[ERREUR] Une exception est survenue : {e}")


if __name__ == "__main__":
    simple_md_to_html("Network_Report.md", "Network_Report.html")
