# python-selenium-contrast-json
use selenium based on python to open json.cn and contrast json automaticly

This is a tiny program to contrst two jsons based on python automaticly, in this project, 
Firstly, you need to prepare a document, as for me, it is an excel document, it can be helpful for me to compare with two jsons.
 
Here is the step of this program.

1.import necessary packages
```
from selenium import webdriver
import xlrd
```
---
 
2.start website driver, for me, here is a driver for Chorme. And then write down the website that you want to visit, for me, json.cn is a nice website that can format json,the most important point is, it can be much more easiler for you to read. 
```
driver = webdriver.Chrome()
driver.get("https://www.json.cn/")
time.sleep(2)
```
