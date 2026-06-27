import streamlit as st
import pandas as pd
import plotly.express as px

from utils import (
    extract_text_from_pdf,
    extract_text_from_txt,
    analyze_resume
)

st.set_page_config(
    page_title="Resume Analyzer Pro",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Resume Analyzer Pro")

st.caption(
    "Explainable AI Resume Classification using NLP • TF-IDF • Chi² Feature Selection • Linear SVM"
)

st.markdown(
"""
Built by **Kiran K. Sahu**

---
"""
)

#Sidebar

st.sidebar.title("📊 Model Information")

st.sidebar.info(
"""
**Version:** 1.0

**Developer:** Kiran K. Sahu

**Algorithm**
- Linear SVM

**Vectorizer**
- TF-IDF

**Feature Selection**
- Chi²

**Features**
- 4,000

**Dataset**
- 2,483 Resumes
- 24 Categories
"""
)

# ===========================
# Dashboard Metrics
# ===========================

st.markdown("## 📊 Model Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Accuracy",
        value="74.65%"
    )

with col2:
    st.metric(
        label="Macro F1",
        value="70.44%"
    )

with col3:
    st.metric(
        label="Categories",
        value="24"
    )

with col4:
    st.metric(
        label="Features",
        value="4,000"
    )

st.divider()

#Result
# ==================================================
# Upload Resume
# ==================================================

st.header("📂 Upload Resume")

uploaded_file = st.file_uploader(
    "Choose Resume",
    type=["pdf", "txt"]
)

# ==================================================
# Process Uploaded Resume
# ==================================================

if uploaded_file is not None:

    if st.button(
        "🚀 Analyze Resume",
        type="primary",
        use_container_width=True
    ):

        with st.spinner("Analyzing Resume..."):

            # Read resume
            if uploaded_file.name.endswith(".pdf"):
                resume_text = extract_text_from_pdf(uploaded_file)
            else:
                resume_text = extract_text_from_txt(uploaded_file)

            # Preview
            st.subheader("📄 Resume Preview")

            st.text_area(
                "Extracted Resume Text",
                resume_text[:1500],
                height=250
            )

            st.divider()

            # Prediction
            result = analyze_resume(resume_text)

            left, right = st.columns([2, 1])

            with left:
                st.subheader("🤖 Prediction")
                st.success(result["prediction"])
                st.subheader("🥇 Top 3 Matches")
                for role in result["top3"]:
                    st.progress(role["ranking"] / 100)

                    st.write(
                        f"**{role['category']}**"
                    )
                    st.caption(
                        f"Model Score: {role['score']:.2f}"
                    )
                #Pie

                chart = pd.DataFrame(result["top3"])
                fig = px.pie(
                    chart,
                    names="category",
                    values="ranking",
                    hole=0.55,
                    title="Top Ranked Categories"
                )
                st.plotly_chart(
                    fig,
                    use_container_width=True
                    )
                
            
            with right:
                st.subheader("📊 Resume Statistics")
                words = len(resume_text.split())
                chars = len(resume_text)
                minutes = round(words / 200, 1)
                st.metric("Words", words)
                st.metric("Characters", chars)
                st.metric("Read Time", f"{minutes} min")

            
            #Keyword Badges

            st.subheader("🔍 Why did the AI predict this?")

            st.write(
                "Most influential keywords detected in your resume:"
            )
            cols = st.columns(4)
            for i, word in enumerate(result["keywords"]):
                cols[i % 4].success(word)

            #Resume Statistics

            st.divider()

            a, b, c = st.columns(3)

            a.metric(
                "Words",
                len(resume_text.split())
            )

            b.metric(
                "Characters",
                len(resume_text)
            )

            c.metric(
                "Read Time",
                f"{round(len(resume_text.split())/200,1)} min"
            )
            #Model Details
            with st.expander("📋 Model Information"):

                st.write("""
                Algorithm: Linear SVM

                Vectorizer: TF-IDF

                Feature Selection: Chi²

                Dataset: 2483 resumes

                Classes: 24
                """)