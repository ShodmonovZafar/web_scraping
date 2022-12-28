import requests
import functions
from bs4 import BeautifulSoup

# Step 1: Find the URL that you want to scrape.
# Method 1:
URL = "https://example.com/"  # Step 1.1
page = requests.get(URL)  # Step 1.2
soup_1 = BeautifulSoup(page.content, 'html.parser')  # Step 1.3

# Method 2:
html_doc = """
<html>
    <head>
        <title>
            The Dormouse's story
        </title>
    </head>
    <body><p class="title">
            <b>
                The Dormouse's story
            </b>
        </p>

        <p class="story">
            Once upon a time there were three little sisters; and their names were
            
            <a href="http://example.com/elsie" class="sister" id="link1">
                Elsie
            </a>,
            
            <a href="http://example.com/lacie" class="sister" id="link2">
                Lacie
            </a>
            
            and
            
            <a href="http://example.com/tillie" class="sister" id="link3">
                Tillie
            </a>;
            
            and they lived at the bottom of a well.
            
            </p>

        <p class="story">...</p>
"""
soup_2 = BeautifulSoup(html_doc, "html.parser") # Step 1.2

# Method 3:
path_to_the_html_document = "html_files/index.html"  # Step 1.1
with open(path_to_the_html_document) as f:  # Step 1.2
    soup_3 = BeautifulSoup(f, "html.parser")  # Step 1.3

# Step 2: Inspecting the Page.
# This step is performed in a web browser.

# Step 3: Find the data you want to extract.
# This step is performed in a web browser.

# Step 4: Write the code.
# This step is performed in a functions.py modul.

# Step 5: Run the code and extract the data.
data = functions.convert_soup_to_csv(soup_3)  # Step 5.1
print(data)  # Step 5.2

# Step 6: Store the data in the required format.
#path_csv_file = "csv_files/data_1.csv"  # Step 6.1
#functions.save_data_to_csv(data, path_csv_file)  Step 6.2
