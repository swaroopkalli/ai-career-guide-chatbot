## 📌 Overview

The **AI Career Guide** is an interactive chatbot that helps students explore:

* Career paths after **10th or 12th grade**
* Subject guidance (Science, Commerce, Arts, Vocational)
* Future scope of careers with **AI integration**
* Skill recommendations, courses, and real-world applications

Built with:

| Technology            | Purpose                              |
| --------------------- | ------------------------------------ |
| **Python**            | Core logic                           |
| **Streamlit**         | UI and chat interface                |
| **Google Gemini API** | Natural language response generation |
| **dotenv**            | Secure API key handling              |

---

## 🚀 Features

* 💬 Real-time conversational response streaming
* 🎓 Career recommendations tailored to students
* 🔍 Uses Gemini + Google Search tool for factual responses
* 🔐 Secure `.env` based API key management
* 🧠 Custom system persona for consistency in tone and expertise

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the repository

```sh
git clone https://github.com/swaroopkalli/ai-career-guide-chatbot.git
cd ai-career-guide-chatbot
```

### 2️⃣ Create a virtual environment (recommended)

```sh
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```sh
pip install -r requirements.txt
```

---

## 🔑 API Key Setup

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_api_key_here
```

Get your Gemini API key here:
👉 [https://ai.google.dev](https://ai.google.dev)

---

## ▶️ Run the App

```sh
streamlit run app.py
```

> Replace **`app.py`** if your main script has a different filename.

---

## 📂 Project Structure

```
📁 ai-career-guide-chatbot
 ├─ app.py
 ├─ .env  (not uploaded)
 ├─ requirements.txt
 ├─ README.md
 ├─ LICENSE
 └─ .gitignore
```

---

## 🧠 How It Works

The chatbot uses:

* `client.models.generate_content_stream()` for streaming replies
* Saved chat history via `st.session_state`
* A predefined system persona to ensure consistent advice tone and structure

---

## 🛣️ Future Enhancements (Planned)

* 📱 Mobile-friendly UI redesign
* 🎤 Speech input + voice output
* 🧬 Student profile personalization
* 📚 Course recommendations and skill roadmap generation

---

## 🤝 Contributing

Pull requests are welcome! If you'd like to add features or fix issues:

```sh
git checkout -b feature-name
```

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

---

## ⭐ Support

If you find this useful, please consider:

* ⭐ Starring the repository
* 🧑‍🎓 Sharing it with students or educators

---
