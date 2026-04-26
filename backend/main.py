from user import User
from product import Product, Cart
from storage import Storage
from admin import Admin
from dealer import Dealer


# ---------- FIND PRODUCT ---------- #
def find_product(name):
    for file in ["accessories.json", "clothes.json"]:
        store = Storage(file)
        data = store.load()

        if not isinstance(data, list):
            continue

        for p in data:
            if p["name"].lower() == name.lower() and p["quantity"] > 0:
                return p, file
    return None, None


# ---------- INIT ---------- #
user_system = User()
admin = Admin()

accessories_dealer = Dealer("Accessories", "accessories.json")
clothes_dealer = Dealer("Clothes", "clothes.json")


# ---------- MAIN LOOP ---------- #
while True:
    print("\n==== MAIN MENU ====")
    role = input("Enter role (admin/user/dealer/exit): ").lower()

    # ================= USER ================= #
    if role == "user":
        while True:
            print("\n--- USER MENU ---")
            print("1 Register")
            print("2 Login")
            print("3 Back")

            choice = input("Choice: ")

            if choice == "1":
                u = input("Username: ")
                p = input("Password: ")
                user_system.register(u, p)

            elif choice == "2":
                u = input("Username: ")
                p = input("Password: ")

                if user_system.login(u, p):

                    # ✅ Cart created per user
                    cart = Cart(user_system.current_user)

                    while True:
                        print("\n--- USER DASHBOARD ---")
                        print("1 Add Product")
                        print("2 Remove Product")
                        print("3 View Cart")
                        print("4 Total Price")
                        print("5 Logout")

                        c = input("Choice: ")

                        # ADD
                        if c == "1":
                            name = input("Product name: ")
                            product_data, file = find_product(name)

                            if product_data:
                                product = Product(
                                    product_data["name"],
                                    product_data["price"]
                                )

                                cart.add_product(product)

                                # reduce stock
                                store = Storage(file)
                                data = store.load()

                                for p in data:
                                    if p["name"].lower() == name.lower():
                                        p["quantity"] -= 1
                                        break

                                store.save(data)

                            else:
                                print("Product not available")

                        # REMOVE
                        elif c == "2":
                            name = input("Product name: ")
                            cart.remove_product(name)

                        # VIEW
                        elif c == "3":
                            cart.show_products()

                        # TOTAL
                        elif c == "4":
                            cart.total_price()

                        # LOGOUT
                        elif c == "5":
                            print("Logged out")
                            break

                        else:
                            print("Invalid choice")

            elif choice == "3":
                break

            else:
                print("Invalid choice")

    # ================= ADMIN ================= #
    elif role == "admin":
        while True:
            print("\n--- ADMIN MENU ---")
            print("1 Register")
            print("2 Login")
            print("3 Back")

            choice = input("Choice: ")

            # REGISTER
            if choice == "1":
                u = input("Admin username: ")
                p = input("Password: ")
                print(admin.register(u, p))

            # LOGIN
            elif choice == "2":
                u = input("Admin username: ")
                p = input("Password: ")

                if admin.login(u, p):
                    print("Login successful")

                    while True:
                        print("\n--- ADMIN DASHBOARD ---")
                        print("1 Add Product")
                        print("2 Remove Product")
                        print("3 View Products")
                        print("4 View Users")
                        print("5 Remove User")
                        print("6 Search Product")
                        print("7 Logout")

                        c = input("Choice: ")

                        if c == "1":
                            name = input("Product name: ")
                            price = float(input("Price: "))
                            quantity = int(input("Quantity: "))
                            print(admin.add_product(name, price, quantity))

                        elif c == "2":
                            name = input("Product name: ")
                            print(admin.remove_product(name))

                        elif c == "3":
                            products = admin.view_products()
                            if products:
                                for p in products:
                                    print(p)
                            else:
                                print("No products")

                        elif c == "4":
                            print(admin.view_users())

                        elif c == "5":
                            u = input("Username: ")
                            print(admin.remove_user(u))

                        elif c == "6":
                            name = input("Search name: ")
                            results = admin.search_product(name)

                            if results:
                                for p in results:
                                    print(p)
                            else:
                                print("No matching products")

                        elif c == "7":
                            admin.logout()
                            print("Logged out")
                            break

                        else:
                            print("Invalid choice")

                else:
                    print("Invalid credentials")

            elif choice == "3":
                break

            else:
                print("Invalid choice")

    # ================= DEALER ================= #
    elif role == "dealer":
        print("\n--- SELECT DEALER ---")
        print("1 Accessories")
        print("2 Clothes")

        d = input("Choice: ")

        if d == "1":
            dealer = accessories_dealer
        elif d == "2":
            dealer = clothes_dealer
        else:
            print("Invalid choice")
            continue

        while True:
            print("\n--- DEALER DASHBOARD ---")
            print("1 Add / Update Product")
            print("2 View Products")
            print("3 Back")

            c = input("Choice: ")

            if c == "1":
                name = input("Product name: ")
                price = float(input("Price: "))
                quantity = int(input("Quantity: "))
                dealer.update_product(name, price, quantity)

            elif c == "2":
                dealer.view_product()

            elif c == "3":
                break

            else:
                print("Invalid choice")

    # ================= EXIT ================= #
    elif role == "exit":
        print("Exiting program...")
        break

    else:
        print("Invalid role")