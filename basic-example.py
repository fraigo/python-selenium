# Basic Example
# Pre-requisites:
# * Install python-selenium
#   pipbas   install -U selenium
# * Download chromedriver (same version of your Chrome browser installed)
#   https://chromedriver.chromium.org/downloads
#   Uncompress and save chromedriver executable into subfolder drivers/

import time

from selenium import webdriver

from selenium.webdriver.common.by import By

# For Windows users , file is chromedriver.exe (add .exe to chromedriver file name)
driver = webdriver.Chrome("drivers/chromedriver")

# set max number of seconds to load a page
driver.set_page_load_timeout(10)

# go to the URL
# https://selenium-python.readthedocs.io/navigating.html
driver.get("https://google.com")

# find the input for search (<input name="q">)
# https://selenium-python.readthedocs.io/navigating.html#filling-in-forms
# https://selenium-python.readthedocs.io/navigating.html#interacting-with-the-page
driver.find_element("name","q").send_keys("Python Selenium")

# find the button to perform search (<input name="btnK" role="button">) and click it
# https://selenium-python.readthedocs.io/locating-elements.html
driver.find_element("name","btnK").click()

# wait for 2 seconds
time.sleep(1)

# locate elements : search results (<div class="g"></div> elements)
# https://selenium-python.readthedocs.io/locating-elements.html
elements = driver.find_elements(By.CLASS_NAME, 'g')

# loop over elements found
for element in elements:
    print("############")
    # find a subelement (a tag for link info)
    link = element.find_element(By.TAG_NAME,"a")
    print("Link Name:\n" + link.text)
    # get href attribute of link
    print("Link URL:\n" + link.get_attribute("href"))


driver.close()
driver.quit()

print("Finished")
