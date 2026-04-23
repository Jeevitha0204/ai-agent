# 🤖 LangChain AI Agent with Groq & Gradio

## 📌 Project Overview
An interactive AI Agent built using **LangChain**, **Groq (LLaMA 3.3 70B)**, and **Gradio** that can perform multiple tasks using custom tools — from solving math problems to text manipulation — all through a clean chat interface.

---

## 🚀 Live Demo
> Run locally or deploy on Hugging Face Spaces

---

## 🛠️ Tools Available in the Agent

| Tool | Description |
|------|-------------|
| 🧮 **Calculator** | Solves any math expression (e.g. `25 * 4`) |
| 📝 **Word Counter** | Counts number of words in a text |
| 🔤 **Character Counter** | Counts number of characters in a text |
| 🔠 **Uppercase Tool** | Converts text to UPPERCASE |
| 🔡 **Lowercase Tool** | Converts text to lowercase |
| 🔁 **Reverse Text** | Reverses any given text |
| 💬 **General QA** | Answers general knowledge questions directly from LLM |

---

## 🧰 Tech Stack

| Technology | Purpose |
|------------|---------|
| **LangChain** | Agent framework & tool calling |
| **Groq API** | LLM backend (LLaMA 3.3 70B Versatile) |
| **Gradio** | Chat UI interface |
| **Python** | Core language |

---

## 📁 Project Structure
langchain-ai-agent/
├── app.py          # Main application file
├── requirements.txt
└── README.md

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/langchain-ai-agent.git
cd langchain-ai-agent
```

### 2. Install dependencies
```bash
pip install langchain langchain-groq gradio
```

### 3. Set your Groq API Key
```bash
export GROQ_API_KEY="your_groq_api_key_here"
```
> Get your free API key at: https://console.groq.com

### 4. Run the app
```bash
python app.py
```

### 5. Open in browser
http://localhost:7860

---

## 💬 Example Queries
🧮 "What is 125 * 48?"
📝 "Count words: I am learning AI and it is very interesting"
🔠 "Convert to uppercase: hello world"
🔁 "Reverse this text: artificial intelligence"
🔤 "Count characters: Hello World"
💬 "What is LangChain?"

---

## 🧠 How It Works
User Input
↓
LangChain Agent (LLaMA 3.3 70B via Groq)
↓
Decides: Use Tool OR Answer Directly
↓
Tool Executes → Result returned to LLM
↓
Final Response shown in Gradio Chat UI

---

## 📦 Requirements
langchain
langchain-groq
gradio

---

## 👤 Author
**Jeevitha M**
Data Science Enthusiast | AI & ML Developer

---

## ⭐ If you found this useful, give it a star!
