import json
import subprocess

def load_config(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def analyze_posture(config_data):
    prompt = f"""
You are a cloud security posture analyst.

Analyze the following security configuration and identify security weaknesses.

Configuration:
{json.dumps(config_data, indent=2)}

Return your answer in plain text using exactly this format:

Finding 1:
Risk:
Issue:
Impact:
Fix:

Finding 2:
Risk:
Issue:
Impact:
Fix:

Finding 3:
Risk:
Issue:
Impact:
Fix:

Keep the answer short, practical, and SOC-focused.

Return plain text only.
Do not use **bold**, *italic*, or markdown formatting.
Use simple bullet points with "-".
"""

    result = subprocess.run(
        ["ollama", "run", "llama3"],
        input=prompt,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    return result.stdout