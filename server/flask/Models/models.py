import random
class Order():
    def __init__(self, user_id, order_id, purchased_list=[]):
        self.order_id = order_id
        self.user_id = user_id
        self.price = 0
        self.purchased_list = purchased_list
        self.order_status = False
    # return a total price of the order
    def getPrice(self):
        self.price = 0
        for item in purchased_list:
            self.price += item['price']
        return self.price
    # get a purchased map by putting all the same products togethor.
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
    # end a order, when a customer get his food.
    def finishOrder(self):
        self.order_status = True
    # create dict data dor database.
    def _dictData(self):
        nor_data = {
            'id': self.order_id,
            'user_id': self.user_id,
            'price': self.price,
            'purchased': self.purchased_list,
            'status': self.order_status
        }
        return nor_data

class OrderLine():
    def __init__(self, order_list):
        self.orders = order_list[:]

    # def __str__(self):
    #     active_orders = self.orders[:]
    #     for order in self.orders:
    #         print("order in order_line", order)
    #         if order['order_status'] == False:
    #             active_orders.append(order)
    #
    #     active_orders.sort(key = lambda x: x['price'])
    #     self.orders = active_orders
    #     return self.orders

    def push(self, item):
        self.orders.append(item)
        return item
    def _dictData(self):
        active_orders = []
        for order in self.orders:
            print("order in order_line", order)
            if order['status'] == False:
                active_orders.append(order)

        active_orders.sort(key = lambda x: x['price'])
        self.orders = active_orders
        return self.orders

class Customer():
    def __init__(self, user_id, user_name, user_image):
        self.user_id = user_id
        self.user_name = user_name
        self.user_image = user_image
        self.order_list = []
    def createOrder(self, purchased_list, order_id):
        order = Order(self.user_id, purchased_list, order_id)
        return order

    def dbData(self):
        nor_data = {
            'id': self.user_id,
            'username': self.user_name,
            'user_image': self.price,
        }
        return nor_data
