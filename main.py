from classes.Menu_items import Menu,MenuItem
from classes.Create_Staff import Chef,Waiter
from  classes.Restaurant_Manager import Restaurant
from classes.Customers_and_Orders import Customer
if __name__ == "__main__":
    print(" Welcome to Restaurant Manager Game!")

    name = input("Enter restaurant name: ")
    menu = Menu()


    menu.add_item(MenuItem("Pizza", 40, "main"))
    menu.add_item(MenuItem("Pasta", 35, "main"))
    menu.add_item(MenuItem("Cola", 10, "drink"))
    menu.add_item(MenuItem("Salad", 20, "appetizer"))
    menu.add_item(MenuItem("Cake", 25, "dessert"))

    restaurant = Restaurant(name, menu)
    chef = Chef("Gorden", 300, "UK")
    waiter = Waiter("Lolo", 200)
    restaurant.hire_staff(chef)
    restaurant.hire_staff(waiter)


    customer = Customer("Yaakov")
    order = restaurant.create_order(customer)

    menu.display_menu()
    order.add_item(menu.get_item_by_name("Pizza"))
    order.add_item(menu.get_item_by_name("Cola"))
    order.display_order()


    restaurant.process_order(order)
    restaurant.complete_order(order)

    restaurant.display_status()
    restaurant.pay_salaries()