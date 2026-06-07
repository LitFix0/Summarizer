# 🧠 AI Text Summarizer

A clean, minimal **AI-powered text summarization web app** built using Flask and OpenAI.
Paste any text and instantly get a structured summary with key insights.

---

## 🚀 Features

* ✨ Concise / Detailed / Bullet-style summaries
* 📌 Key points extraction
* 🏷️ Topic detection
* 😊 Sentiment analysis (positive / neutral / negative)
* ⏱️ Reading time + word count
* ⚡ Fast API response with latency tracking
* 🎨 Clean, modern UI (no frameworks)

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, CSS, Vanilla JS
* **AI Model:** OpenAI API
* **Environment:** dotenv

---

## 📂 Project Structure

```
summarizer-final/
│
├── backend/
│   └── app.py
│
├── frontend/
│   └── index.html
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/your-username/ai-summarizer.git
cd ai-summarizer
```

---

### 2. Create virtual environment

```
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate   # Mac/Linux
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Setup environment variables

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_api_key_here
```



---

### 5. Run the app

```
python backend/app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

---

## 🧪 API Endpoint

### POST `/summarize`

**Request:**

```json
{
  "text": "Your input text...",
  "model": "gpt-4o-mini",
  "style": "concise"
}
```

**Response:**

```json
{
  "success": true,
  "data": {
    "summary": "...",
    "key_points": ["...", "..."],
    "topics": ["..."],
    "sentiment": "neutral",
    "word_count": 120,
    "reading_time": "1 min read"
  },
  "model_used": "gpt-4o-mini",
  "elapsed_ms": 420
}
```

---

## 🔐 Security Notes

* API key is stored securely using `.env`
* `.env` is excluded via `.gitignore`
* Do NOT expose API keys in frontend or public repos

---



---

## 🚧 Future Improvements

* 🔄 Streaming responses
* 📄 File upload (PDF / DOCX support)
* 🌐 Deploy on cloud (Render / Vercel)
* 🧠 Multi-language summarization
* 📊 Advanced analytics dashboard

---

## 🙌 Acknowledgements

* OpenAI for powerful language models
* Flask for lightweight backend framework

---

## 📌 Author

**Shashank Rawat**


---

## ⭐ If you like this project

Give it a star on GitHub — it helps!
