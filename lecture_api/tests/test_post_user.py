from lecture_api.pages.page_book_store_users import PageBookUsers
class TestCreateUser:

    user_id = None

    def test_create_user(self):
        page = PageBookUsers()
        user = page.create_user('Vasua1', 'P@sswOrd')
        self.user_id = user.get('id')

    def test_delete_user(self):
        page = PageBookUsers()
        page.CUSTOM_USER_ENDPOINT = page.CUSTOM_USER_ENDPOINT.format(id_)
        page.deleter_user()