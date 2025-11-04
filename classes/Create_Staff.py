class Staff:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.energy = 100

    def work(self):
        self.energy = max(0, self.energy - 10)
        print(f"{self.name} is working... Energy: {self.energy}")

    def rest(self):
        self.energy = min(100, self.energy + 20)
        print(f"{self.name} is resting. Energy: {self.energy}")

    def is_tired(self):
        return self.energy < 30

    def get_info(self):
        return f"{self.name} | Salary: {self.salary}₪ | Energy: {self.energy}"


class Chef(Staff):
    def __init__(self, name, salary, specialty):
        super().__init__(name, salary)
        self.specialty = specialty

    def cook_order(self, order):
        if self.energy >= 15:
            self.energy -= 15
            order.set_status("cooking")
            print(f"{self.name} is cooking order #{order.order_number}...")
            order.set_status("ready")
            print(f"Order #{order.order_number} is ready!")
        else:
            print(f"{self.name} is too tired to cook.")

    def work(self):
        self.energy = max(0, self.energy - 15)
        print(f"{self.name} cooked a dish. Energy: {self.energy}")


class Waiter(Staff):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.tips = 0

    def serve_order(self, order):
        order.set_status("delivered")
        print(f"{self.name} served order #{order.order_number} to {order.customer.name}!")
        if order.customer.is_happy():
            self.receive_tip(20)

    def receive_tip(self, amount):
        self.tips += amount
        print(f"{self.name} received a tip of {amount}! Total tips: {self.tips}")

    def get_total_earnings(self):
        return self.salary + self.tips