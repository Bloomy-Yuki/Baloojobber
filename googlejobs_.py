import pandas as pd
import serpapi
from cleaner import clean_description
import os
from dotenv import load_dotenv

load_dotenv()

# Access them like this
API_KEY = os.getenv("SERP_API_KEY")

if not API_KEY:
    raise ValueError("API_KEY not found in .env file!")




def GoogleJobs(title, city = "cologne"):
    print(f"Searching Google for '{title}' jobs in {city}...\n")
    client = serpapi.Client(api_key=API_KEY)    
    params = {
        "engine": "google_jobs",
        "q": title,
        "location": city,
        "gl": "de",
        "chips": "date_posted:week",
        "api_key": API_KEY
    }

    all_jobs = []

    # Loop through the pages (e.g., 3 pages = up to 30 jobs)
    for page in range(2):
        print(f"Fetching page {page + 1}...")
        
        search = client.search(params)
        results = search.as_dict()
        
        if "error" in results:
            print(f"API Error: {results['error']}")
            break

        # Add this page's jobs to our master list
        jobs = results.get("jobs_results", [])
        all_jobs.extend(jobs)
        
        # Look for the pagination token in the response
        pagination = results.get("serpapi_pagination", {})
        next_token = pagination.get("next_page_token")
        
        #If there is no next token, we've reached the end of the jobs!
        if not next_token:
            print("No more pages available.")
            break
            
        #If there is a next page, update the parameters for the next loop
        params["next_page_token"] = next_token

    print(f"\nScraped {len(all_jobs)} total jobs.\n")
    print("=" * 40)
    
    extracted_data = []
    
    #Loop through the raw SerpApi results
    for job in all_jobs:
        
        # safely extract the first apply link, if it exists
        apply_options = job.get("apply_options", [])
        
        job_link = apply_options[0].get("link") if apply_options else "No Link Available"
        
        # safely extract the posted date (e.g., "2 days ago")
        extensions = job.get("detected_extensions", {})
        posted_date = extensions.get("posted_at", "Unknown Date")

        # Build a clean dictionary for each job
        job_data = {
            "title": job.get("title", "Unknown Title"),
            "company": job.get("company_name", "Unknown Company"),
            "score": None,
            "date": posted_date,     
            "job_url": job_link,               
            "description": clean_description(job.get("description", "")),
            "id": job.get("job_id")
        }
        extracted_data.append(job_data)
    
    df = pd.DataFrame(extracted_data)
    
    return df



