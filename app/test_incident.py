import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modules.alert_parser import load_alerts
from modules.incident_commander import analyze_incident

# load alerts
alerts = load_alerts("data/alerts.json")

# send to AI
response = analyze_incident(alerts)

print("\n===== AI INCIDENT ANALYSIS =====\n")
print(response)