import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import csv
from colorama import Fore
import getpass

Email_id = input("\033[1;32m Enter your Valid Email Address here : \t")
Password = getpass.getpass("\033[1;32m Enter the Password Here : \t")
file_csv = input("\033[1;32m Enter Your CSV path here: \t ")
Chrome_path = input("\033[1;32m Enter your Chrome Path here: \t")
print(Fore.RED + "NOTE : YOU NEED TO DISABLE THE 2FA OR ELSE THIS BOT WILL NOT WORK")

time.sleep(10)
options = webdriver.ChromeOptions()
options.add_argument('proxy-server=106.122.8.54:3128')
options.add_argument(r'--user-data-dir={}'.format(Chrome_path))
browser = uc.Chrome(options=options)
browser.maximize_window()
browser.get("https://studio.youtube.com")
try:
    browser.find_element(By.ID, 'identifierId').send_keys(Email_id)
    browser.find_element(By.CSS_SELECTOR, '#identifierNext > div > button > span').click()
    password_selector = "#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input"
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, password_selector)))
    browser.find_element(By.CSS_SELECTOR, password_selector).send_keys(Password)
    browser.find_element(By.CSS_SELECTOR, '#passwordNext > div > button > span').click()
except:
    pass
with open(file_csv, newline='', mode='r') as csvfile:
    reading = csv.DictReader(csvfile)
    for row in reading:
        file_path = row['filepath']
        title_text = row['title']
        description_type = row['description']
        tags_values = row['tags']
        date = row['date']
        time_add = row['time']
        
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#upload-icon"))).click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="content"]/input'))).send_keys(file_path)
        title = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='textbox']")))
        title.clear()
        title.send_keys(title_text)
        time.sleep(3)
        description = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div")))
        description.clear()
        description.send_keys(description_type)
        no_for_kids = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='audience']/ytkc-made-for-kids-select/div[4]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]")))
        browser.execute_script("arguments[0].scrollIntoView(true);", no_for_kids)
        no_for_kids.click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#toggle-button"))).click()
        tags = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='chip-bar']/div")))
        browser.execute_script("arguments[0].scrollIntoView(true);", tags)
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='clear-button']"))).click()
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[4]/ytcp-form-input-container/div[1]/div/ytcp-free-text-chip-bar/ytcp-chip-bar/div/input"))).send_keys(tags_values)
        next_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='next-button']")))
        for i in range(3):
                    next_button.click()
                    time.sleep(1)
        schedule_button = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='schedule-radio-button']"))).click()
        schedult_text = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='datepicker-trigger']/ytcp-dropdown-trigger/div/div[2]/span"))).click()
        action = ActionChains(browser)
        action.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE * 15).perform()
        time.sleep(3)
        schedult_text = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='datepicker-trigger']/ytcp-dropdown-trigger/div/div[2]/span")))
        browser.execute_script("arguments[0].scrollIntoView();", schedult_text)
        writing_schedult_text = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytcp-date-picker/tp-yt-paper-dialog/div/form/tp-yt-paper-input/tp-yt-paper-input-container/div[2]/div/iron-input/input")))
        writing_schedult_text.send_keys(date)
        writing_schedult_text.send_keys(Keys.ENTER)
        time.sleep(5)
        time_schedule = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[3]/ytcp-visibility-scheduler/div[1]/ytcp-datetime-picker/div/div[2]/form/ytcp-form-input-container/div[1]/div/tp-yt-paper-input/tp-yt-paper-input-container/div[2]/div/iron-input/input")))
        time_schedule.click()
        action = ActionChains(browser)
        action.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE * 10).perform()
        time_schedule.clear()
        time.sleep(1)
        time_schedule.send_keys(time_add)
        time.sleep(1)
        time_schedule.send_keys(Keys.ENTER)
        time.sleep(1)
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#done-button"))).click()
        WebDriverWait(browser, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#close-button > div"))).click()
    print("Done")