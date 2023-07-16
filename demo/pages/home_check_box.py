from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://demoqa.com/checkbox")

def expand_folders(folder_names):
    for folder_name in folder_names:
        folder_locator = (By.XPATH, f"//span[text()='{folder_name}']/preceding-sibling::span")
        folder_icon = driver.find_element(*folder_locator)
        folder_icon.click()

def check_checkboxes(checkbox_names):
    for checkbox_name in checkbox_names:
        checkbox_locator = (By.XPATH, f"//span[text()='{checkbox_name}']/preceding-sibling::input[@type='checkbox']")
        checkbox = driver.find_element(*checkbox_locator)
        checkbox.click()

folders_to_expand = ["Home", "Documents", "Office"]
checkboxes_to_check = ["Public", "Private"]

expand_folders(folders_to_expand)
check_checkboxes(checkboxes_to_check)