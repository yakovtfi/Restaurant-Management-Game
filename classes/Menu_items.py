class MenuItem:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        self.available = True

    def get_info(self):
        return f"{self.name} - {self.price}₪ ({self.category})"

    def set_available(self, status):
        self.available = status

    def is_available(self):
        return self.available


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, menu_item):
        self.items.append(menu_item)

    def remove_item(self, item_name):
        self.items = [item for item in self.items if item.name != item_name]

    def get_item_by_name(self, name):
        for item in self.items:
            if item.name == name:
                return item
        return None

    def get_items_by_category(self, category):
        return [item for item in self.items if item.category == category]

    def display_menu(self):
        print("\n--- MENU ---")
        for item in self.items:
            if item.is_available():
                print(item.get_info())


    def get_total_items(self):
        return len(self.items)
