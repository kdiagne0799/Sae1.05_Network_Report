# 🛡️ NetTrace Investigator

![Python](https://img.shields.io/badge/Language-Python_3.x-blue?style=for-the-badge&logo=python)  
![Status](https://img.shields.io/badge/Status-Stable-success?style=for-the-badge)  
![Domain](https://img.shields.io/badge/Domain-Network_Threat_Analysis-red?style=for-the-badge)

## Overview

**NetTrace Investigator** is a small toolchain designed to analyze raw network traces (exported from `tcpdump`) and produce a structured security report (Markdown → HTML). The goal is to transform hard-to-read raw dumps into clear, actionable outputs highlighting suspicious behaviors and relevant indicators.

---

## Key Features

- **Data preparation**
  - Read a dump file (`DumpFile.txt`).
  - Extract relevant fields (IP addresses, ports, timestamps, TCP flags).
  - Export a clean CSV (`Network_Analysis.csv`).

- **Security analysis**
  - Detect common attack patterns (SSH brute force, port scans, SYN floods).
  - Identify unencrypted traffic and risky services.

- **Reporting**
  - Generate a Markdown report (`Network_Report.md`).
  - Convert the report to a styled HTML page (`Network_Report.html`).

---

## Pipeline

```mermaid
graph LR
    A[DumpFile.txt] -->|txt_to_csv.py| B[Network_Analysis.csv]
    B -->|csv_to_md.py| C[Network_Report.md]
    C -->|md_to_html.py| D[Network_Report.html]
```

> Modular approach: each step is independent and replaceable (e.g., swap HTML generator).

---

## Project structure

| File | Purpose |
|---|---|
| `DumpFile.txt` | Example raw dump from tcpdump |
| `txt_to_csv.py` | Extraction/cleanup → CSV |
| `csv_to_md.py` | Analysis → generate Markdown report |
| `md_to_html.py` | Convert Markdown → HTML |
| `Network_Analysis.csv` | Structured data (Excel/Pandas ready) |
| `Network_Report.md` | Analysis report (Markdown) |
| `Network_Report.html` | Final report (HTML) |

---

## Requirements

- Python 3.x
- Standard library only (`os`, `csv`, `re`, `collections`, etc.) — no external packages required.

---

## Quick start

Run the full pipeline from the project root:

```bash
python txt_to_csv.py        # -> Network_Analysis.csv
python csv_to_md.py        # -> Network_Report.md
python md_to_html.py       # -> Network_Report.html
```

Each script can be executed separately if you only need a specific step.

---

## Usage (detailed)

- `txt_to_csv.py`
  - Input: `DumpFile.txt`
  - Output: `Network_Analysis.csv`
  - Usage: `python txt_to_csv.py [--input DumpFile.txt] [--output Network_Analysis.csv]`

- `csv_to_md.py`
  - Input: `Network_Analysis.csv`
  - Output: `Network_Report.md`
  - Usage: `python csv_to_md.py [--input Network_Analysis.csv] [--output Network_Report.md]`

- `md_to_html.py`
  - Input: `Network_Report.md`
  - Output: `Network_Report.html`
  - Usage: `python md_to_html.py [--input Network_Report.md] [--output Network_Report.html]`

---

## Output format & examples

- Expected CSV header example:

```
timestamp,src_ip,src_port,dst_ip,dst_port,protocol,flags,info
```

- Example alerts produced in the report:
  - IP 192.168.190.130: 66 SSH attempts within 5 minutes →  brute force.
  - High rate of SYN packets toward a single target →  DoS.

---

## Development & Contributing

- Tests: add fixtures under `tests/` and provide simple verification scripts.
- Contribution flow: fork → branch → PR. Keep commits small and add clear descriptions.
- Potential improvements: CLI options, time/IP filters, JSON export.

---

## License & contact

- License: add a `LICENSE` file to define project license.
- Author / contact: kdiagne799@gmail.com
 
