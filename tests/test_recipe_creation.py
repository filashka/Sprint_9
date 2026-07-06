import allure

from data.recipes import generate_recipe


@allure.feature("Создание рецепта")
class TestRecipeCreation:
    @allure.title("Создание рецепта отображает карточку с введённым названием")
    def test_create_recipe(
        self, authorized_user, main_page, recipe_create_page, recipe_page
    ):
        new_recipe = generate_recipe()
        main_page.go_to_create_recipe()
        recipe_create_page.create_recipe(new_recipe)
        assert recipe_page.is_recipe_displayed(new_recipe["name"]), (
            "Карточка созданного рецепта не отображается"
        )
        assert recipe_page.get_title() == new_recipe["name"]
