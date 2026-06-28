import uuid


def generate_user():
    suffix = uuid.uuid4().hex[:10]
    return {
        "first_name": "Тест",
        "last_name": "Пользователь",
        "username": f"user_{suffix}",
        "email": f"user_{suffix}@example.com",
        "password": f"Foodgram_{uuid.uuid4().hex[:8]}",
    }
