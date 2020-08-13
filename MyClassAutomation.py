from time import sleep
import datetime

try:
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
except Exception as e:
	print('Requirement Not Satisfied !')
	print("Download necessary files, using commands:")
	print('pip install selenium')
	sleep(5)
	quit()
	
try:
	driver = webdriver.Chrome('./chromedriver')
	# driver.maximize_window()
	driver.get("https://myclass.lpu.in/")
except Exception as e:
	print('Download ChromeDriver, of same version as Chrome')
	print('https://chromedriver.chromium.org/downloads')
	sleep(10)
	quit()

def login():
	user_field = driver.find_element_by_xpath('//*[@id="txtUserName"]')
	user_field.send_keys("11903306")
	pass_field = driver.find_element_by_xpath('//*[@id="txtPassword"]')
	pass_field.send_keys("9419Roshank@")
	pass_field.send_keys(Keys.RETURN)

def goToClass():
	sleep(1) # wait till the table datas are not updated
	maxClasses = 6
	grayColor = '128'
	for i in range(1, maxClasses):
		try:
			sub = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div[1]/div[2]/a['+str(i)+']')
			bgColor = sub.value_of_css_property('background')
		except:
			print('All classes are completed, Come Next Day')
			return
		if(grayColor not in bgColor):
			# print(bgColor)
			sub.click()
			break
	joinClass()


def joinClass():
	sleep(0.5)
	try:
		joinButton = driver.find_element_by_xpath('//*[@id="meetingSummary"]/div/div/a')
		joinButton.click()
	except Exception as e:
		print("Class is Not Started Yet")

def chooseMode():
	# speakMode = driver.find_element_by_xpath('')
	# listenMode = driver.find_element_by_xpath('')
	pass

def wishTeacher():
	now = datetime.datetime.now()
	if(now.hour<12):
		wish="Good Morning"
	elif(now.hour>=12 and now.hour<=4):
		wish="Good Afternoon"
	else:
		wish="Good Evening"

	chatbox = driver.find_element_by_xpath('//*[@id="message-input"]')
	chatbox.send_keys(wish)
	chatbox.send_keys(Keys.RETURN)

login()
homePage = driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]/div/div[2]/a')
homePage.click()
goToClass()

# chooseMode()
# wishTeacher()

sleep(3)
driver.close() # to close the browser and driver
driver.quit() #closes all the tabs



#Join Button
# //*[@id="meetingSummary"]/div/div/a

#Chat box
# //*[@id="message-input"]

# print(driver.title)

# CSS ID: .find_element_by_id(“id-search-field”)
# DOM Path: .find_element_by_xpath(“//input[@id=’id-search-field’]”)
# CSS class: .find_element_by_class_name(“search-field”)


# print(driver.current_url)


'''
//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[1]
//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[2]
//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[3]
//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[4]
//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div/div[2]/a[5]
'''
