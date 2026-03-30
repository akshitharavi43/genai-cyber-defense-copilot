import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modules.reasoning_engine import load_text_file, generate_attack_story


posture = load_text_file("data/posture_output.txt")
malware = load_text_file("data/malware_output.txt")
incident = load_text_file("data/incident_output.txt")

response = generate_attack_story(posture, malware, incident)

print("\n===== UNIFIED AI REASONING =====\n")
print(response)