import subprocess

def analyze_incident(alerts):
    prompt = f"""
You are a SOC Incident Commander.

Analyze these alerts:
{alerts}

Provide:
- Incident Type
- Timeline
- Risk Score
- Recommended Actions

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
