# GenAI Cyber Defense Copilot

AI-powered Security Operations Platform that combines security posture analysis, malware behavior explanation, incident response planning, and unified threat reasoning.

This project demonstrates how Generative AI can assist SOC teams in detecting, understanding, and responding to cyber threats.


## Key Features

Security Posture Analyzer  
Identifies misconfigurations in IAM policies, firewall rules, and storage settings.

Malware Behavior Explainer  
Analyzes system behavior logs and explains attacker actions using MITRE ATT&CK mapping.

GenAI Incident Commander  
Processes SIEM alerts and produces incident timelines, risk scores, and response recommendations.

Unified AI Reasoning Engine  
Correlates posture weaknesses, malware activity, and alerts to determine the root cause of attacks.

SOC Dashboard  
Interactive Streamlit dashboard to visualize analysis results.


## Architecture

## System Architecture

```text
                 ┌──────────────────────┐
                 │   Security Inputs    │
                 │──────────────────────│
                 │ • System Configs     │
                 │ • Process Logs       │
                 │ • SIEM Alerts        │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │      Data Parsers    │
                 │──────────────────────│
                 │ Normalize & Extract  │
                 │ key fields from logs │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │      AI Modules      │
                 │──────────────────────│
                 │ • Posture Analyzer   │
                 │ • Malware Explainer  │
                 │ • Incident Commander │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │ Unified Reasoning AI │
                 │──────────────────────│
                 │ Correlates security  │
                 │ findings to identify │
                 │ attack root causes   │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │  Risk Scoring Engine │
                 │──────────────────────│
                 │ Calculates threat    │
                 │ severity & priority  │
                 └──────────┬───────────┘
                            │
                            ▼
                 ┌──────────────────────┐
                 │  Streamlit Dashboard │
                 │──────────────────────│
                 │ SOC visualization    │
                 │ investigation output │
                 └──────────────────────┘
```

## Technologies Used

Python  
Streamlit  
Ollama + Llama3 (Local LLM)  
FAISS (Vector search)  
spaCy (NLP processing)


## Installation

Clone the repository:

```bash
git clone https://github.com/akshitharavi43/genai-cyber-defense-copilot.git
cd genai-cyber-defense-copilot
```
Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

### Windows
```bash
venv\Scripts\activate
```
### macOS / Linux
```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Dashboard

Start the Streamlit dashboard:

```bash
streamlit run ui/dashboard.py
```
Open your browser and go to:

```
http://localhost:8501
```



## Example Workflow

1. Load system configuration data
2. Analyze posture weaknesses
3. Explain malware behavior
4. Investigate SIEM alerts
5. Generate unified attack reasoning
6. Display results in SOC dashboard


## Example Output

Risk Score: 90 / 100  
Severity: Critical  

Root Cause:  
Weak IAM permissions allowed credential dumping leading to lateral movement.

Recommended Response:
- Isolate infected hosts
- Reset compromised credentials
- Restrict exposed services
- Conduct forensic investigation


## Dashboard Preview

![dashboard](https://github.com/user-attachments/assets/8e639997-d6a1-485f-9a28-913ac3491051)


## Use Cases

SOC automation  
Threat analysis assistance  
Security posture auditing  
Incident response planning  
Cybersecurity research


## Security Concepts Demonstrated

Security posture assessment
Malware behavior analysis
Incident response automation
Threat correlation and attack chain reconstruction
Risk scoring and prioritization
MITRE ATT&CK mapping


## Future Improvements

Real-time SIEM ingestion  
Integration with Wazuh or Splunk  
Automatic MITRE ATT&CK mapping  
Threat intelligence enrichment  
Automated response playbooks


## Author

Akshitha Ravi  
Cybersecurity & AI Enthusiast
```bash
https://github.com/akshitharavi43
```
