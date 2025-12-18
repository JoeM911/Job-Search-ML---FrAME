import requests
import csv

API_KEY = "Ej15cpldCLOJgVbYVko+Xg/nGnk5/bOpx4aBQa1VFwY="
USER_AGENT = "joemanayathumariyil2@gmail.com"

headers = {
    "Authorization-Key": API_KEY,
    "User-Agent": USER_AGENT
}

params = {
    "Keyword": "Engineer",
    "ResultsPerPage": 20
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
            item["PositionTitle"],
            item["OrganizationName"],
            item["UserArea"]["Details"]["JobSummary"]
        ])

print("Saved jobs_raw.csv")
