# 🤖 FAQ Chatbot — AI & Technology Concepts

[![Contributors](https://img.shields.io/github/contributors/khushi-Jag/ApexcifyTechnologys_Rock-Paper-Scissors-with-AI-Opponent)](https://github.com/khushi-Jag/ApexcifyTechnologys_Rock-Paper-Scissors-with-AI-Opponent/graphs/contributors)
[![Forks](https://img.shields.io/github/forks/khushi-Jag/ApexcifyTechnologys_Rock-Paper-Scissors-with-AI-Opponent)](https://github.com/khushi-Jag/ApexcifyTechnologys_Rock-Paper-Scissors-with-AI-Opponent/network/members)
[![Stars](https://img.shields.io/github/stars/khushi-Jag/ApexcifyTechnologys_Rock-Paper-Scissors-with-AI-Opponent)](https://github.com/khushi-Jag/ApexcifyTechnologys_Rock-Paper-Scissors-with-AI-Opponent/stargazers)
[![Issues](https://img.shields.io/github/issues/khushi-Jag/ApexcifyTechnologys_Rock-Paper-Scissors-with-AI-Opponent)](https://github.com/khushi-Jag/ApexcifyTechnologys_Rock-Paper-Scissors-with-AI-Opponent/issues)
[![License](https://img.shields.io/github/license/khushi-Jag/ApexcifyTechnologys_Rock-Paper-Scissors-with-AI-Opponent)](https://github.com/khushi-Jag/ApexcifyTechnologys_Rock-Paper-Scissors-with-AI-Opponent/blob/main/LICENSE)


> A **professional interactive FAQ chatbot** built with Flask that provides intelligent answers to common questions about Artificial Intelligence, Machine Learning, and Web Development — using NLP techniques including Cosine Similarity and keyword overlap matching.

---

## 📌 Table of Contents

* [About The Project](#-about-the-project)
* [Key Features](#-key-features)
* [Built With](#-built-with)
* [How It Works](#-how-it-works)
* [Project Structure](#-project-structure)
* [Getting Started](#-getting-started)
* [Usage](#-usage)
* [Contributing](#-contributing)
* [License](#-license)
* [Contact](#-contact)

---

## 💡 About The Project

The **FAQ Chatbot** is an NLP-powered question-answering system that intelligently matches user queries to the most relevant answer from a curated knowledge base covering AI, ML, and Web Development concepts.

Unlike simple keyword matching systems, this chatbot uses a **hybrid scoring approach** — combining Cosine Similarity for semantic matching with keyword overlap for direct term matching — to deliver confident, accurate responses even when the user's phrasing doesn't exactly match the stored questions.

---

## ✨ Key Features

* **Intelligent Matching** – Hybrid scoring using Cosine Similarity (65%) and Keyword Overlap (35%).
* **NLP Preprocessing** – Stopword removal, synonym expansion (e.g. `"ML"` → `"Machine Learning"`), and text normalization.
* **Confidence Scoring** – Responses categorized as High, Medium, or Low confidence.
* **Dynamic Suggestions** – Helpful fallback suggestions when no confident match is found.
* **Modern Glassmorphism UI** – Clean, responsive interface built with vanilla CSS.

---

## 🛠 Built With

| Technology | Purpose |
|---|---|
| Python 3.8+ | Core language |
| Flask | Web framework & backend server |
| HTML5 / CSS3 | Frontend UI (Glassmorphism design) |
| JavaScript (ES6+) | Frontend interactivity |
| Math (Cosine Similarity) | Semantic similarity scoring |
| Re (Regex) | Text cleaning & normalization |

> No external NLP libraries required — pure Python standard library implementation.

---

## 🧠 How It Works

User input goes through a multi-stage NLP pipeline before being matched:

### Processing Pipeline

```
User Query
     │
     ▼
1. Normalization (lowercase + remove special chars)
     │
     ▼
2. Synonym Mapping ("ML" → "Machine Learning", "AI" → "Artificial Intelligence")
     │
     ▼
3. Vectorization (word frequency vectors)
     │
     ▼
4. Hybrid Scoring:
   ├── Cosine Similarity  (65% weight) — semantic similarity
   └── Keyword Overlap    (35% weight) — direct term matching
     │
     ▼
5. Confidence Classification (High / Medium / Low)
     │
     ▼
Best Match Answer  OR  Dynamic Suggestions
```

### Scoring Breakdown

| Method | Weight | Description |
|---|---|---|
| **Cosine Similarity** | 65% | Measures angle between query and FAQ vectors |
| **Keyword Overlap** | 35% | Counts direct word matches with significant terms |

### Confidence Levels

| Score Range | Confidence | Response |
|---|---|---|
| High | Best match returned | Direct answer |
| Medium | Partial match found | Answer with disclaimer |
| Low | No strong match | Dynamic suggestions shown |

---

## 📁 Project Structure

```
FAQ-Chatbot/
│
├── app.py              # Main Flask server + NLP logic
├── static/
│   └── style.css       # Glassmorphism UI styles
├── templates/
│   └── index.html      # Main frontend template
├── requirements.txt    # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

* Python 3.8+

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/khushi-Jag/FAQ-Chatbot.git
cd FAQ-Chatbot
```

**2. Create a virtual environment** *(recommended)*

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install flask
```

---

## 📝 Usage

**1. Run the application**

```bash
python app.py
```

**2. Open in browser**

```
http://127.0.0.1:5000
```

**3. Ask a question**

Type any question related to AI, Machine Learning, or Web Development:

```
What is deep learning?
How does NLP work?
What is the difference between AI and ML?
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a feature branch:

```bash
git checkout -b feature/AmazingFeature
```

3. Commit your changes:

```bash
git commit -m "Add AmazingFeature"
```

4. Push and open a Pull Request:

```bash
git push origin feature/AmazingFeature
```

---

## 📝 License

Distributed under the **MIT License**. See `LICENSE` for details.

---

## 📫 Contact

**Khushi Jagwani**
GitHub: [https://github.com/khushi-Jag](https://github.com/khushi-Jag)

---

## 🙏 Acknowledgments

* [Flask Documentation](https://flask.palletsprojects.com/)
* Open Source Community ❤️
