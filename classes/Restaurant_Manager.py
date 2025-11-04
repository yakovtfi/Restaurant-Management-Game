from classes.Customers_and_Orders import Order


class Restaurant:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu
        self.staff = []
        self.orders = []
        self.money = 1000
        self.order_counter = 1

    def hire_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"{staff_member.name} hired!")

    def fire_staff(self, staff_name):
        self.staff = [s for s in self.staff if s.name != staff_name]
        print(f"{staff_name} has been fired.")

    def create_order(self, customer):
        order = Order(customer, self.order_counter)
        self.order_counter += 1
        self.orders.append(order)
        return order

    def process_order(self, order):
        chef = next((s for s in self.staff if s.__class__.__name__ == "Chef"), None)
        waiter = next((s for s in self.staff if s.__class__.__name__ == "Waiter"), None)
        if chef:
            chef.cook_order(order)
        if waiter:
            waiter.serve_order(order)

    def complete_order(self, order):
        self.money += order.get_total()
        self.orders.remove(order)
        print(f"Order #{order.order_number} completed! +{order.get_total()}")

    def pay_salaries(self):
        total_salaries = sum(s.salary for s in self.staff)
        self.money -= total_salaries
        print(f"Paid salaries: {total_salaries}₪")

    def get_statistics(self):
        return {
            "total_orders": len(self.orders),
            "money": self.money,
            "staff_count": len(self.staff)
        }

    def display_status(self):
        print(f"\n {self.name} STATUS")
        print(f"Money: {self.money} | Orders: {len(self.orders)} | Staff: {len(self.staff)}")