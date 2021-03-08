import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import datetime

# output_file_name = input("Enter log file name: ")
# output_file_path = "/Users/mark.fomin/Documents/Wattbox/{}.txt".format(output_file_name)
# outputFile = open(output_file_path, "a+")


def get_timestamp():
    dt = datetime.datetime.now()
    print_timestamp = dt.strftime("%d-%b-%Y (%H:%M:%S.%f)")
    return print_timestamp


driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.set_window_size(1200, 600)
driver.get("https://app.ovrc.com")
print(get_timestamp(), "Launching OvrC")
time.sleep(2)
# Entering username
driver.find_element_by_xpath("//*[@id='root']/div[1]/div[2]/form/div/fieldset/div[1]/div[2]/input").send_keys("mark.fomin@snapav.com")
print(get_timestamp(), "Entering username...")
# Entering password
driver.find_element_by_xpath("//*[@id='root']/div[1]/div[2]/form/div/fieldset/div[2]/div[2]/input").send_keys("SnapAV704")
print(get_timestamp(), "Entering password...")
time.sleep(1)
# Selecting login button
driver.find_element_by_id("button__login").click()
print(get_timestamp(), "Clicking Login button...")
time.sleep(5)

# Selecting Devices tab
driver.find_element_by_xpath("//*[@id='devices__tab']/span/span[3]").click()
print(get_timestamp(), "Selecting Devices Tab...")
time.sleep(2)

# Selecting the 2 outlet wattbox
driver.find_element_by_xpath("//*[@id='root']/div[2]/div[2]/div/div/div[2]/div/div[2]/div[2]/div/div/table/tbody/tr[4]/td[3]").click()
print(get_timestamp(), "Selecting Wattbox-150 device...")
time.sleep(2)

driver.find_element_by_xpath("//*[@id='root']/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/h2/span[3]/span").click()
print(get_timestamp(), "Expanding device details...")
time.sleep(2)

# Firmware version element
fw_version = driver.find_element_by_xpath("//*[@id='root']/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div[1]/div[5]/span[2]").text
print(get_timestamp(), "Wattbox firmware version is: " + fw_version)
time.sleep(2)

# Reset all outlets button
driver.find_element_by_xpath("//*[@id='root']/div[2]/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/div/button/span[2]").click()
print(get_timestamp(), "Clicked Resetting All Outlets Button...")
time.sleep(2)
# Confirm reset button press
driver.find_element_by_xpath("//*[@id='root']/div[3]/div/div[3]/div[1]/button/span[2]").click()
time.sleep(5)

print(get_timestamp(), "Script finished!")

driver.quit()
