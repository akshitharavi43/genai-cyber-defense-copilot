def calculate_risk_score(posture_text, malware_text, incident_text):
    score = 0

    high_risk_keywords = [
        "admin",
        "public access",
        "0.0.0.0/0",
        "credential dumping",
        "persistence",
        "lateral movement",
        "privilege escalation",
        "command-and-control",
        "high (9/10)",
        "high"
    ]

    combined_text = f"{posture_text} {malware_text} {incident_text}".lower()

    for keyword in high_risk_keywords:
        if keyword in combined_text:
            score += 10

    if score > 100:
        score = 100

    if score >= 80:
        severity = "Critical"
    elif score >= 60:
        severity = "High"
    elif score >= 40:
        severity = "Medium"
    else:
        severity = "Low"

    return score, severity