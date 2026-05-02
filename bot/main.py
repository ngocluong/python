from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_opt)
url = "https://appbrewery.github.io/instant_pot/"
wiki = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(wiki)
# dollar = driver.find_element(By.CLASS_NAME, "a-price-whole")
# cent = driver.find_element(By.CLASS_NAME, "a-price-fraction")
# print(f"The price is: {dollar.text}.{cent.text}")

total = driver.find_element(By.XPATH, '//*[@id="articlecount"]/ul/li[1]/a')
print(total.text)
search_box = driver.find_element(By.NAME, 'search')
print(search_box.get_attribute('value'))
search_box.send_keys("Python")
search_box.send_keys(Keys.ENTER)
# search_btn = driver.find_element(By.CSS_SELECTOR, "#searchform button")
# search_btn.click()


# driver.close()
# driver.quit()