import allure

from data.urls import CREATE_RECIPE_PATH
from locators.locators import RecipeCreatePageLocators as Loc
from page_objects.base_page import BasePage


class RecipeCreatePage(BasePage):
    @allure.step("Открыть страницу создания рецепта")
    def open_create(self):
        self.open(CREATE_RECIPE_PATH)

    @allure.step("Добавить ингредиент из списка автодополнения")
    def add_ingredient(self, query, amount):
        self._type(Loc.INGREDIENT_SEARCH, query)
        self._click(Loc.ingredient_option(query))
        self._type(Loc.INGREDIENT_AMOUNT, amount)
        self._click(Loc.ADD_INGREDIENT)

    @allure.step("Загрузить фото рецепта")
    def upload_image(self, image_path):
        self._find(Loc.IMAGE_INPUT).send_keys(image_path)

    @allure.step("Заполнить форму рецепта и отправить")
    def create_recipe(self, recipe):
        self._type(Loc.NAME, recipe["name"])
        self.add_ingredient(recipe["ingredient_query"], recipe["amount"])
        self._type(Loc.COOKING_TIME, recipe["cooking_time"])
        self._type(Loc.DESCRIPTION, recipe["description"])
        self.upload_image(recipe["image"])
        self._click(Loc.SUBMIT)
