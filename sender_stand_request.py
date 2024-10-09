# Импорт настроек из модуля configuration, который содержит параметры конфигурации, такие как URL сервиса
import configuration

# Импорт библиотеки requests для выполнения HTTP-запросов
import requests

# Импорт данных запроса из модуля data, в котором определены параметры и тело запроса
import data


# Функция post_new_order для отправки POST-запроса на создание нового заказа
def post_new_order():
    # Выполнение POST-запроса с использованием URL из конфигурационного файла, тела запроса и заголовков
    # URL_SERVICE и CREATE_NEW_ORDER объединяются для формирования полного URL для запроса
    # json=data.order_body используется для отправки данных пользователя в формате JSON
     return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER,
                         json=data.order_body)

# Вызов функции post_new_order с телом запроса из модуля data для создания нового заказа
response_new_order = post_new_order()


# Функция get_order_details для отправки GET-запроса для получения заказа по его трек-номеру номеру
def get_order_details():
    # Выполнение GET-запроса с использованием URL из конфигурационного файла и параметра запроса
    # URL_SERVICE и CREATE_NEW_KIT объединяются для формирования полного URL для запроса
    # params=data.track_number используется для запроса данных заказа по его трек-номеру
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_DETAILS,
                        params=data.track_number)

# Вызов функции get_order_details для получения заказа по трек-номеру из модуля data
response_get_order = get_order_details()