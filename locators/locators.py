from selenium.webdriver.common.by import By


class MainPageLocators:
    SIGNUP_LINK = (By.CSS_SELECTOR, "a[href='/signup']")
    SIGNIN_LINK = (By.CSS_SELECTOR, "a[href='/signin']")
    CREATE_RECIPE_LINK = (By.CSS_SELECTOR, "a[href='/recipes/create']")
    LOGOUT_LINK = (By.XPATH, "//a[normalize-space(text())='Выход']")


class SignUpPageLocators:
    FIRST_NAME = (By.NAME, "first_name")
    LAST_NAME = (By.NAME, "last_name")
    USERNAME = (By.NAME, "username")
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    SUBMIT = (By.XPATH, "//button[contains(., 'Создать аккаунт')]")


class SignInPageLocators:
    LOGIN = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    SUBMIT = (By.XPATH, "//button[contains(., 'Войти')]")


class RecipeCreatePageLocators:
    NAME = (
        By.XPATH,
        "//label[div[contains(normalize-space(), 'Название рецепта')]]//input",
    )
    INGREDIENT_SEARCH = (
        By.XPATH,
        "//label[div[contains(normalize-space(), 'Ингредиенты')]]//input",
    )
    INGREDIENT_AMOUNT = (
        By.XPATH,
        "//label[div[contains(normalize-space(), 'Ингредиенты')]]/following::input[1]",
    )
    ADD_INGREDIENT = (By.XPATH, "//div[normalize-space(text())='Добавить ингредиент']")
    COOKING_TIME = (
        By.XPATH,
        "//label[div[contains(normalize-space(), 'Время приготовления')]]//input",
    )
    DESCRIPTION = (
        By.XPATH,
        "//label[div[contains(normalize-space(), 'Описание рецепта')]]//textarea",
    )
    IMAGE_INPUT = (By.XPATH, "//input[@type='file']")
    SUBMIT = (By.XPATH, "//button[contains(., 'Создать рецепт')]")

    @staticmethod
    def ingredient_option(query):
        """Autocomplete option whose text exactly equals the typed query."""
        return (By.XPATH, f"//div[normalize-space(text())='{query}']")


class RecipePageLocators:
    TITLE = (By.XPATH, "//h1[contains(@class, 'single-card__title')]")

    @staticmethod
    def title_by_name(name):
        return (By.XPATH, f"//h1[contains(normalize-space(), '{name}')]")
