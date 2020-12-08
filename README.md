# python-selenium-contrast-json
use selenium based on python to open json.cn and contrast json automaticly

This is a tiny program to contrst two jsons based on python automaticly.  
Firstly, you need to prepare a document, as for me, it is an excel document, it can be helpful for me to compare with two jsons.
 
   
Here is the step of this program.

## 1. Import necessary packages
```
from selenium import webdriver
import xlrd
```
 
## 2.Start website driver, for me, here is a driver for Chorme. And then write down the website that you want to visit, for me, json.cn is a nice website that can format json,the most important point is, it can be much more easiler for you to read. 
```
driver = webdriver.Chrome()
driver.get("https://www.json.cn/")
time.sleep(2)
```

## 3.Let the project open your specific document and specific sheet.Use a loop to read the rows and cols,  
## and then put the content into the website, before this step, you need to find the id on the page where you need put the content into.
```
data = xlrd.open_workbook('doc.xlsx')
tables = data.sheets()[0]
allRows = tables.nrows
allCols = tables.ncols
for rows in range(1, allRows + 1):
    cell_values = tables.cell(rows, 5).value
    # str = str(cell_values)
    # pyperclip.copy(cell_values)
    driver.get("https://www.json.cn/")
    driver.find_element_by_id("json-src").send_keys(cell_values)
    time.sleep(30)
    driver.find_element_by_id("json-src").send_keys('0')
```

## 4.Close and quit the driver, if you do not do this, then your ram will be die:) trust me.  
NEVER FORGET TO CLOSE AND QUIT IN THE END OF THE CODE!!!!
```
driver.close()
driver.quit()
```
