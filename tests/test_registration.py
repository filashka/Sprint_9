import allure


@allure.feature("Создание аккаунта")
class TestRegistration:
    @allure.title("Регистрация нового аккаунта открывает страницу авторизации")
    def test_create_account(self, main_page, signup_page, signin_page, new_user):
        main_page.open_main()
        main_page.go_to_signup()
        signup_page.register(new_user)
        assert signin_page.is_opened(), (
            "Форма авторизации не отобразилась после регистрации"
        )
        assert "/signin" in signin_page.current_url
