#Куртмулаева Динара, земля 8а, диплом
import configuration
import data
import requests

# 1.Выполнить запрос на создание заказа.
def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH)

# 2.Сохранить номер трека заказа.
def get_track_number():
    data.order_body.copy()
    new_order = post_new_order()
    return new_order.json()['track']

# 3.Выполнить запрос на получения заказа по треку заказа.
def get_info():
    track: object = get_track_number()
    params_track = {"t": track}
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH, params=params_track)