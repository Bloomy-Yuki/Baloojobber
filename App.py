#terminal
from cleaner import clear_console
from datetime import date

#comparison
from encoder import Encode #Encoders are free but bloat the system, use only when dev
from deepseek import deepseek

#scrapers
from jobspy_ import DataframeJobspy
from googlejobs_ import GoogleJobs

#processing
from process import ScrapeAndSave

#----------------------------------------
print(f"{date.today()} \t BalooJobber v0.01")
print(f"="*40)
print(f"""The program will scrape various sources on the internet
and will output a spreadsheet with all the data in jobs.csv""")

search_term = str(input("what job title are you looking for?: "))
search_city = str(input("which city?: "))
#----------------------------------------

ScrapeAndSave(DataframeJobspy,Encode, search_term=search_term, city= search_city)

#ScrapeAndSave(DataframeJobspy,deepseek, search_term=search_term, city= search_city)
#ScrapeAndSave(GoogleJobs,deepseek, search_term= search_term,city= search_city)




