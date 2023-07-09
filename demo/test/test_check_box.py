import pytest
from selenium.common import NoSuchElementException

from demo.data.testing_data import user_data
from demo.pages.page_check_box import PageCheckBox
from demo.pages.page_text_box import PageTextBox


@pytest.mark.usefixtures('chrome')
class TestTextBox:

    def test_expand_folder(self):
        page = PageCheckBox(self.driver)
        page.open()
        page.expand('Home')
        page.expand('Documents')
        page.expand('WorkSpace')
        page.check('Angular')
        page.check('React')
        results = page.get_results()
        pass