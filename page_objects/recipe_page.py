import allure

from locators.locators import RecipePageLocators
from page_objects.base_page import BasePage


class RecipePage(BasePage):
    @allure.step("Проверить, что карточка созданного рецепта отображается")
    def is_recipe_displayed(self, name):
        return self.is_visible(RecipePageLocators.title_by_name(name))

    @allure.step("Получить название рецепта")
    def get_title(self):
        return self._get_text(RecipePageLocators.TITLE)
