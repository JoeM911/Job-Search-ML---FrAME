**Job Search ML – Resume Matching Framework
Overview**
This project implements a simple resume-to-job matching system using Natural Language Processing (NLP). The goal is to compare the content of a candidate’s resume against job postings and quantify how well they align based on textual similarity.

The system uses a TF-IDF (Term Frequency–Inverse Document Frequency) vectorization approach to convert text into numerical features and compute similarity scores between resumes and job descriptions.

**Key Features**
Resume and job description text preprocessing

TF-IDF vectorization for feature extraction

Cosine similarity scoring to rank job postings

Automated job data retrieval via USAJobs.gov API

Outputs ranked job listings based on resume relevance

**Data Source**

USAJobs.gov API
Job postings are pulled programmatically using API access provided by USAJobs.gov.

**Tech Stack**

Python

scikit-learn (TF-IDF, cosine similarity)

Pandas

Requests

NLP techniques for text cleaning and comparison

**How It Works**

My resume text is loaded and cleaned.

Job postings are retrieved from USAJobs.gov via API.

Both resume and job descriptions are vectorized using TF-IDF.

Cosine similarity scores are calculated.

Jobs are ranked based on similarity to the resume.

**Motivation**

This project was built to explore how machine learning and NLP can be applied to automate and improve the job search process by objectively matching resumes to relevant job postings.

**Future Improvements**
Support for multiple resumes

Keyword weighting by job category

More advanced models (e.g., embeddings / transformers)

Web UI for interactive job ranking

Resume parsing from PDF/DOCX

**Disclaimer**

This project is for educational purposes and demonstrates a baseline ML approach. It is not intended to replace professional recruiting tools.
