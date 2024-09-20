import time
from itertools import dropwhile

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")
driver.maximize_window()

f = driver.find_element(By.XPATH,"//span[text()='Fashion']")
achain = ActionChains(driver)
achain.move_to_element(f).perform()
time.sleep(2)
m = driver.find_element(By.XPATH,"//a[text()='Men Footwear']")
achain.move_to_element(m).perform()
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/object/a[3]").click()
time.sleep(4)

p = driver.current_window_handle

pointer1 = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div[1]/div/div/div/section[2]/div[3]/div[1]/div[1]/div")
pointer2 = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div/div[1]/div/div/div/section[2]/div[3]/div[1]/div[2]/div")

achain.move_to_element(pointer1).pause(1).click_and_hold(pointer1).move_by_offset(30,0).release().perform()
achain.move_to_element(pointer2).pause(1).click_and_hold(pointer2).move_by_offset(-60,0).release().perform()

time.sleep(4)
driver.find_element(By.XPATH, "//a[@title='Corporate Casuals For Men']").click()
time.sleep(4)

# allhandle = driver.window_handles
#
# for h in allhandle:
#     if h != p:
#         driver.switch_to.window(p)
# time.sleep(4)

driver.close()