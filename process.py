import pandas as pd
from cleaner import clean_description

def ScrapeAndSave(search_func, evaluate_func, search_term, city):
    
    #new data
    new_jobs = search_func(title=search_term, city = city)
    
    
    columns_to_keep = ["title", "company", "score", "date", "job_url", "description", "id"]
    #read cv
    with open("cv.txt", "r", encoding="utf-8") as f:
        cv_text = f.read()
    
    cv_text = clean_description(cv_text)

    #Load database
    try:
        older = pd.read_csv("jobs.csv")
    except FileNotFoundError:
        older = pd.DataFrame(columns=["title", "company", "score", "date", "job_url", "description", "id"])
        
    older_ids = set(older["id"].astype(str)) 
    older_des = set(older["description"].astype(str))

    #Processing

    for i, row in new_jobs.iterrows():
        job_id = str(row["id"])
        job_des = str(row["description"])

        progress = round(((i + 1) / len(new_jobs)) * 100, 2)
        
        if ((job_id not in older_ids) and (job_des not in older_des)):
            
            print(f"{progress:4.0f} %:{row['title']}...")
            score = evaluate_func(cv=cv_text, jd=row["description"])
            
            # Create a clean row to append
            new_row = row.copy()
            new_row["score"] = score
            
            # Use pd.concat for safer appending
            older = pd.concat([older, new_row.to_frame().T], ignore_index=True)
            older_ids.add(job_id) # Update set to avoid duplicates in same run
        
        

    #Save
    older[columns_to_keep].to_csv("jobs.csv", index=False)
    print("spreadsheet updated, have a gay wonderful day!")