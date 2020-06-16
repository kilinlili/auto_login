# coding:utf-8

from selenium import webdriver
import time

user_name = 
pass_word = 


driver = webdriver.Chrome(executable_path='/mnt/c/Users/kilin/env0/chromedriver_win32/chromedriver.exe')
driver.get("https://moodle.s.kyushu-u.ac.jp/login/index.php")
time.sleep(1)



username_box = driver.find_element_by_xpath("//*[@id='username']")
password_box = driver.find_element_by_xpath("//*[@id='password']")
username_box.send_keys(user_name)
password_box.send_keys(pass_word)

time.sleep(1)

login_button = driver.find_element_by_xpath("//*[@id='loginbtn']")
login_button.click()


time.sleep(1)
driver.get("https://moodle.s.kyushu-u.ac.jp/course/view.php?id=21538")


driver.refresh()
driver.refresh()
driver.refresh()

time.sleep(1)

print("OK\n")

driver.close()

