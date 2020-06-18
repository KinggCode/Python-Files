from bs4 import BeautifulSoup
import requests

url = "https://www.linkedin.com/jobs/search/?alertAction=viewjobs&distance=25&keywords=internship&location=Berlin&locationId=PLACES.de.2-1"

response = requests.get(url)            #Response should have the value,
                                        #Response[200]
#print(response)
data = response.text                    #Getting source code from the page
#print(data)

soup = BeautifulSoup(data,'html.parser')    #This helps in arrange data parsed from html pages.
tags = soup.find_all('a')                   #Finding all links on the pages.

#for tag in tags:
    #print(tag.get('href'))

titles = soup.find_all("a",{"class":"job-card-search__link-wrapper js-focusable disabled ember-view"})
count = 0
for title in titles:
    count +=1
    print(count)
    print(title.text)

address = soup.find_all("span",{"class":"subtle loc"})
for addres in address:
    print(addres.text)

jobs = soup.find_all("li",{"class":"jl"})
for job in jobs:
    #title = job.find_all('a':'
    print(job.text)
    
    
