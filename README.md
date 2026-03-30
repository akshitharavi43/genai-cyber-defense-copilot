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

Logs / Configs / Alerts
        │
        ▼
   Data Parsers
        │
        ▼
AI Modules
  • Posture Analyzer
  • Malware Explainer
  • Incident Commander
        │
        ▼
Unified Reasoning Engine
        │
        ▼
Streamlit SOC Dashboard


## Technologies Used

Python  
Streamlit  
Ollama + Llama3 (Local LLM)  
FAISS (Vector search)  
spaCy (NLP processing)


## Installation

Clone the repository:

git clone https://github.com/akshitharavi43/genai-cyber-defense-copilot.git
cd genai-cyber-defense-copilot

Create virtual environment:

python -m venv venv

Activate environment:

Windows
venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt


## Running the Dashboard

Start the Streamlit dashboard:

streamlit run ui/dashboard.py
Then open:
http://localhost:8501



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


## Use Cases

SOC automation  
Threat analysis assistance  
Security posture auditing  
Incident response planning  
Cybersecurity research


## Future Improvements

Real-time SIEM ingestion  
Integration with Wazuh or Splunk  
Automatic MITRE ATT&CK mapping  
Threat intelligence enrichment  
Automated response playbooks


## Author

Akshitha Ravi  
Cybersecurity & AI Enthusiast