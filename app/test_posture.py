import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from modules.posture_analyzer import load_config, analyze_posture

config = load_config("data/config.json")
response = analyze_posture(config)

print("\n===== SECURITY POSTURE ANALYSIS =====\n")
print(response)