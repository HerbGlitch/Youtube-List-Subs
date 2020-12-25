import pandas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver import ActionChains
from time import sleep
from getpass import getpass

username = input("Username: ")
password = getpass()

seleted_driver = "firefox"
driver = webdriver.Firefox()

# If you want to open Chrome IDK if the would work :P
if(seleted_driver == "chrome"):
    driver = webdriver.Chrome()

driver.get("https://stackoverflow.com/users/login?ssrc=head")
driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
driver.find_element_by_xpath('//input[@type="email"]').send_keys(username)
driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
sleep(1)
driver.find_element_by_xpath('//input[@type="password"]').send_keys(password)
driver.find_element_by_xpath('//*[@id="passwordNext"]').click()

pattern="https://stackoverflow.com/"
wait = WebDriverWait(driver, 30)
wait.until(expected_conditions.url_matches(pattern))

driver.get("https://youtube.com")
sleep(10)
driver.get("https://studio.youtube.com")
sleep(1)
driver.find_element_by_xpath("//div[text()='See all']").click()
driver.find_element_by_xpath("//*[@id='date-select']").click()
driver.find_element_by_xpath("//yt-formatted-string[text()='Lifetime']").click()
# driver.find_element_by_xpath("//*[@id='page-size']").click()

temp = driver.find_elements_by_xpath("//div[contains(@class, 'subscriber-info-name style-scope ytcp-subscribers-table-row')]")
names = []
for t in temp:
    names.append(t.get_attribute('innerHTML'))

df = pandas.DataFrame(data={"public subscribers": names})
df.to_csv("./test.csv", sep=",", index=False)