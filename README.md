# 🛡️ NetTrace Investigator

![Python](https://img.shields.io/badge/Language-Python_3.x-blue?style=for-the-badge&logo=python)  
![Status](https://img.shields.io/badge/Status-Stable-success?style=for-the-badge)  
![Domain](https://img.shields.io/badge/Domain-Network_Threat_Analysis-red?style=for-the-badge)

---

## 📋 Contexte pédagogique

Ce projet a été réalisé dans le cadre de la **SAE 1.05 - Traiter des données** (BUT Réseaux & Télécommunications - Semestre 1) à l'IUT de Roanne.

### Problématique

Le réseau d'une entreprise (site en Inde) sature. Les vérifications classiques (Wireshark, tests réseau, configurations) n'ont rien donné. Il faut analyser un fichier `tcpdump` pour identifier les activités suspectes responsables de la saturation.

### 🎯 Compétences visées (RT3)

**Compétence RT3** : Créer des outils et applications informatiques pour les Réseaux & Télécommunications

**Apprentissages critiques mobilisés :**
- **AC03.11** : Utiliser un système informatique et ses outils (Python, Git, tcpdump)
- **AC03.12** : Lire, exécuter, corriger et modifier un programme
- **AC03.13** : Traduire un algorithme dans un langage et pour un environnement donné
- **AC03.14** : Connaître l'architecture et les technologies d'un site Web (Markdown → HTML)
- **AC03.15** : Choisir les mécanismes de gestion de données adaptés (CSV, dictionnaires, listes)
- **AC03.16** : S'intégrer dans un environnement propice au développement collaboratif (GitHub)

### 📦 Livrables attendus

- ✅ Code Python hébergé sur GitHub
- ✅ Notice d'utilisation en anglais (ce README)
- ✅ Présentation orale de 12 minutes avec démonstration
- ✅ Traitement Excel du fichier CSV
- ✅ Portfolio avec pièces justificatives

---

## 📑 Table of contents

- [Professor Requirements Checklist](#-professor-requirements-checklist)
- [Project Overview](#-project-overview)
- [Prerequisites](#-prerequisites)
- [Quick Install & Run](#-quick-install--run-pipeline)
- [Scripts & File Descriptions](#-scripts--file-descriptions)
- [Security Analysis - Detection Thresholds](#-security-analysis---detection-thresholds)
- [Input / Output Formats](#-input--output-formats-and-examples)
- [Excel Analysis](#-excel-analysis)
- [Demo Preparation (12 min)](#-how-to-prepare-the-demo-presentation)
- [Troubleshooting](#-troubleshooting)
- [Testing & Fixtures](#-testing--fixtures)
- [Contributing](#-contributing)
- [License & Contact](#-license--contact)

---

## ✅ Professor requirements checklist

Use this checklist to ensure your repository meets grading expectations:

- [ ] Code present and runnable (`txt_to_csv.py`, `csv_to_md.py`, `md_to_html.py`)
- [ ] README in English with installation, usage, expected outputs
- [ ] Sample input file (`DumpFileB2.txt`) and outputs included
- [ ] Demo script (`run_report.py`) that runs the full pipeline
- [ ] Evidence of testing (unit tests or fixtures) in `/tests` or `/fixtures`
- [ ] Presentation notes/slides (12 minutes) and demo plan
- [ ] Code quality: docstrings, readable variable names, inline comments
- [ ] Excel analysis of CSV file (charts, pivot tables)
- [ ] README links project deliverables to competencies (AC03.11–AC03.16)

---

## 📖 Project overview

**NetTrace Investigator** is a compact Python toolchain that converts raw `tcpdump` output into an actionable network security report (CSV → Markdown → HTML).

**Goal:** Transform hard-to-read packet dumps into clear, structured outputs highlighting:
- SSH brute force attacks
- Port scanning activity
- ICMP floods (DoS)
- Top bandwidth consumers

This project was developed to investigate network saturation issues when traditional methods failed, by processing `tcpdump` logs through automated Python analysis.

---

## ✅ Prerequisites

- **Python 3.8 or newer**
- Place `DumpFileB2.txt` (or your tcpdump export) in the project root directory
- **No external packages required** (standard library only: `os`, `csv`, `re`, `collections`, `datetime`)
- **Optional:** Microsoft Excel for manual CSV analysis

---

## 🚀 Quick install & run (pipeline)

### Option 1: Run each script manually

```bash
# Step 1: Parse raw dump → CSV
python txt_to_csv.py
# → Creates Network_Analysis.csv (delimiter: `;`)

# Step 2: Analyze CSV → Markdown report
python csv_to_md.py
# → Creates Network_Report.md

# Step 3: Convert Markdown → HTML
python md_to_html.py
# → Creates Network_Report.html
Option 2: Run entire pipeline in one command
bash
python run_report.py
# → Executes all 3 steps automatically
🧩 Scripts & file descriptions
File	Purpose
DumpFileB2.txt	Raw tcpdump export (input)
txt_to_csv.py	Parse dump → extract timestamps, IPs, ports, flags, lengths → write CSV
csv_to_md.py	Analyze CSV → detect attacks, top talkers → generate Markdown report
md_to_html.py	Convert Markdown → styled HTML with embedded CSS
Network_Analysis.csv	Structured data (delimiter: ;) - Excel ready
Network_Report.md	Security analysis report (Markdown format)
Network_Report.html	Final styled report (standalone HTML)
run_report.py	(Optional) Run full pipeline in one command
🔍 Security analysis - Detection thresholds
The tool uses threshold-based heuristics to detect suspicious patterns:

1. Critical Threat: Targeted SSH Attack
🔴 Main Assault: 192.168.190.130 (66 packets). Brute Force confirmed.

Threshold: More than 50 SSH connection attempts (port 22) from a single source IP

Logic: Groups SSH packets by source IP and timestamp, flags IPs exceeding threshold

Detected: 66 connection attempts from 192.168.190.130 to port 22

Recommendation: Block source IP immediately and enable fail2ban

2. Other Detected Anomalies
⚠️ Port Scanning
Host probed 135 different ports.

Threshold: A single source IP connects to more than 20 different destination ports on the same target

Logic: Analyzes unique (src_ip, dst_ip, dst_port) combinations

Detected: Scanning activity targeting 135 unique ports

Recommendation: Investigate source host for compromise, implement port knocking

⚠️ ICMP Flood
84 packets detected. Potential DoS.

Threshold: More than 50 ICMP packets in a short time frame

Logic: Counts ICMP echo requests per source

Detected: 84 ICMP packets indicating flood attempt

Recommendation: Rate-limit ICMP traffic, block suspicious sources

Additional Detection Capabilities
Unencrypted Traffic Detection
Ports monitored: HTTP (80), Telnet (23), FTP (21)

Recommendation: Migrate to HTTPS, SSH, SFTP

Top Talkers Analysis
Lists most active IPs by packet count

Identifies bandwidth hogs or compromised hosts

🔎 Input / Output formats and examples
CSV Structure
Header (delimiter ;):

text
Timestamp;Source_IP;Source_Port;Dest_IP;Dest_Port;Flags;Length;Packet_Info
Example row:

text
15:34:04.766656;192.168.1.100;52341;10.0.0.5;22;S;60;SSH connection attempt
Markdown Report Example
The generated report includes:

text
## 🚨 Critical Alerts

### 1. Critical Threat: Targeted SSH Attack
🔴 **Main Assault**: `192.168.190.130` (66 packets). Brute Force confirmed.

### 2. Other Detected Anomalies
⚠️ **Port Scanning**: Host probed **135** different ports.
⚠️ **ICMP Flood**: 84 packets detected. Potential DoS.
HTML Report
The HTML output includes:

✅ Professional styling with Bootstrap + embedded CSS

✅ Color-coded sections (🔴 critical alerts, ⚠️ warnings)

✅ Tables for structured data

✅ Standalone file (no external dependencies)

✅ Ready for presentation or email sharing

📈 Excel analysis
The generated Network_Analysis.csv (delimiter ;) can be imported into Excel for additional analysis:

Import steps:
Open Excel → Data → Get Data → From Text/CSV

Select Network_Analysis.csv

Choose delimiter: semicolon (;)

Import data

Recommended analyses:
Pivot Tables:
Traffic volume by IP address

Port usage distribution

Timeline of suspicious activity

Charts:
Top 10 source IPs by packet count (horizontal bar chart)

Protocol distribution (pie chart: TCP vs UDP vs ICMP)

Hourly traffic patterns (line chart: packets per hour)

Filters:
Filter by port 22 (SSH) to analyze brute force attempts

Filter by protocol ICMP to visualize flood patterns

Filter by unique destination ports to identify port scans

🎯 How to prepare the demo (12-minute presentation)
Timeline structure:
Time	Content
0:00–1:30	Context: Problem (network saturation), data source (tcpdump)
1:30–4:00	Demo: Run txt_to_csv.py, show Network_Analysis.csv structure
4:00–7:00	Analysis: Run csv_to_md.py, open Network_Report.md, highlight alerts
7:00–9:00	Visualization: Convert to HTML, show styled report and recommendations
9:00–11:00	Technical details: Explain thresholds (66 SSH, 135 ports, 84 ICMP), detection logic
11:00–12:00	Conclusion: Results summary, limitations, future improvements
Key points to demonstrate:
Identified threats:

SSH brute force: 66 packets from 192.168.190.130

Port scanning: 135 ports probed

ICMP flood: 84 packets detected

Excel analysis:

Show pivot table with top IPs

Display chart of protocol distribution

Demonstrate filtering capabilities

Competencies demonstrated:

AC03.11: Python + Git usage

AC03.12: Code modification and debugging

AC03.13: Algorithm implementation (threshold detection)

AC03.14: Web technologies (MD → HTML)

AC03.15: Data structures (CSV, dictionaries)

AC03.16: GitHub collaboration

Prepare 3–4 slides:
SAE context + problematic (network saturation)

Pipeline diagram (Dump → CSV → MD → HTML)

Screenshot of Network_Report.html with alerts highlighted

Results summary + competencies demonstrated

⚠️ Troubleshooting
Problem	Solution
FileNotFoundError: DumpFileB2.txt	Ensure file exists in project root
Empty CSV output	Confirm dump contains lines with IP keyword
Encoding errors	Files are written in UTF-8, verify text editor encoding
Markdown not converting	Check Network_Report.md exists before running md_to_html.py
Wrong CSV delimiter in Excel	Select semicolon (;) as delimiter during import
🧪 Testing & fixtures
Recommended test structure:
text
/fixtures/
  DumpFileB2_sample.txt       # Small sample dump (10-20 lines)
  Network_Analysis_sample.csv # Expected CSV output
  Network_Report_sample.md    # Expected Markdown output

/tests/
  test_txt_to_csv.py          # Unit tests for parsing functions
  test_csv_to_md.py           # Unit tests for detection algorithms
  test_integration.py         # Full pipeline test on sample data
Running tests:
bash
python -m unittest discover tests/
🤝 Contributing
Fork the repository

Create a feature branch: git checkout -b feature/new-detection

Commit small, focused changes with clear messages

Submit a pull request with detailed description

Future improvements:
🔹 CLI arguments (--input, --output) for flexibility

🔹 JSON export for SIEM integration

🔹 Machine learning anomaly detection

🔹 Real-time monitoring mode for live tcpdump feeds

🔹 Web dashboard with interactive visualizations

🔹 Configurable thresholds (SSH attempts, port scan count, ICMP limit)

📜 License & contact
License: MIT (or specify if required by instructor)

Author: Khadim Diagne

Contact: kdiagne799@gmail.com

GitHub: kdiagne0799/Sae1.05_Network_Report

🙏 Acknowledgments
IUT de Roanne - BUT Réseaux & Télécommunications

SAE 1.05 teaching team for providing the project framework

tcpdump maintainers for the network capture tool

Python community for excellent standard library documentation

Made with 💻 for SAE 1.05 - BUT R&T S1 - IUT de Roanne
