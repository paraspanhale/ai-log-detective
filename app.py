import streamlit as st
import ollama

st.set_page_config(page_title="AI Log Detective", layout="wide")
st.title("🔍 AI Log Detective: Multi-File Edition")

# Initialize session state for reports
if 'reports' not in st.session_state:
    st.session_state.reports = []

uploaded_files = st.file_uploader("Upload your log files", type=['txt', 'log'], accept_multiple_files=True)

# Layout: Buttons side-by-side
col1, col2 = st.columns([1, 5])

with col1:
    analyze_btn = st.button("Analyze All Files")
with col2:
    clear_btn = st.button("Clear Results")

# Clear logic
if clear_btn:
    st.session_state.reports = []
    st.rerun()

# Analysis logic
if analyze_btn and uploaded_files:
    st.session_state.reports = [] 
    
    for file in uploaded_files:
        content = file.read().decode("utf-8")
        
        with st.spinner(f"Detecting errors in {file.name}..."):
            response = ollama.chat(model='llama3.2', messages=[
                {'role': 'user', 'content': f"Analyze these logs and list errors with fixes: {content[:2000]}"}
            ])
            report_text = response['message']['content']
            
            st.subheader(f"Report for: {file.name}")
            st.markdown(report_text)
            st.session_state.reports.append(f"--- Report for {file.name} ---\n{report_text}\n\n")

# Display previously analyzed reports (if they exist)
elif st.session_state.reports:
    for report in st.session_state.reports:
        st.markdown(report)

# Optional Download Button
if st.session_state.reports:
    st.divider()
    full_report = "".join(st.session_state.reports)
    st.download_button(
        label="📥 Download Summary as .txt",
        data=full_report,
        file_name="summary.txt",
        mime="text/plain"
    )