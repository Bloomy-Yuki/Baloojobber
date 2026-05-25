import pandas as pd
from jobspy import scrape_jobs

def DataframeJobspy(title, city = "cologne", dist = 15, results = 20 ):
    print("scraping linkedin and indeed...")
    jobs = scrape_jobs(
    site_name=["indeed","linkedin"],
    search_term= title,
    location = city,
    results_wanted = results,
    hours_old= 240,
    country_indeed='germany',
    distance = dist,
    linkedin_fetch_description=True 
    )
    print(f"Found {len(jobs)} jobs")
    return pd.DataFrame(jobs)
