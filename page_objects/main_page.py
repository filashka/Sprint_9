import allure

from data.urls import MAIN_PATH
from locators.locators import MainPageLocators
from page_objects.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Открыть главную страницу")
    def open_main(self):
        self.open(MAIN_PATH)

    @allure.step("Перейти на страницу регистрации")
    def go_to_signup(self):
        self._click(MainPageLocators.SIGNUP_LINK)

    @allure.step("Перейти на страницу авторизации")
    def go_to_signin(self):
        self._click(MainPageLocators.SIGNIN_LINK)

    @allure.step("Открыть вкладку Создать рецепт")
    def go_to_create_recipe(self):
        self._click(MainPageLocators.CREATE_RECIPE_LINK)

    @allure.step("Проверить, что кнопка Выход отображается")
    def is_logout_displayed(self):
        return self.is_visible(MainPageLocators.LOGOUT_LINK)
