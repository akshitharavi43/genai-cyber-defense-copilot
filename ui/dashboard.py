import sys
import os
import re


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st

from modules.posture_analyzer import load_config, analyze_posture
from modules.malware_explainer import explain_malware
from modules.alert_parser import load_alerts
from modules.incident_commander import analyze_incident
from modules.reasoning_engine import generate_attack_story
from modules.risk_engine import calculate_risk_score

def clean_ai_text(text):
    if not text:
        return ""

    # Remove markdown bold/italic markers
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"\*(.*?)\*", r"\1", text)
    text = re.sub(r"__(.*?)__", r"\1", text)
    text = re.sub(r"_(.*?)_", r"\1", text)

    # Remove markdown headings like ## Title
    text = re.sub(r"^\s*#{1,6}\s*", "", text, flags=re.MULTILINE)

    # Remove stray backticks
    text = text.replace("```", "").replace("`", "")

    # Convert bullet markers like "* item" to "- item"
    text = re.sub(r"^\s*\*\s+", "- ", text, flags=re.MULTILINE)

    # Remove lines that are only leftover markdown symbols
    text = re.sub(r"^\s*[\*\-_]{2,}\s*$", "", text, flags=re.MULTILINE)

    # Clean extra blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


st.set_page_config(page_title="GenAI Cyber Defense Copilot", layout="wide")

st.title("🛡️ GenAI Cyber Defense Copilot")
st.subheader("AI Security Operations Commander")

st.markdown("This dashboard combines posture analysis, malware explanation, incident response, and unified AI reasoning.")

st.sidebar.header("Controls")
run_analysis = st.sidebar.button("Run Full Analysis")

st.sidebar.markdown("---")
st.sidebar.write("Input files used:")
st.sidebar.code("data/config.json")
st.sidebar.code("data/malware_logs.txt")
st.sidebar.code("data/alerts.json")


def load_text_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


if run_analysis:
    with st.spinner("Running AI security analysis..."):

        # Posture Analysis
        config = load_config("data/config.json")
        posture_output = clean_ai_text(analyze_posture(config))

        # Malware Analysis
        malware_logs = load_text_file("data/malware_logs.txt")
        malware_output = clean_ai_text(explain_malware(malware_logs))

        # Incident Analysis
        alerts = load_alerts("data/alerts.json")
        incident_output = clean_ai_text(analyze_incident(alerts))

        # Unified Reasoning
        reasoning_output = clean_ai_text(generate_attack_story(
            posture_output,
            malware_output,
            incident_output
        ))

        # Risk Score
        risk_score, severity = calculate_risk_score(
            posture_output,
            malware_output,
            incident_output
        )

    st.success("Analysis completed successfully.")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Overall Risk Score", f"{risk_score}/100")
    with col2:
        st.metric("Severity", severity)

    st.markdown("---")

    tab1, tab2, tab3, tab4 = st.tabs([
        "Security Posture",
        "Malware Analysis",
        "Incident Analysis",
        "Unified Reasoning"
    ])

    with tab1:
        st.subheader("Security Posture Findings")
        st.text_area("Posture Output", clean_ai_text(posture_output), height=350)

    with tab2:
        st.subheader("Malware Behavior Analysis")
        st.text_area("Malware Output", clean_ai_text(malware_output), height=350)

    with tab3:
        st.subheader("Incident Commander Output")
        st.text_area("Incident Output", clean_ai_text(incident_output), height=350)

    with tab4:
        st.subheader("Unified AI Reasoning")
        st.text_area("Reasoning Output", clean_ai_text(reasoning_output), height=350)

else:
    st.info("Click 'Run Full Analysis' from the sidebar to start.")