##а) тест клікає Yes та перевіряє результат (знизу)
#б) тест вмикає та клікає "No" та перевіряє результат (is_selected)
#в) Тест збирає інфу по всіх радіо-буттонах на сторінці і складає в словник (приклад у відео уроку)


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://demoqa.com/radio-button")

yes_button = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
yes_button.click()

result = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//p[@class='text-success']"))
).text

assert result == "You have selected Yes"

no_button = driver.find_element(By.XPATH, "//label[@for='noRadio']")
no_button.click()

is_selected = no_button.is_selected()

assert is_selected

radio_buttons = driver.find_elements(By.XPATH, "//input[@type='radio']")
radio_button_info = {}

for button in radio_buttons:
    button_id = button.get_attribute("id")
    button_value = button.get_attribute("value")
    button_selected = button.is_selected()
    radio_button_info[button_id] = {"value": button_value, "selected": button_selected}

print(radio_button_info)