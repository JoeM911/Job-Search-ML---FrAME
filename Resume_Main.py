from fetchusa_jobs import fetch_jobs
from clean_jobs import cleaned_jobs
from resume_match import run_resume_match

def main():
    print("\n--- JOB MATCHER PIPELINE START ---\n")

    fetch_jobs()
    cleaned_jobs()
    run_resume_match()

    print("\n--- PIPELINE COMPLETE ---\n")

if __name__ == "__main__":
    main()
