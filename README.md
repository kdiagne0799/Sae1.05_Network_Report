# 🛡️ SAE1.05 Network Traffic Analysis Tool

# 🛡️ NetTrace Investigator

![Python](https://img.shields.io/badge/Language-Python_3.x-blue?style=for-the-badge&logo=python)  
![Status](https://img.shields.io/badge/Status-Stable-success?style=for-the-badge)  
![Domain](https://img.shields.io/badge/Domain-Network_Threat_Analysis-red?style=for-the-badge) 

---

## 📋 Educational Context

This project was completed as part of **SAE 1.05 - Data Processing** (Networks & Telecommunications Bachelor - Semester 1) at IUT Roanne.

### Problem Statement

A company's network (site in India) is saturated. Traditional checks (Wireshark, network tests, configurations) found nothing. We need to analyze a `tcpdump` file to identify suspicious activities causing the saturation.

### 🎯 Target Skills (RT3)

**Skill RT3**: Create IT tools and applications for Networks & Telecommunications

**Critical Learning Outcomes:**
- **AC03.11**: Use a computer system and its tools (Python, Git, tcpdump)
- **AC03.12**: Read, execute, correct, and modify a program
- **AC03.13**: Translate an algorithm into a language for a specific environment
- **AC03.14**: Know web technologies architecture (Markdown → HTML)
- **AC03.15**: Choose appropriate data management mechanisms (CSV, dictionaries, lists)
- **AC03.16**: Work in a collaborative development environment (GitHub)

### 📦 Expected Deliverables

- ✅ Python code hosted on GitHub
- ✅ User manual in English (this README)
- ✅ 12-minute oral presentation with demo
- ✅ Excel processing of CSV file
- ✅ Portfolio with supporting documents

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
⚙️ How It Works
Extraction_TXT_A_CSV Explained The first script opens a window on your screen. You click a button, choose your tcpdump text file, and it extracts all the important information:

When each packet was sent (timestamp)
What protocol was used (IP, TCP, etc.)
Where it came from (source IP and port)
Where it was going (destination IP and port)
Special flags (like SYN, ACK)
Packet sizes and sequence numbers Then it saves everything into a CSV file with columns separated by semicolons. Super simple.

## 📖 Project overview

**NetTrace Investigator** is a compact Python toolchain that converts raw `tcpdump` output into an actionable network security report (CSV → Markdown → HTML).

**Goal:** Transform hard-to-read packet dumps into clear, structured outputs highlighting:
- SSH brute force attacks
- Port scanning activity
- ICMP floods (DoS)
- Top bandwidth consumers

This project was developed to investigate network saturation issues when traditional methods failed, by processing `tcpdump` logs through automated Python analysis.

---

## 📋 Prerequisites

### Required Python Version

- **Python 3.8 or higher**

### Required Libraries

All required modules are included in the Python standard library:

```python
os              # File operations
csv             # CSV file handling
re              # Regular expressions
collections     # Data structures (Counter, defaultdict)
datetime        # Timestamp handling
```

No external packages needed.

**Optional software:** Microsoft Excel (for manual data analysis and pivot tables)

---

## 🎯 What this project does

This tool helps you find out why a network is having problems. It reads network traffic files (tcpdump format) and detects suspicious activities such as SSH brute force attacks, port scans, and ICMP floods.

This project was developed for a university assignment at IUT Roanne: two company sites (France and India) experienced network issues and needed deeper traffic analysis than standard tools provided.

---

## 📦 What's inside

### Scripts and purpose

| Script | Purpose |
|---|---|
| `txt_to_csv.py` | Converts raw tcpdump text file → clean CSV (semicolon-separated) |
| `csv_to_md.py` | Analyzes CSV → generates Markdown report with security alerts |
| `md_to_html.py` | Converts Markdown report → styled HTML page for presentation |

### Files generated

- `Network_Analysis.csv` — Structured data (semicolon-separated)
- `Network_Report.md` — Security analysis report (Markdown)
- `Network_Report.html` — Final styled report (HTML with embedded CSS)

---

## ⚙️ How it works

### txt_to_csv.py — parsing raw tcpdump

The script extracts:

- Timestamp — when each packet was captured
- Protocol — TCP, UDP, ICMP, etc.
- Source IP & Port
- Destination IP & Port
- TCP Flags — SYN, ACK, FIN, RST, etc.
- Packet Length


### csv_to_md.py — detection and reporting

This script applies simple heuristic thresholds to flag potentially suspicious patterns in the traffic.

#### Detection thresholds

| Attack type       | Description                                      | Threshold                          |
|-------------------|--------------------------------------------------|------------------------------------|
| SSH brute force   | Numerous SSH attempts (port 22) from a single IP | > 50 SSH packets within 5 minutes  |
| Port scanning     | One IP contacts many different destination ports | > 20 distinct destination ports    |
| ICMP flood (DoS)  | Excessive ICMP packets from a single IP          | > 50 ICMP packets                  |

#### Example findings (from DumpFile.txt analysis)

- 🔴 Critical: Targeted SSH attack — Source `192.168.190.130` (66 SSH packets to port 22)  
  - Severity: HIGH  
  - Recommendation: block this IP and enable fail2ban or similar protection  

- 🟠 Port scanning — 135 destination ports probed  
  - Severity: MEDIUM  
  - Recommendation: investigate the source host and check for compromise  

- 🟡 ICMP flood — 84 ICMP packets detected  
  - Severity: MEDIUM  
  - Recommendation: apply ICMP rate limiting or filtering on edge devices  

The script generates `Network_Report.md`, which includes:

- An executive summary of the capture
- Lists of suspicious IPs with associated severity levels
- Top 30 most active IPs and protocol usage statistics
- Actionable recommendations for the network/security team



### md_to_html.py — presentation

Converts `Network_Report.md` to a standalone `Network_Report.html` with:

- Embedded CSS (Bootstrap-inspired styles)
- Color-coded alerts (red/orange/green)
- Tables and sections ready for presentation or emailing

---

## 📊 What you get

### 1) `Network_Analysis.csv`

This script generates a CSV table with the following columns:

```
Timestamp;Source_IP;Source_Port;Dest_IP;Dest_Port;Protocol;Flags;Length;Packet_Info
```
<img width="2187" height="1602" alt="image" src="https://github.com/user-attachments/assets/2efffe00-d650-4f07-9cd9-3db5fb3f64db" />

It writes a CSV with semicolon separators so it can be easily opened in Excel.
<img width="1996" height="1536" alt="image" src="https://github.com/user-attachments/assets/4901a5a5-6815-4eb5-a63e-39bc57123ca7" />
<img width="400" height="215" alt="image" src="https://github.com/user-attachments/assets/4582ef44-cb99-4e59-a5ed-65875e8edd82" />

<img width="1754" height="318" alt="image" src="https://github.com/user-attachments/assets/54c8cb34-044b-4ac1-a089-da899fcc594c" />



**Example input (excerpt from DumpFile.txt):**

<img width="1740" height="1072" alt="image" src="https://github.com/user-attachments/assets/4facc056-130e-41d0-a644-9481d3772b70" />

After analyzing, it creates a folder called `resultats_interface/` with:
- A Markdown report with all the statistics
- 3 PNG images showing graphs and charts
- Clear lists of any problems it found

## 📊 What You Get

When you run both scripts, here's what gets created:
CSV File - All your network packets in a neat table format
Markdown Report - A text document with:
- How many packets were analyzed
- Total data volume
- Top 10 most active IP addresses
- What protocols were used
- Any suspicious activity found
**Example output (CSV row):**

<img width="2788" height="1148" alt="image" src="https://github.com/user-attachments/assets/9f3ce5dd-69ba-4783-90d6-4bd03abcb5df" />


## 🖼️ Visualization outputs

| Image file            | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| **anomalies.png**     | Summary of all detected anomalies, organized by severity level.            |
<img width="706" height="607" alt="image" src="https://github.com/user-attachments/assets/7cee89f6-f6bd-40f4-a487-693502770744" />

| **analyse_trafic.png** | Four graphs illustrating traffic trends, attack peaks, most active IP addresses, and data volumes. |
<img width="516" height="613" alt="image" src="https://github.com/user-attachments/assets/2172afcb-1c31-44b2-bd06-05336bb651d2" />

| **protocoles.png**    | Pie chart showing the distribution of the different network protocols used. |
<img width="597" height="617" alt="image" src="https://github.com/user-attachments/assets/400be61b-8e3c-4938-b6dd-0f4c562e81bc" />


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


### 2) `Network_Report.md`

This file provides a detailed textual summary of the capture, including:

- Total number of packets analyzed (e.g., 11,016)
- Overall data volume statistics
- Top 30 most active IP addresses
- Protocol breakdown (TCP, UDP, ICMP)
- Security alerts (for example, 3 detected threats)

**Sample report preview:**

<img width="2190" height="1598" alt="image" src="https://github.com/user-attachments/assets/ea926a16-7cae-4b18-992e-aad6a141cfc4" />

### 3) `Network_Report.html`

This is a styled HTML version of the report, ideal for:

- Sharing by email
- Presenting during the oral defense
- Adding to a professional portfolio

<img width="2187" height="1480" alt="image" src="https://github.com/user-attachments/assets/183f741d-35d5-4de0-866f-542b26d038e1" />
<img width="2154" height="1321" alt="image" src="https://github.com/user-attachments/assets/14d2d0b1-01c8-4437-a46e-15ef8a27fad8" />


---

## 🚀 How to use

### Installation

No external packages required. Make sure Python 3.8+ is installed.

```bash
git clone https://github.com/kdiagne0799/Sae1.05_Network_Report.git
cd Sae1.05_Network_Report
```

### Step-by-step usage

1. Convert tcpdump file to CSV:

```bash
python txt_to_csv.py
```

Sample console output:

```
Démarrage de la conversion...
Lecture : DumpFile.txt
Lignes lues : 507,891
Paquets extraits : 11,016
Lignes ignorées : 496,875
Fichier créé : Network_Analysis.csv
```

1. Analyze the CSV and create markdown report:

```bash
python csv_to_md.py
```

Sample console output:

```
========== ANALYSE DEMARREE ==========

Lecture de Network_Analysis.csv...
11,016 paquets lus
Analyse en cours...
Détection des anomalies...

🚨 ALERTES DETECTEES :
  - SSH Brute Force : 192.168.190.130 (66 packets)
  - Port Scan : 135 ports probed
  - ICMP Flood : 84 packets

Rapport créé : Network_Report.md

========== ANALYSE TERMINEE ==========
```

1. Generate an HTML report:

```bash
python md_to_html.py
```

Sample console output:

```
Conversion Markdown → HTML...
Lecture : Network_Report.md
Génération HTML avec CSS...
Fichier créé : Network_Report.html

✅ Rapport HTML prêt pour présentation !
```

### Files created

```
Sae1.05_Network_Report/
├── DumpFile.txt            # Your original tcpdump file
├── Network_Analysis.csv      # Structured data (Excel-ready)
├── Network_Report.md         # 📄 Read this first! Main report
├── Network_Report.html       # 🌐 Professional styled version
├── txt_to_csv.py             # Script 1
├── csv_to_md.py              # Script 2
├── md_to_html.py             # Script 3
└── README.md                 # This file
```

---

## 🔍 Understanding the Results

### ✅ If No Problems Found
The report will say:
✅ No anomalies detected. Network traffic appears normal.

### 🚨 If Problems Found
You'll see alerts like:
- 🔴 SSH brute force: 66 packets...
- ⚠️ Port scanning: 135 ports...
- ⚠️ ICMP Flood: 84 packets detected. Potential DoS.
---

## 🧪 Testing & Quality Assurance

### Current Testing Approach
- Manual testing with sample `DumpFileB2.txt` (11,016 packets)
- Verification of detection thresholds against known attack patterns
- Output validation: CSV structure, Markdown formatting, HTML rendering

### Recommended Future Tests
- Unit tests for `parse_line()` and timestamp extraction functions
- Integration test running full pipeline against sample dump
- Fixtures folder with trimmed sample dumps for automated testing

---

## 🔧 Technical Details

### Code Structure

- **Modular design:** Each script performs one specific transformation
- **Standard library only:** No external dependencies for easy deployment and grading
- **Clear separation:** Data extraction → Analysis → Visualization
- **PEP8 compliant:** Clean, readable Python code with docstrings

### Project Architecture


Contribution guidelines:

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/name`
3. Add tests and documentation
4. Open a Pull Request with a clear description

---

## 💡 Why This Matters

Network issues can be very hard to spot, especially when you have thousands or even millions of packets to go through. These tools handle the repetitive work for you: they read all the data, detect patterns, and highlight anything unusual.

In our scenario, the Indian production site was experiencing network problems. With these tools, we can quickly understand whether it is:

#### 🔴 A security incident (for example, someone flooding or scanning the network)  
#### 🟠 A configuration issue (a single host sending an abnormal amount of traffic)  
#### 🟢 Legitimate traffic that simply requires more bandwidth  

## 👨‍🎓 About This Project

This project was developed for SAE 1.05 (Data Processing) during the first year of the BUT Networks and Telecommunications program at IUT Roanne. The objectives were to learn Python, practice network traffic analysis, and build practical tools that real IT teams could rely on.

The requirements specified that the tool should be usable by teams in India who work in English, so all outputs and explanations had to remain clear, simple, and easy to follow.

## 📊 Excel Analysis

### How to Use Excel

You can open the generated CSV file in Excel for manual exploration and custom analysis.

#### Import Steps

1. Open Excel → **Data** → **From Text/CSV**  
2. Select your CSV file  
   <img width="945" height="501" alt="image" src="https://github.com/user-attachments/assets/b3cdfabf-48b7-47f9-bb1b-a90b317f0aea" />
   <img width="1119" height="323" alt="image" src="https://github.com/user-attachments/assets/b7cef9e9-2884-4238-be87-fe090bf75b69" />

3. **Important:** Choose **semicolon (;)** as the delimiter  
4. Click **Load**  
   <img width="2787" height="1169" alt="image" src="https://github.com/user-attachments/assets/f4fa5444-48b0-485c-a7f8-8b524599a7e1" />

#### Enable VBA Macro (Optional)

- Press `Alt + F11` to open the VBA editor  
  <img width="945" height="362" alt="image" src="https://github.com/user-attachments/assets/e06309bd-4875-4770-a196-ac44b879ef30" />
  <img width="2379" height="1471" alt="image" src="https://github.com/user-attachments/assets/d99b2e89-23b0-4000-a1e5-085be528e4a7" />

- Press `Alt + F8` to run the analysis macro  
  <img width="945" height="502" alt="image" src="https://github.com/user-attachments/assets/0081424f-f569-4f9e-ae0e-1187298fd0f5" />
  <img width="1783" height="1059" alt="image" src="https://github.com/user-attachments/assets/df06c753-84e5-4186-860b-754db37ecf59" />

- Run the macro to automatically format and enhance the Excel report  
  <img width="2337" height="787" alt="image" src="https://github.com/user-attachments/assets/60d0390a-b372-4b3c-bb51-e2987974ce05" />



## 🔮 Future improvements

Potential enhancements for this project:

- 🔹 **CLI arguments:** Add `--input`, `--output` flags for flexible file paths and time range filters
- 🔹 **JSON export:** Export results for integration with SIEM tools (Splunk, ELK Stack)
- 🔹 **Machine learning:** Implement ML models for advanced anomaly detection
- 🔹 **Real-time monitoring:** Add live tcpdump feed analysis mode
- 🔹 **Web dashboard:** Create interactive visualization interface with charts and graphs
- 🔹 **Configurable thresholds:** Allow users to customize detection thresholds (SSH attempts, port scan count)

---


## 📜 License & Contact

**License:** MIT (recommended for educational projects)

**Author:** Khadim Diagne  
**Program:** BUT Réseaux & Télécommunications - Year 1  
**School:** IUT Roanne  
**Project:** SAE 1.05 - Data Processing

**Contact:** <kdiagne799@gmail.com>  
**GitHub:** [@kdiagne0799](https://github.com/kdiagne0799)


