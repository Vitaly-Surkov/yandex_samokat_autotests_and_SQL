# Виталий Сурков, 22-я когорта — Финальный проект. Инженер по тестированию плюс

# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API
import sender_stand_request

# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов
import data

# Тест 1. Успешное получение данных о заказе по треку
def test_receiving_order_by_track_get_success_response():

    # В переменную new_order сохраняем результат запроса для создания нового заказа
    new_order = sender_stand_request.post_new_order()

    # В переменную track_number сохраняем номер трека из модуля data
    track_number = data.track_number
    # Меняем значение в переменной track_number на трек-номер из созданного заказа
    track_number['t'] = new_order.json()["track"]

    # В переменную order_details сохраняем результат запроса на получение заказа по треку
    order_details = sender_stand_request.get_order_details()

    # Проверяем, что код ответа равен 200
    assert order_details.status_code == 200