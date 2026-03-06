# 🔍 AI Log Detective

A local-first diagnostic tool that uses Ollama and Llama 3.2 to analyze system log files, identify errors, and suggest fixes. Built with Python and Streamlit.

## 🚀 Features
* **Multi-File Support:** Upload and analyze multiple log files simultaneously.
* **Local-First AI:** Privacy-focused analysis using your local Ollama engine—no data leaves your machine.
* **Downloadable Reports:** Optionally export analysis summaries to a text file.
* **Clean UI:** Batch analysis with built-in "Clear" functionality for a streamlined workflow.

## 🛠 Prerequisites
You need [Ollama](https://ollama.com) installed and running on your system.
1. Download and install Ollama.
2. Pull the model: `ollama pull llama3.2`
3. Ensure the service is running: `ollama serve` (or `systemctl start ollama`)

## 📦 How to Run

1. **Clone the repository:**
   ```bash
   git clone <your-repo-link>
   cd my-ai-analyzer
