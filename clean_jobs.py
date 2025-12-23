import pandas as pd
import re

def cleaned_jobs():
    df = pd.read_csv("jobs_raw.csv")

    def clean_text(text):
        if pd.isna(text):
            return ""
        text = text.lower()
        text = re.sub(r"\s+", " ", text)
        text = re.sub(r"[^a-z0-9\s]", "", text)
        return text.strip()

    df["clean_description"] = df["job_description"].apply(clean_text)

    df.to_csv("jobs_cleaned.csv", index=False)

    print("Saved jobs_cleaned.csv") 
if __name__ == "__main__":
    cleaned_jobs()
