
import pandas as pd
import openpyxl

scraper = pd.read_html("https://www.licious.in/red-meat")
print(scraper)
