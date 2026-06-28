import allure


@allure.feature("Авторизация")
class TestAuthorization:
    @allure.title("Авторизация по логину открывает главную страницу")
    def test_login_with_username(self, registered_user, signin_page, main_page):
        signin_page.open_signin()
        signin_page.login(registered_user["username"], registered_user["password"])
        assert main_page.is_logout_displayed(), (
            "Кнопка Выход не отображается — вход не выполнен"
        )
        assert "/recipes" in main_page.current_url
