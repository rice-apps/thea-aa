import pandas as pd
from xls2xlsx import XLS2XLSX
import pandas as pd
import os  

"""
This file contains the pipeline to convert .xls extension file downloaded from Superfund Site 
to .xlxs extension. 

.xls - the file extension for Microsoft Excel spreadsheets created between 1997 and 2003
.xlxs - Based on XML, the XLSX format launched with Office 2007

Requirement: 
"""

# relative paths to the stored .xls file
xls_file_path = "backend-thea-aa/downloads/cqry.xls"
xlsx_file_path = "backend-thea-aa/downloads/converted/file.xlsx"

# convert
converter = XLS2XLSX(xls_file_path)
converter.to_xlsx(xlsx_file_path)

# read the data
df = pd.read_excel(xlsx_file_path)

# backend-thea-aa/downloads
os.makedirs('backend-thea-aa/downloads/converted', exist_ok=True)  
df.to_csv('backend-thea-aa/downloads/converted/superfund_data.csv')  

# display
print(df.head(15))
print(df.shape)
print(df.columns)
print(df.dtypes)

