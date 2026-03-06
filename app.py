import streamlit as st
from openai import OpenAI

# Google Search Console Verification
st.markdown("""
    <meta name="google-site-verification" content="YOUR_COPIED_VERIFICATION_CODE_HERE" />
""", unsafe_allow_html=True)

# 1. Page Configuration
st.set_page_config(page_title="AI Log Detective", layout="wide")
st.title("🔍 AI Log Detective")

# 2. Setup Client safely using Streamlit Secrets
# Make sure you have GROQ_API_KEY set in your Streamlit Cloud "Secrets"
try:
    client = OpenAI(
        api_key=st.secrets["GROQ_API_KEY"], 
        base_url="https://api.groq.com/openai/v1"
    )
except Exception as e:
    st.error("API Key not found. Please check your Streamlit Secrets configuration.")
    st.stop()

# 3. Initialize session state
if 'reports' not in st.session_state:
    st.session_state.reports = []

uploaded_files = st.file_uploader("Upload your log files", type=['txt', 'log'], accept_multiple_files=True)

# 4. Layout: Buttons
col1, col2 = st.columns([1, 5])
with col1:
    analyze_btn = st.button("Analyze All Files")
with col2:
    clear_btn = st.button("Clear Results")

# 5. Clear logic
if clear_btn:
    st.session_state.reports = []
    st.rerun()

# 6. Analysis logic
if analyze_btn and uploaded_files:
    st.session_state.reports = [] 
    
    for file in uploaded_files:
        content = file.read().decode("utf-8")
        
        with st.spinner(f"Detecting errors in {file.name}..."):
            try:
                # Updated to use the Groq client
                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {'role': 'system', 'content': 'You are an expert log analyzer. List errors and suggest fixes.'},
                        {'role': 'user', 'content': f"Analyze these logs: {content[:2000]}"}
                    ]
                )
                report_text = response.choices[0].message.content
                
                st.subheader(f"Report for: {file.name}")
                st.markdown(report_text)
                st.session_state.reports.append(f"--- Report for {file.name} ---\n{report_text}\n\n")
            except Exception as e:
                st.error(f"Error analyzing {file.name}: {e}")

# 7. Display results and Download
elif st.session_state.reports:
    for report in st.session_state.reports:
        st.markdown(report)

if st.session_state.reports:
    st.divider()
    full_report = "".join(st.session_state.reports)
    st.download_button(
        label="📥 Download Summary as .txt",
        data=full_report,
        file_name="summary.txt",
        mime="text/plain"
    )
