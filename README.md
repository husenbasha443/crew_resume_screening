

```markdown
# 🧠 CrewAI Resume Screening System

An AI-powered **Resume Screening & Knowledge Processing System** built using **CrewAI**, **LiteLLM**, and YAML-based agent/task configuration.  
This project follows a **clean `src/` layout**, supports blogs & knowledge ingestion, and is easily extendable for real-world HR use cases.

---

## 📁 Project Structure

```

crewai_resume_screening/
│
├── .venv/                      
│
├── blogs/
│   └── blog.md                 
│
├── knowledge/                  
│
├── src/
│   └── crewai_resume_screening/
│       ├── **pycache**/
│       │
│       ├── config/
│       │   ├── agents.yaml    
│       │   └── tasks.yaml     
│       │
│       ├── tools/             
│       │
│       ├── **init**.py
│       ├── crew.py            
│       └── main.py             
│
├── tests/                     
│
├── .env                        
├── demo.ipynb                  
├── pyproject.toml              
├── requirements.txt            
├── uv.lock                     
└── README.md

````

---

## 🚀 Features

- Resume screening using CrewAI agents
- YAML-based agent & task configuration
- Modular and scalable project layout
- Knowledge folder ready for **RAG integration**
- Blog/content processing support
- LiteLLM multi-model compatibility
- Clean separation of logic, config, and tools

---

## 🛠️ Prerequisites

- **Python 3.10+**
- Virtual environment support
- LLM API key (OpenAI / Azure / Groq / etc.)

---

## ⚙️ Installation & Setup

### 1️⃣ Activate Virtual Environment

```powershell
.venv\Scripts\activate
````

---

### 2️⃣ Install Dependencies

```powershell
pip install -r requirements.txt
pip install "litellm[proxy]"
```

> ⚠️ `litellm[proxy]` is required to avoid FastAPI import errors.

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key
AZURE_OPENAI_KEY=your_azure_key
AZURE_OPENAI_ENDPOINT=your_azure_endpoint
```

---

## ▶️ Running the Project

### Option 1: Using CrewAI CLI (Recommended)

```bash
crewai run
```

---


## 👨‍💻 Author

**Husen Basha**



