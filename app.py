import streamlit as st
from openai import OpenAI

# 1. Page Configuration
st.set_page_config(page_title="AI Log Detective", layout="wide")
st.title("🔍 AI Log Detective")

# 2. Setup Client
try:
    client = OpenAI(
        api_key=st.secrets["GROQ_API_KEY"], 
        base_url="https://api.groq.com/openai/v1"
    )
except Exception as e:
    st.error("API Key not found. Please check your Streamlit Secrets.")
    st.stop()

# 3. Initialize session state
if 'reports' not in st.session_state:
    st.session_state.reports = []

# 4. Input Section (Files + Text Area)
st.write("### Provide your logs")
uploaded_files = st.file_uploader("Upload log files", type=['txt', 'log'], accept_multiple_files=True)
pasted_logs = st.text_area("OR paste log content here:", height=200, placeholder="Paste your log data here...")

# 5. Buttons
col1, col2 = st.columns([1, 5])
with col1:
    analyze_btn = st.button("Analyze Logs")
with col2:
    clear_btn = st.button("Clear Results")

# 6. Clear logic
if clear_btn:
    st.session_state.reports = []
    st.rerun()

# 7. Analysis logic
if analyze_btn:
    # Validate input
    if not uploaded_files and not pasted_logs:
        st.warning("Please upload a file or paste text to analyze.")
    else:
        st.session_state.reports = []
        
        # Process files
        if uploaded_files:
            for file in uploaded_files:
                content = file.read().decode("utf-8")
                process_log(content, f"File: {file.name}")

        # Process pasted text
        if pasted_logs:
            process_log(pasted_logs, "Pasted Content")

# Helper function to process logs
def process_log(content, source_name):
    with st.spinner(f"Analyzing {source_name}..."):
        try:
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {'role': 'system', 'content': 'You are an expert log analyzer. List errors and suggest fixes.'},
                    {'role': 'user', 'content': f"Analyze these logs: {content[:2000]}"}
                ]
            )
            report_text = response.choices[0].message.content
            st.subheader(f"Report for: {source_name}")
            st.markdown(report_text)
            st.session_state.reports.append(f"--- Report for {source_name} ---\n{report_text}\n\n")
        except Exception as e:
            st.error(f"Error analyzing {source_name}: {e}")

# 8. Display results
if st.session_state.reports:
    st.divider()
    full_report = "".join(st.session_state.reports)
    st.download_button("📥 Download Summary", data=full_report, file_name="summary.txt", mime="text/plain")
