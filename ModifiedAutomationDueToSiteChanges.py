from time import sleep
import datetime
import os

try:
	from selenium import webdriver
	from selenium.webdriver.common.keys import Keys
	from selenium.webdriver.support.ui import WebDriverWait
	from selenium.webdriver.support import expected_conditions as EC
	from selenium.webdriver.common.by import By
	print('Pass: Requirement Satisfied')
except Exception as e:
	print('Requirement Not Satisfied !')
	choice = input("Do you want to Download Selenium (Y/N): ")
	if(choice.lower()=="y"):
		os.system("pip install selenium")
	else:
		print("Download necessary files, using command ( pip install selenium )")
	sleep(5)
	quit()

try:
	driver = webdriver.Chrome('./chromedriver') 
	driver.maximize_window()
	print("Pass: Browser Opened")
	driver.get("https://myclass.lpu.in/")
except Exception as e:
	print('Download ChromeDriver, of same version as of Chrome')
	print('https://chromedriver.chromium.org/downloads')
	sleep(10)
	quit()

def login():
	sleep(1)
	driver.get("https://myclass.lpu.in/") #due to MyClass site modification
	print()
	try:
		user_field = driver.find_element_by_xpath('//*[@id="txtUserName"]')
		user_field.send_keys("RegID")
		pass_field = driver.find_element_by_xpath('//*[@id="txtPassword"]')
		pass_field.send_keys("Password")
		# pass_field.send_keys(Keys.RETURN)
		
		#Due to Captcha added in MyClass, manually type captcha
		print('Please Enter Captcha Fast: ')
		sleep(20) # time tiil you enter the captcha
	except Exception as e:
		print("Fail: Something ocurred while logging !")
		sleep(60)
		driver.quit()
		quit()
	print('Pass: Login Done')


def goToClass():
	try:
		element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div[1]/div[2]/a[1]')))
	except Exception as e:
		print("Its Holiday, enjoy your day")
		sleep(5)
		driver.quit()
		quit()

	maxClasses = 7 #maximum classes in a week
	grayColor = '128, 128, 128'
	for i in range(1, maxClasses+2):
		try:
			sub = driver.find_element_by_xpath('//*[@id="calendar"]/div[2]/div/table/tbody/tr/td/div/div/div[3]/table/tbody/tr/td[2]/div[1]/div[2]/a['+str(i)+']')
			bgColor = sub.value_of_css_property('background')
		except Exception as e:
			print('All classes are completed, Come Next Day')
			sleep(5)
			driver.quit()
			quit()
		if(grayColor not in bgColor):
			sub.click()
			break
	joinClass()

def joinClass():
	try:
		joinButton = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="meetingSummary"]/div/div/a')))
		joinButton.click()
	except Exception as e:
		print("Class is Not Started Yet")
		sleep(5)
		quit()
	chooseMode()

def chooseMode():
	# sleep(10)
	try:
		frame = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="frame"]')))
		driver.switch_to.frame(frame)
		print("Pass: Joined Class")
		listenMode = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/span/button[2]')))
		listenMode.click()
	except Exception as e:
		print("Teacher had not started the meeting")
		quit()
	print("Pass: Listen Mode Selected")
	wishTeacher()

def wishTeacher():
	now = datetime.datetime.now()
	if(now.hour<12):
		wish="Good Morning"
	elif(now.hour>=12 and now.hour<=15):
		wish="Good Afternoon"
	else:
		wish="Good Evening"

	# sleep(2)
	try:
		chatbox = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID,"message-input"))) 
		chatbox.send_keys(wish)
		chatbox.send_keys(Keys.RETURN)
	except Exception as e:
		print("Fail: Unable to wish the teacher")
		quit()
	print("Pass: Teacher Wished")

login()
try:
	homePage = driver.find_element_by_xpath('//*[@id="homeCenterDiv"]/div/div[1]/div/div[2]/a').click()
	print('Pass: HomePage')
except:
	print("Fail: Unable to Login !")
	driver.quit()
	quit()

goToClass()
sleep(3)
print('Pass: Successfully Executed')
# driver.quit() #closes all the tabs
