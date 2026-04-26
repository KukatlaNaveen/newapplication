from storage import Storage

class Admin:
    def __init__(self):
        self.admin_storage = Storage("admin.json")
        self.admin = self.admin_storage.load()

        if not isinstance(self.admin, dict):
            self.admin = {}

        self.is_logged_in = False

        self.product_storage = Storage("products.json")
        self.products = self.product_storage.load()
        if not isinstance(self.products, list):
            self.products = []

        self.user_storage = Storage("users.json")

    # -------- AUTH -------- #
    def register(self, username, password):
        if self.admin:
            return "Admin already exists"

        self.admin["username"] = username
        self.admin["password"] = password
        self.admin_storage.save(self.admin)
        return "Admin registered"

    def login(self, username, password):
        if (
            self.admin.get("username") == username
            and self.admin.get("password") == password
        ):
            self.is_logged_in = True
            return True
        return False

    def logout(self):
        self.is_logged_in = False

    # -------- PRODUCTS -------- #
    def add_product(self, name, price, quantity):
        if not self.is_logged_in:
            return "Login required"

        for p in self.products:
            if p["name"].lower() == name.lower():
                p["quantity"] += quantity
                p["price"] = price
                self.product_storage.save(self.products)
                return "Stock updated"

        self.products.append({
            "name": name,
            "price": price,
            "quantity": quantity
        })

        self.product_storage.save(self.products)
        return "Product added"

    def remove_product(self, name):
        for p in self.products:
            if p["name"].lower() == name.lower():
                self.products.remove(p)
                self.product_storage.save(self.products)
                return "Removed"
        return "Not found"

    def view_products(self):
        return self.products

    # -------- USERS -------- #
    def view_users(self):
        users = self.user_storage.load()
        return list(users.keys())

    def remove_user(self, username):
        users = self.user_storage.load()

        if username in users:
            del users[username]
            self.user_storage.save(users)
            return "User removed"

        return "User not found"

    def search_product(self, name):
        result = []
        for p in self.products:
            if name.lower() in p["name"].lower():
                result.append(p)
        return result