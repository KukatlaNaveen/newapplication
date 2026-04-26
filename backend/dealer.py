from storage import Storage

class Dealer:
    def __init__(self, name, filename):
        self.name = name
        self.store = Storage(filename)

    def get_product(self):
        data = self.store.load()
        if not isinstance(data, list):
            return []
        return data

    def update_product(self, name, price, quantity):
        data = self.get_product()

        # update dealer file
        for p in data:
            if p["name"].lower() == name.lower():
                p["price"] = price
                p["quantity"] += quantity
                self.store.save(data)
                print("Stock updated")
                break
        else:
            data.append({
                "name": name,
                "price": price,
                "quantity": quantity
            })
            self.store.save(data)
            print("Product added")

        # also update main product file
        main_store = Storage("products.json")
        products = main_store.load()

        if not isinstance(products, list):
            products = []

        for p in products:
            if p["name"].lower() == name.lower():
                p["price"] = price
                p["quantity"] += quantity
                main_store.save(products)
                return

        products.append({
            "name": name,
            "price": price,
            "quantity": quantity
        })
        main_store.save(products)

    def view_product(self):
        data = self.get_product()
        if not data:
            print("No products")
            return

        for p in data:
            print(f"{p['name']} | Price: {p['price']} | Qty: {p['quantity']}")