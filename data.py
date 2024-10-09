# Данные заказчика для создания нового заказа в системе содержат имя, фамилию,
# адрес, станцию метро, телефон, срок аренды, дату доставки, комментарий и цвет самоката
order_body = {
    "firstName": "Иван", # Имя заказчика
    "lastName": "Иванов", # Фамилия заказчика
    "address": "Случайная, 11", # Адрес заказчика
    "metroStation": 26, # Ближайшая станция метро
    "phone": "+78003553535", # Телефон заказчика
    "rentTime": 2, # Срок аренды самоката
    "deliveryDate": "2025-01-01", # Дата доставки самоката
    "comment": "Хочу самокат", # Комментарий заказчика
    "color": [ # Цвет самоката
        "BLACK"
    ]
}

# Параметры для получения заказа по номеру трекера
track_number = {
        "t":123456 # Трекинговый номер заказа
    }