
#banner
print("")
print("---------------------------------------")
print("Copyright Lonewolf Software")
print("Experimental Software Testing Facility")
print("FB-Selena v1.0")
print("---------------------------------------")
print("")

#import
from selenium import webdriver
import time
print("Imporing API ...")

chrome_path = r"---Chromedriverpath---"
print("Importing Chromunium Path ...")
print("")

#set
print("Opening Bot Screen...")
driver = webdriver.Chrome(chrome_path)
print("")

#url
print("URL SELECTED : [ https://www.facebook.com/ ]")
driver.get("https://www.facebook.com/")
print("")

#login
print("Inputting Username : ")
driver.find_element_by_xpath("""//*[@id="email"]""").send_keys('#####')
print("Inputting Password : ")
driver.find_element_by_xpath("""//*[@id="pass"]""").send_keys('#####')
print("Logging in...")
driver.find_element_by_xpath("""//*[@id="u_0_r"]""").click()

##navigate
print("Login Success...!!!")
print("")
#homescreen
print("Selecting Home Screen")
driver.get("https://www.facebook.com/home/")
print("Closing Popups")
driver.find_element_by_xpath("""//*[@id="facebook"]/body/div[27]/div[2]/div/div/div/div/div[3]/div/div/div[2]/div/a[1]""").click()

#friends
print("Selecting Friends List")
driver.find_element_by_xpath("""//*[@id="u_0_q"]/li[3]/a""").click()
time.sleep(5)

driver.find_element_by_xpath

#forward to next page
for i in range(1,50):
    print(str(i) + " Page Scrolled")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(0.5)

#list friends
print("Listing Friends")
friends = driver.find_elements_by_class_name("fsl")


#display all friends list
print("Displaying")
for friend in friends:
    print(friend.text)




