# Виталий Сурков, 22-я когорта — Финальный проект. Инженер по тестированию плюс

# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API
import sender_stand_request
# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов
import data

# Функция для позитивной проверки
def positive_assert(track):
    # В переменную order_details сохраняем результат запроса на получение заказа по трек-номеру
    order_details_response = sender_stand_request.get_order_details(track)

    # Проверяем, что код ответа равен 200
    assert order_details_response.status_code == 200


# Тест 1. Успешное получение данных о заказе по треку
def test_receiving_order_by_track_get_success_response():
    # Создаем новый заказ и сохраняем результат запроса в переменную new_order_response
    new_order_response = sender_stand_request.post_new_order()

    # Сохраняем копию параметра запроса track_number из модуля data в переменную current_track
    current_track = data.track_number.copy()

    # Меняем значение параметра t в переменной current_track на трек-номер из созданного заказа
    current_track['t'] = new_order_response.json()["track"]

    # Вызываем функцию positive_assert с изменённой переменной current_track в качестве аргумента
    positive_assert(current_track)