from storage import Storage

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self, username):
        self.username = username
        self.store = Storage("cart.json")

        data = self.store.load()
        if not isinstance(data, dict):
            data = {}

        self.data = data

        if self.username not in self.data:
            self.data[self.username] = []

    def add_product(self, product):
        cart = self.data[self.username]

        for item in cart:
            if item["name"] == product.name:
                item["quantity"] += 1
                self.store.save(self.data)
                print("Quantity updated")
                return

        cart.append({
            "name": product.name,
            "price": product.price,
            "quantity": 1
        })

        self.store.save(self.data)
        print("Added to cart")

    def remove_product(self, name):
        cart = self.data[self.username]

        for item in cart:
            if item["name"].lower() == name.lower():
                cart.remove(item)
                self.store.save(self.data)
                print("Removed")
                return

        print("Not found")

    def show_products(self):
        cart = self.data.get(self.username, [])

        if not cart:
            print("Cart empty")
            return

        for item in cart:
            print(f"{item['name']} | Price: {item['price']} | Qty: {item['quantity']}")

    def total_price(self):
        cart = self.data.get(self.username, [])
        total = sum(item["price"] * item["quantity"] for item in cart)

        print("Total:", total)

        if total > 1000:
            total *= 0.9
            print("After discount:", total)