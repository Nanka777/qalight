import pytest
from selenium.common import NoSuchElementException

from demo.data.testing_data import user_data
from demo.pages.page_text_box import PageTextBox


@pytest.mark.usefixtures('chrome')
class TestTextBox:

    def test_full_name(self):
        page_text_box = PageTextBox(self.driver)
        page_text_box.open()
        page_text_box.set_full_name(user_data.get('full_name'))
        page_text_box.submit()
        assert user_data.get('full_name') == page_text_box.get_result_name()

    def test_email_valid(self):
        page_text_box = PageTextBox(self.driver)
        page_text_box.open()
        page_text_box.set_email(user_data.get('email_correct'))
        page_text_box.submit()
        assert user_data.get('email_correct') == page_text_box.get_result_email()

    def test_email_invalid(self):
        page_text_box = PageTextBox(self.driver)
        page_text_box.open()
        page_text_box.set_email(user_data.get('email_incorrect'))
        page_text_box.submit()
        is_error_present = page_text_box.is_error_in_email_present()
        with pytest.raises(NoSuchElementException):
            page_text_box.get_result_email()
        assert is_error_present

    def test_curr_addr(self):
        page_text_box = PageTextBox(self.driver)
        page_text_box.open()
        page_text_box.set_curr_addr(user_data.get('curr_addr'))
        page_text_box.submit()
        assert user_data.get('curr_addr') == page_text_box.get_result_curr_addr()

    def test_perm_addr(self):
        page_text_box = PageTextBox(self.driver)
        page_text_box.open()
        page_text_box.set_perm_addr(user_data.get('perm_addr'))
        page_text_box.submit()
        assert user_data.get('perm_addr') == page_text_box.get_result_perm_addr()