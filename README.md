# 🔍 AI Log Detective

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/streamlit-UI-red.svg)](https://streamlit.io/)
[![Ollama](https://img.shields.io/badge/AI-Ollama-green.svg)](https://ollama.com/)

**AI Log Detective** is a privacy-first, local diagnostic tool designed to parse system logs using the power of Llama 3.2. Because it runs locally via Ollama, your sensitive system data never leaves your machine.



---

## 🚀 Key Features
* **Multi-File Processing:** Analyze batches of `.log` or `.txt` files in one go.
* **100% Private:** No cloud APIs. Your logs stay on your local disk.
* **Actionable Intelligence:** The AI suggests specific fixes for identified issues.
* **Exportable Reports:** Download your session results as a clean, formatted `summary.txt`.
* **User-Friendly UI:** Simple controls to analyze, clear, and export data.

---

🌐 Accessing the App
Option 1: Use the Live Cloud Version (Recommended)

You can use the tool immediately without installing anything:
👉 Launch AI Log Detective : 

## 🛠 Prerequisites
Ensure you have the following installed on your system:
1. **[Ollama](https://ollama.com):** Required to run the local LLM.
2. **Python 3.10+:** Ensure you have Python installed.

### Configure the AI Model
Run these commands to prepare your local engine:

# Download the model
```bash
ollama pull llama3.2
```

# Start the Ollama background service
```bash
ollama serve
```

📦 Getting Started
1. Clone the repository
```bash
git clone [https://github.com/YOUR_USERNAME/ai-log-detective.git](https://github.com/YOUR_USERNAME/ai-log-detective.git)
cd ai-log-detective
```

2. Set up the virtual environment

# Create and activate the environment
```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

5. Launch the application
```bash
python -m streamlit run app.py
```

The browser will automatically open to http://localhost:8501.


💡 How to Use

   Upload: Drag and drop your log files into the uploader.

   Analyze: Click the Analyze All Files button.

   Review: Inspect the generated findings for each file.

   Download: Optionally click Download Summary to save the report.

   Clear: Click Clear Results to reset the UI for your next batch.
