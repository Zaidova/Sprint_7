from datetime import datetime, timedelta

ERROR_LOGIN_DUPLICATE = "Этот логин уже используется. Попробуйте другой."
ERROR_MISSING_FIELDS_CREATE_COURIER = "Недостаточно данных для создания учетной записи"
ERROR_MISSING_FIELDS_LOG_IN_COURIER = "Недостаточно данных для входа"
ERROR_NOT_FOUND = "Учетная запись не найдена"

ORDER_PAYLOAD = {
    "firstName": "Иван",
    "lastName": "Иванов",
    "address": "Ленина 14",
    "metroStation": "1",
    "phone": "+79991112233",
    "rentTime": 2,
    "deliveryDate": datetime.now()  + timedelta(days=1),
    "comment": "Коммент",
}