import time

import pytest

from demo.pages.page_alerts import PageAlerts


@pytest.mark.usefixtures('firefox')
class TestAlerts:

    def test_just_alert(self):
        page = PageAlerts(self.driver).open()
        alert = page.get_just_alert()
        assert alert.text == 'You clicked a button'
        alert.accept()

    def test_timed_alert(self):
        page = PageAlerts(self.driver).open()
        alert = page.get_timed_alert()
        pass

    def test_confirm_box(self):
        page = PageAlerts(self.driver).open()
        alert = page.get_confirm_box()
        pass

    def test_prompt_box(self):
        text = 'text to prompt box'
        page = PageAlerts(self.driver).open()
        alert = page.get_prompt_box()
        alert.send_keys(text)
        time.sleep(3)
        alert.accept()
        assert text in page.get_prompt_box_result()
        print(page.get_prompt_box_result())