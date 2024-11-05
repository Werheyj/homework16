from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def main() -> dict:
    return {'message': 'Главная страница'}


@app.get('/user/admin')
async def admin() -> dict:
    return {'message_admin': 'Вы вошли как администратор'}


@app.get('/user/{user_id}')
async def number_id(user_id: int) -> dict:
    return {'message_user_id': f'Вы вошли как пользователь № {user_id}'}


@app.get('/user')
async def user(username: str, age: int) -> dict:
    return {'message_user': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}
