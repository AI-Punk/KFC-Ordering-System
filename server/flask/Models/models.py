import random
class Order():
    def __init__(self, username, purchased_list=[], order_id):
        self.order_id = order_id
        self.username = username
        self.price = 0
        self.purchased_list = purchased_list
        self.order_status = False

    def getPrice(self):
        self.price = 0
        for item in purchased_list:
            self.price += item['price']
        return self.price

    def getPurchasedMap(self):
        purchased_map = {}
        for item in purchased_list:
            # if purchased_map.get(item['name']) == False:
            #     purchased_map[item['name']] = item['price']
            # else:
            #     purchased_map[item['name']] += item['price']
            if purchased_map.get(item['name']) == False:
                purchased_map[item['name']] = 0
            purchased_map[item['name']] += item['price']
        return purchased_map

    def finishOrder(self):
        self.order_status = True
        
class OrderLine():
    def __init__(self, order_list):
        self.orders = order_list[:]
    def __str__(self):
        active_orders = self.orders[:]
        for order in self.orders:
            if order['order_status'] == False:
                active_orders.append()

        active_orders.sort(key = lambda x: x['price'])
        self.orders = active_orders
        return self.orders

class Customer():
    def __init__(self, user_id, user_name, user_image):
        self.user_id = user_id
        self.user_name = user_name
        self.user_image = user_image
        self.order_list = []
    def createOrder(self):
        order = Order(self.id, )
