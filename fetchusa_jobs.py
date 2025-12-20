import requests
import csv

def fetch_jobs():
    API_KEY = "Ej15cpldCLOJgVbYVko+Xg/nGnk5/bOpx4aBQa1VFwY="
    USER_AGENT = "joemanayathumariyil2@gmail.com"

    headers = {
        "Authorization-Key": API_KEY,
        "User-Agent": USER_AGENT
    }

    params = {
        "Keyword": "Engineer",
        "ResultsPerPage": 500  # USAJobs hard limit
    }

    response = requests.get(
        "https://data.usajobs.gov/api/search",
        headers=headers,
        params=params
    )

    data = response.json()
    jobs = data["SearchResult"]["SearchResultItems"]

    with open("jobs_raw.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["job_title", "agency", "job_description"])

        for job in jobs:
            item = job["MatchedObjectDescriptor"]

            writer.writerow([
                item.get("PositionTitle", ""),
                item.get("OrganizationName", ""),
                item.get("UserArea", {}).get("Details", {}).get("JobSummary", "")
            ])

    print(f"Fetched and saved {len(jobs)} job listings to jobs_raw.csv")

if __name__ == "__main__":
    fetch_jobs()
