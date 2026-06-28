# Sprint_9 — автотесты Foodgram (Продуктовый помощник)

UI-автотесты на Selenium для сервиса
[foodgram-frontend](https://foodgram-frontend-1.foodgram.education-services.ru/).
Покрыты три функциональности: создание аккаунта, авторизация и создание рецепта.
Тесты построены по паттерну Page Object, отчётность — Allure, запуск — локально
(Chrome) или в Selenoid через `docker-compose`, CI/CD — GitHub Actions.

## ⚠️ Особенность: вход по логину

На этом стенде **авторизация по email не работает** (баг). Поэтому в тестах вход
выполняется по **username (логину)**: значение логина вводится в поле формы входа,
email для авторизации не используется. Тестовый пользователь хранит и `username`,
и `email`, но `SignInPage.login()` отправляет именно `username`.

## Структура проекта

```
page_objects/      # пакет Page Object — по классу на страницу
  base_page.py     #   базовые обёртки над драйвером (только явные ожидания)
  main_page.py     #   шапка/навигация, кнопка Выход
  signup_page.py   #   форма регистрации
  signin_page.py   #   форма авторизации
  recipe_create_page.py
  recipe_page.py   #   страница созданного рецепта
locators/
  locators.py      # ВСЕ локаторы (в тестах и пейджах локаторов нет)
data/
  users.py         # генерация уникальных пользователей
  recipes.py       # данные рецепта + путь к картинке (pathlib)
  urls.py          # базовый URL и пути страниц
conftest.py        # фикстуры: драйвер, пейджи, предусловия
tests/
  test_registration.py     # класс TestRegistration
  test_authorization.py    # класс TestAuthorization
  test_recipe_creation.py  # класс TestRecipeCreation
assets/test_image.png      # фото для загрузки рецепта
config/browsers.json       # конфигурация браузеров Selenoid
Dockerfile  docker-compose.yml  .github/workflows/ci.yml
allure-report/             # сгенерированный отчёт
```

## Установка библиотек

```bash
pip install -r requirements.txt
```

## Запуск локально (Chrome)


```bash
pytest                 # обычный режим
pytest --headless      # без окна браузера
```


## Запуск в Selenoid (docker-compose)

```bash
docker compose up --build --abort-on-container-exit --exit-code-from tests
```

Поднимается Selenoid с образом `selenoid/chrome:128.0`, тесты идут через
`webdriver.Remote` (`--selenoid-uri=http://selenoid:4444/wd/hub`). Результаты
Allure складываются в `./allure-results`.

## Отчёт Allure

```bash
# быстрый просмотр
allure serve allure-results

# сгенерировать статический отчёт (его и пушим в репозиторий)
allure generate allure-results -o allure-report --clean
```
