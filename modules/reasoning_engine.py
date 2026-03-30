import subprocess


def load_text_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def generate_attack_story(posture_text, malware_text, incident_text):
    prompt = f"""
You are an expert SOC analyst and incident response lead.

You are given 3 different security analysis outputs:

1. Security Posture Findings
2. Malware Behavior Analysis
3. Incident Alert Analysis

Your job is to correlate them and explain the full attack story.

Security Posture Findings:
{posture_text}

Malware Behavior Analysis:
{malware_text}

Incident Alert Analysis:
{incident_text}

Return your answer in plain text with exactly these sections:

Root Cause:
Attack Story:
Why Attack Succeeded:
Business Impact:
Priority Response Actions:

Keep the answer concise, logical, and security-focused.

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