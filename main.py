import logging
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def displayResult(task):
    print('Found: ' + str(len(task)) + ' Text blocks')
    print(task)


list_undercurledRedText = []
list_undercurledRedTextFiltered = []

browser = webdriver.Edge()

browser.get('https://developer.mozilla.org/de/docs/Web/API/Document')

# print("----------------- Task 1 ----------------- ")
for undercurledRedText in WebDriverWait(browser, 20).until(
        EC.visibility_of_all_elements_located((By.XPATH, "//a[@class='page-not-created']//code"))):
    list_undercurledRedText.append(undercurledRedText.text)

# print("----------------- Task 2 ----------------- ")
# Non-Standard = !
for undercurledRedTextFiltered in WebDriverWait(browser, 20).until(EC.visibility_of_all_elements_located(
        (By.XPATH, "//a[@class='page-not-created'][following-sibling::abbr[@class='icon icon-nonstandard']]"))):
    list_undercurledRedTextFiltered.append(undercurledRedTextFiltered.text)

# time.sleep(5)
browser.quit()

print('1: Red Underlined text block')
print('2: Red Underlined Text with "!" symbol')
print('press 0 to exit')
selectText = 0
while 1 >= selectText or 2 <= selectText:
    try:
        selectText = int(input("Please choose 1 or 2 : "))
        if selectText == 1:
            displayResult(list_undercurledRedText)
        elif selectText == 2:
            displayResult(list_undercurledRedTextFiltered)
        elif selectText == 0:
            break
        else:
            print("Invalid option")

    except ValueError:
        # Remember, print is a function in 3.x
        print("That wasn't an integer")


