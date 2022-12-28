import requests
import functions
from bs4 import BeautifulSoup

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# Step 1: Find the URL that you want to scrape.
URL = "http://example.com/"  # Step 1.1
page_1 = requests.get(URL)  # Step 1.2
soup_1 = BeautifulSoup(page_1.content, 'html.parser')  # Step 1.3.1
soup_2 = BeautifulSoup(html_doc, "html.parser") # Step 1.3.2

# Step 2: Inspecting the Page.
# This step is performed in a web browser.

# Step 3: Find the data you want to extract.
# This step is performed in a web browser.

# Step 4: Write the code.
# This step is performed in a functions.py modul.

# Step 5: Run the code and extract the data.
data_1 = functions.convert_soup_to_csv(soup_2)  # Step 5.1
print(data_1)  # Step 5.2

# Step 6: Store the data in the required format.
#path_csv_file_1 = "csv_files/data_1.csv"  # Step 6.1
#func.save_data_to_csv(csv_h1, path_csv_file_1) 
