import allure

from data.urls import SIGNIN_PATH
from locators.locators import SignInPageLocators
from page_objects.base_page import BasePage


class SignInPage(BasePage):
    @allure.step("Открыть страницу авторизации")
    def open_signin(self):
        self.open(SIGNIN_PATH)

    @allure.step("Авторизоваться по имени пользователя (логину)")
    def login(self, username, password):
        # Bug: authorization by email is broken — log in with the username.
        self._type(SignInPageLocators.LOGIN, username)
        self._type(SignInPageLocators.PASSWORD, password)
        self._click(SignInPageLocators.SUBMIT)

    @allure.step("Проверить, что форма авторизации отображается")
    def is_opened(self):
        return self.is_visible(SignInPageLocators.SUBMIT)
