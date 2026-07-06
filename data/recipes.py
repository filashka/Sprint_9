import uuid
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = APP_DIR / "assets"
RECIPE_IMAGE = ASSETS_DIR / "test_image.png"


def generate_recipe():
    suffix = uuid.uuid4().hex[:8]
    return {
        "name": f"Тестовый рецепт {suffix}",
        "description": "Описание тестового рецепта, создано автотестом.",
        "cooking_time": "15",
        # common ingredient — guaranteed to return autocomplete results
        "ingredient_query": "соль",
        "amount": "5",
        # absolute path string required by send_keys()
        "image": str(RECIPE_IMAGE),
    }
