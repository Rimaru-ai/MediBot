import streamlit as st
from agents.summarizer import summarize_report
from agents.reminders import extract_medications, create_reminders

st.set_page_config(page_title="MediBot Assistant", page_icon="🩺", layout="wide")

st.title("🩺 MediBot – Healthcare Assistant")
st.write("An agentic assistant for **medical task automation** (summarization + reminders).")

# --- Tabs for agents ---
tab1, tab2 = st.tabs(["📄 Report Summarizer", "💊 Medication Reminders"])

# --- Tab 1: Summarization ---
with tab1:
    st.subheader("Summarize a Medical Report")
    report_text = st.text_area("Paste your medical report here:", height=200)

    if st.button("Summarize Report"):
        if report_text.strip():
            summary = summarize_report(report_text)
            st.success("✅ Summary Generated:")
            st.write(summary)
        else:
            st.warning("Please enter some report text.")

# --- Tab 2: Medication Reminders ---
with tab2:
    st.subheader("Generate Medication Reminders")
    prescription_text = st.text_area("Paste prescription details here:", height=150)

    days = st.slider("Number of days to generate reminders:", 1, 7, 3)
    hour = st.number_input("Reminder time (hour in 24hr format):", min_value=0, max_value=23, value=9)

    if st.button("Generate Reminders"):
        if prescription_text.strip():
            meds = extract_medications(prescription_text)
            if meds:
                st.info(f"💊 Extracted Medications: {', '.join(meds)}")
                reminders = create_reminders(meds, days, hour)
                st.success("✅ Reminders:")
                for r in reminders:
                    st.write(f"- {r}")
            else:
                st.warning("No medications detected in the text.")
        else:
            st.warning("Please enter a prescription.")
