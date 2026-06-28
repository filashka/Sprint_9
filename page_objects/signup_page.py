import allure

from data.urls import SIGNUP_PATH
from locators.locators import SignUpPageLocators
from page_objects.base_page import BasePage


class SignUpPage(BasePage):
    @allure.step("Открыть страницу регистрации")
    def open_signup(self):
        self.open(SIGNUP_PATH)

    @allure.step("Заполнить и отправить форму регистрации")
    def register(self, user):
        self._type(SignUpPageLocators.FIRST_NAME, user["first_name"])
        self._type(SignUpPageLocators.LAST_NAME, user["last_name"])
        self._type(SignUpPageLocators.USERNAME, user["username"])
        self._type(SignUpPageLocators.EMAIL, user["email"])
        self._type(SignUpPageLocators.PASSWORD, user["password"])
        self._click(SignUpPageLocators.SUBMIT)
