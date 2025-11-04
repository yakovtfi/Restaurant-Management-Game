class Customer:
    def __init__(self,name:str):
        self.name = name
        self.satisfaction = 50

    def  increase_satisfaction(self, amount:int):
        self.satisfaction += amount

    def decrease_satisfaction(self, amount:int):
        self.satisfaction -= amount

    def  is_happy(self):
        return self.satisfaction > 70

    def  get_info(self):
        return f"Customer: {self.name}, Satisfaction: {self.satisfaction}"


class Order:
    def __init__(self, customer, order_number):
        self.customer = customer
        self.order_number = order_number
        self.items = []
        self.status = "pending"
        self.total_price = 0

    def add_item(self, menu_item):
        if menu_item.is_available():
            self.items.append(menu_item)
            self.total_price += menu_item.price
        else:
            print(f"{menu_item.name} is not available.")

    def remove_item(self, menu_item):
        if menu_item in self.items:
            self.items.remove(menu_item)
            self.total_price -= menu_item.price

    def get_total(self):
        return self.total_price

    def set_status(self, new_status):
        self.status = new_status

    def display_order(self):
        print(f"\nOrder #{self.order_number} - {self.customer.name}")
        for item in self.items:
            print(f" - {item.get_info()}")
        print(f"Total: {self.total_price} | Status: {self.status}")

    def is_complete(self):
        return self.status == "delivered"