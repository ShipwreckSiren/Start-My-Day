#########################
# Login to the firewall #
#########################

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path= r'C:\bin\chromedriver.exe')
driver.get('http://000.00.000.0:900/')
print ("Opened Firewall")

form_element = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/form/p[2]/input")
form_element.send_keys("myusr")
form_element = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/form/p[3]/input").click()
print ("Firewall ID Entered")

default = "mypass"
usr_input = input("Enter Firewall Credentials: ")
cred = default + usr_input

form2_element = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/form/p[2]/input")
form2_element.send_keys(cred)
form2_element = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/form/p[3]/input").click()
sleep(10)

Signon_Methods = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td[2]/font")

try:
    Signon_Methods = driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/form/p[3]/input").click()
    print ("Signed into the firewall")

except: print("Sign on error")
