from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PageTextBox:
    URL = 'https://demoqa.com/text-box'

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.field_full_name_loc = By.CSS_SELECTOR, 'input#userName'
        self.field_email_loc = By.CSS_SELECTOR, 'input#userEmail'
        self.area_curr_addr_loc = By.CSS_SELECTOR, 'textarea#currentAddress'
        self.area_perm_addr_loc = By.CSS_SELECTOR, 'textarea#permanentAddress'
        self.button_submit_loc = By.CSS_SELECTOR, 'button#submit'
        self.result_full_name_loc = By.CSS_SELECTOR, 'p#name'
        self.result_email_loc = By.CSS_SELECTOR, 'p#email'
        self.result_curr_addr_loc = By.CSS_SELECTOR, 'p#currentAddress'
        self.result_perm_addr_loc = By.CSS_SELECTOR, 'p#permanentAddress'

    def open(self) -> None:
        self.driver.get(self.URL)

    def set_full_name(self, full_name: str) -> None:
        full_name_field = self.driver.find_element(*self.field_full_name_loc)
        full_name_field.clear()
        full_name_field.send_keys(full_name)

    def set_email(self, email: str) -> None:
        email_field = self.driver.find_element(*self.field_email_loc)
        email_field.clear()
        email_field.send_keys(email)

    def set_curr_addr(self, curr_addr: str) -> None:
        curr_addr_field = self.driver.find_element(*self.area_curr_addr_loc)
        curr_addr_field.clear()
        curr_addr_field.send_keys(curr_addr)

    def set_perm_addr(self, perm_addr: str) -> None:
        curr_addr_field = self.driver.find_element(*self.area_perm_addr_loc)
        curr_addr_field.clear()
        curr_addr_field.send_keys(perm_addr)

    def submit(self):
        submit_button = self.driver.find_element(*self.button_submit_loc)
        action = ActionChains(self.driver).scroll_to_element(submit_button)
        action.perform()
        submit_button.click()

    def get_result_name(self) -> str:
        result_name = self.driver.find_element(*self.result_full_name_loc).text
        return result_name.split(':')[1].strip()

    def get_result_email(self) -> str:
        result_email = self.driver.find_element(*self.result_email_loc).text
        return result_email.split(':')[1].strip()

    def get_email_field_attrib(self, attribute) -> str:
        attrib = self.driver.find_element(*self.field_email_loc).get_attribute(attribute)
        return attrib

    def is_error_in_email_present(self) -> bool:
        is_error_present = 'field-error' in self.get_email_field_attrib('class')
        return is_error_present

    def get_result_curr_addr(self) -> str:
        result_curr_addr = self.driver.find_element(*self.result_curr_addr_loc).text
        return result_curr_addr.split(':')[1].strip()

    def get_result_perm_addr(self) -> str:
        result_perm_addr = self.driver.find_element(*self.result_perm_addr_loc).text
        return result_perm_addr.split(':')[1].strip()