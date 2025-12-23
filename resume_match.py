import pandas as pd
import re
from docx import Document
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def run_resume_match():

    # -------------------------
    # Utility: clean text
    # -------------------------
    def clean_text(text):
        text = text.lower()
        text = re.sub(r"\s+", " ", text)
        text = re.sub(r"[^a-z0-9\s]", "", text)
        return text.strip()

    # -------------------------
    # Load jobs
    # -------------------------
    df = pd.read_csv("jobs_cleaned.csv")

    process_title_keywords = [
       "chemical engineer",
        "process engineer",
        "chemical engineering",
        "process engineering",
        
    ]

    df = df[df["job_title"].str.contains(
        "|".join(process_title_keywords),
        case=False,
        na=False
    )].reset_index(drop=True)

    # -------------------------
    # Load resume DOCX (relative path)
    # -------------------------
    doc = Document(r"C:\Users\Joe\Downloads\Joe Manoj RESUME.docx")
    lines = [p.text.strip() for p in doc.paragraphs if p.text.strip()]

    # -------------------------
    # Detect EXPERIENCE / INTERNSHIP section
    # -------------------------
    experience_lines = []
    in_experience = False

    for line in lines:
        lower = line.lower()

        if "experience" in lower or "internship" in lower:
            in_experience = True
            continue

        if "skills" in lower or "education" in lower:
            in_experience = False

        if in_experience:
            experience_lines.append(line)

    # -------------------------
    # Extract bullet-like lines
    # -------------------------
    bullets = [line for line in experience_lines if len(line.split()) > 6]

    # -------------------------
    # Identify process / chemical bullets
    # -------------------------
    process_terms = [
    "process",
    "chemical",
    "hazop",
    "pssr",
    "loto",
    "reactor",
    "distillation",
    "unit operations",
    "process safety",
    "plant",
    "chemicals",
    ]

    process_bullets = [
        b for b in bullets
        if any(term in b.lower() for term in process_terms)
    ]

    # -------------------------
    # Build weighted resume text
    # -------------------------
    resume_text = (
        " ".join(process_bullets * 3) + " " +
        " ".join(bullets)
    )

    resume_text = clean_text(resume_text)

    # -------------------------
    # Combine jobs + resume
    # -------------------------
    documents = df["clean_description"].tolist()
    documents.append(resume_text)

    # -------------------------
    # TF-IDF
    # -------------------------
    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=1000
    )

    tfidf_matrix = vectorizer.fit_transform(documents)

    # -------------------------
    # Cosine similarity
    # -------------------------
    resume_vector = tfidf_matrix[-1]
    job_vectors = tfidf_matrix[:-1]

    similarity_scores = cosine_similarity(
        resume_vector, job_vectors
    )[0]

    df["match_score"] = similarity_scores

    top_matches = df.sort_values(
        "match_score", ascending=False
    )

    top_matches = top_matches.rename(columns={
        "job_title": "Job Title",
        "agency": "Agency",
        "match_score": "Match Score"
    })

    print(
        top_matches[["Job Title", "Agency", "Match Score"]]
        .head(10)
        .to_string(index=False)
    )

if __name__ == "__main__":
    run_resume_match()
