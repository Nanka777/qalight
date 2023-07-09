import pytest

from lecture_selenium.pages.page_text_box import PageTextBox


user_data = {'fullname': 'Vasya Pupkin',
             'email': 'pupkin@1.com',
             'curr_addr': 'My current address',
             'perm_addr': 'My perm address'}
@pytest.mark.usefixtures('chrome')
class TestTextBox:

    def test_full_name(self, chrome):
        page = PageTextBox(chrome)
        page.open().set_full_name(user_data.get('fullname'))
        page.submit()
        name = page.get_full_name()
        assert name == user_data['fullname']

    def test_email_positive(self):
        pass

    def test_email_negative(self):
        pass

    def test_curr_addr(self):
        pass

    def test_perm_addr(self):
        pass

    def test_full_form_positive(self):
        pass

    def test_full_form_negative(self):
        pass