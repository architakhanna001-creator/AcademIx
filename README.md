# ✦ AcademIx

> An AI-powered study companion that transforms PDF notes into structured learning material using Google's Gemini AI.

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![Gemini](https://img.shields.io/badge/Google-Gemini%20AI-4285F4?logo=google)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?logo=bootstrap)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 Overview

AcademIx is an AI-powered study companion designed to simplify exam preparation.

Instead of manually creating notes, flashcards, and quizzes, users simply upload their study material in PDF format. AcademIx uses Google's Gemini AI to analyze the content and automatically generate structured learning resources within seconds.

The project combines Artificial Intelligence with an intuitive user interface to make studying faster, smarter, and more interactive.

---

## ✨ Features

- 📄 Upload PDF study notes
- 🤖 AI-generated detailed summary
- 🧠 Interactive flashcards
- ❓ Auto-generated MCQ quiz
- 💬 AI chatbot for asking questions about uploaded notes
- 🌙 Light & Dark mode
- 📑 Professional PDF export
- 🎉 Animated loading screen & confetti effects
- 📱 Responsive modern UI

---

## 🛠 Tech Stack

### Backend
- Python
- Flask
- Google Gemini API
- ReportLab

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap 5

### AI
- Gemini 2.5 Flash

---

## 📂 Project Structure

```
AcademIx/
│
├── static/
│   ├── css/
│   ├── js/
│
├── templates/
│   ├── components/
│   ├── base.html
│   ├── index.html
│   └── result.html
│
├── utils/
│   ├── ai.py
│   ├── chatbot.py
│   ├── pdf_export.py
│   ├── quiz.py
│   └── study_generator.py
│
├── uploads/
├── .env
├── main.py
└── requirements.txt
```

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/architakhanna001-creator/AcademIx.git
```

Move into the project directory.

```bash
cd AcademIx
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Create a `.env` file.

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application.

```bash
python main.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📸 Screenshots

> Add screenshots here after uploading them.

### Home Page

<img src="screenshots/home.png" width="900">

### AI Summary

<img src="screenshots/summary.png" width="900">

### Flashcards

<img src="screenshots/flashcards.png" width="900">

### Quiz

<img src="screenshots/quiz.png" width="900">

### Dark Mode

<img src="screenshots/darkmode.png" width="900">

---

## 🎯 Future Improvements

- Voice-based learning assistant
- OCR support for scanned PDFs
- Multi-language support
- User authentication
- Study progress tracking
- Cloud deployment
- AI-generated mind maps

---

## 👩‍💻 Author

**Archita Khanna**

- GitHub: https://github.com/architakhanna001-creator
- LinkedIn: *(Add your LinkedIn profile here)*

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.