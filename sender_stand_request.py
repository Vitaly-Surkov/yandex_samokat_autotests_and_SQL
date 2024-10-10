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


# Функция get_order_details для отправки GET-запроса на получение заказа по его трек-номеру
def get_order_details(track):
    # Выполнение GET-запроса с использованием URL из конфигурационного файла и параметра запроса
    # URL_SERVICE и GET_ORDER_DETAILS объединяются для формирования полного URL для запроса
    # params=track используется для запроса данных заказа по его трек-номеру
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_DETAILS,
                        params=track)