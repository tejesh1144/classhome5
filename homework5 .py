#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup 
from selenium import webdriver
import csv 
import time 

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open the URL in the browser
driver.get("https://www.naukri.com/data-science-jobs?src=discovery_trendingWdgt_homepage_srch")

# Wait for the page to load (adjust the time based on your internet speed)
time.sleep(5)

# Parse the page source using BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Define class for job data
job_class = "cust-job-tuple layout-wrapper lay-2 sjw__tuple"

# Find elements with specified class
job_data_div = soup.find_all(class_=job_class)

# Extract text from found elements and store in a list
job_data = []
for i in job_data_div:
    job_data.append(i.text)

# Define the output CSV file path
output_file = "job_data.csv"

# Write the data to the CSV file
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # Write data rows
    for data in job_data:
        writer.writerow([data])

# Print message after data is saved
print(output_file)

# Close the WebDriver
driver.quit()


# In[ ]:




