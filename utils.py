import re
import pymupdf as fitz              # PyMuPDF
import joblib
import numpy as np
import nltk

for pkg in ["punkt", "punkt_tab", "wordnet", "omw-1.4"]:
    try:
        nltk.data.find(pkg)
    except LookupError:
        nltk.download(pkg, quiet=True)



from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


lemmatizer = WordNetLemmatizer()

vectorizer = joblib.load("models/tfidf_vectorizer.pkl")

selector = joblib.load("models/chi2_selector.pkl")

model = joblib.load("models/svm_resume_classifier.pkl")


feature_names = vectorizer.get_feature_names_out()

selected_features = feature_names[
    selector.get_support()
]

print("Models loaded successfully.")

#PDF Reader

def extract_text_from_pdf(uploaded_file):
    """
    Extract text from a PDF uploaded through Streamlit.
    """

    text = ""

    pdf = fitz.open(
        stream=uploaded_file.read(),
        filetype="pdf"
    )

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text

#TXT Reader

def extract_text_from_txt(uploaded_file):
    """
    Extract text from TXT file.
    """

    return uploaded_file.read().decode("utf-8")



#Clean resume text

def clean_resume(text):

    text = str(text)

    # Remove HTML
    text = re.sub(r"<.*?>", " ", text)

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", " ", text)

    # Remove emails
    text = re.sub(r"\S+@\S+", " ", text)

    # Remove phone numbers
    text = re.sub(r"\+?\d[\d\s().-]{7,}\d", " ", text)

    # Lowercase
    text = text.lower()

    # Keep only letters
    text = re.sub(r"[^a-zA-Z\s]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    words = word_tokenize(text)

    words = [
        lemmatizer.lemmatize(word)
        for word in words
        if len(word) >= 3 and word.isalpha()
    ]

    return " ".join(words)

#Predict resume category

def analyze_resume(resume_text):

    # Clean
    cleaned = clean_resume(resume_text)

    # TF-IDF
    vector = vectorizer.transform([cleaned])

    # Chi²
    vector_selected = selector.transform(vector)

    # Prediction
    prediction = model.predict(vector_selected)[0]

    # Decision scores
    scores = model.decision_function(vector_selected)[0]

    # ---------- TOP 3 ----------
    idx = np.argsort(scores)[::-1]

    top3 = []

    max_score = scores.max()

    confidence = np.exp(scores - max_score)
    confidence = confidence / confidence.sum()

    for i in idx[:3]:

        top3.append({
            "category": model.classes_[i],
            "score": float(scores[i]),
            "ranking": round(float(confidence[i]) * 100, 2)
        })

    # ---------- KEYWORDS ----------

    pred_index = list(model.classes_).index(prediction)

    coef = model.coef_[pred_index]

    active = vector_selected.toarray()[0]

    contribution = coef * active

    keyword_idx = np.argsort(contribution)[::-1]

    keywords = []

    for i in keyword_idx:

        if active[i] > 0:

            keywords.append(selected_features[i])

        if len(keywords) == 8:
            break

    return {
    "prediction": prediction,
    "top3": top3,
    "keywords": keywords,
    "cleaned_text": cleaned
    }

