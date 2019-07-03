import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Storing the values in the list
name = ['Maximus', 'Dhadharey']
email = ['maximus33@gmail.com', 'dhaddharey33@gmail.com']
age = [22, 21]

# XPath URL
inputName = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/input'
inputEmailID = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/input'
inputAge = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/input'

# Radion Buttons ['Student', 'Enginner', 'Entrepreneur', 'IT Professional', 'Policy maker', 'Social worker', 'Teachers', 'Journalist', 'Freelancer', 'others']
radioStudent = '//*[@id="mG61Hd"]/div/div[2]/div[2]/div[4]/div/div[2]/div/span/div/div[1]/label/div/div[1]'

# Submit Buttons
submit = '//*[@id="mG61Hd"]/div/div[2]/div[3]/div[1]/div/div/span'


def sleep():
	time.sleep(3)



browser = webdriver.Firefox()
browser.get('https://docs.google.com/forms/d/11agBkil4mX-ZHmlq-ILaBUqyy1jH_yfSHELm6FZfbVc/viewform?edit_requested=true')

# Implement the for loop in the list data type
i = 0

while i < len(name):

	browser.find_element_by_xpath(inputName).send_keys(name[i])

	browser.find_element_by_xpath(inputEmailID).send_keys(email[i])

	browser.find_element_by_xpath(inputAge).send_keys(age[i])

	browser.find_element_by_xpath(radioStudent).click()

	sleep()

	browser.find_element_by_xpath(submit).click()

	i += 1

	sleep()

	browser.back()
 
	sleep()
	
#Finish the loop here

# Quit browser 
browser.quit()