# 📄 Resume Analyzer Pro

Explainable AI Resume Classification using:

• NLP
• TF-IDF
• Chi² Feature Selection
• Linear SVM

---

## Features

✅ Upload PDF Resume

✅ Upload TXT Resume

✅ Resume Preview

✅ Explainable AI Keywords

✅ Top-3 Ranked Categories

✅ Interactive Pie Chart

✅ Resume Statistics

---

## Tech Stack

Python

Streamlit

Scikit-learn

NLTK

PyMuPDF

Plotly

---

## Dataset

2483 professional resumes

24 job categories

---

## Accuracy

Accuracy : 74.65%

Macro F1 : 70.44%

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/kiran0198/Resume-Analyzer-Pro.git
```

### 2. Navigate to the project folder

```bash
cd Resume-Analyzer-Pro
```

### 3. Create a virtual environment (Recommended)

Windows:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the setup script

```bash
python setup.py
```

This downloads the required NLTK resources and verifies that all trained model files are available.

## 🚀 How to Run

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

The application will open automatically in your default web browser.

If it doesn't open automatically, visit:

```
http://localhost:8501
```

Upload a PDF or TXT resume and click **🚀 Analyze Resume** to view:

* Resume Preview
* Predicted Job Category
* Top-3 Ranked Categories
* Explainable AI Keywords
* Interactive Dashboard
* Resume Statistics


## Future Work

ATS Resume Score

Skill Gap Analysis

Resume Recommendations

LLM-based Resume Feedback

---

Developed by

Kiran K. Sahu
