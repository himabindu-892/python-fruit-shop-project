fruits = ["Apple","Banana","Mango","Grape","Orange"]
prices = [100,50,200,60,90]
quantities = [10,20,15,13,30]
cart = []
cart_prices = []
cart_quantities = []
def view_fruits():
    print("Available Fruits:")
    for i in range(len(fruits)):
        print(f"{i+1}. {fruits[i]} - Rs.{prices[i]} per kg ({quantities[i]} kgs available)")

def add_to_cart():
    view_fruits()
    choice = int(input("Enter the fruit number to add to cart: ")) - 1
    if choice >= 0 and choice < len(fruits):
        quantity = int(input("Enter quantity (in kgs) to add to cart: "))
        if quantity <= quantities[choice]:
            cart.append(fruits[choice])
            cart_prices.append(prices[choice])
            cart_quantities.append(quantity)
            quantities[choice] -= quantity
            print(f"{quantity} kgs of {fruits[choice]} added to cart.")
        else:
            print("Out of stock.")
    else:
        print("Invalid choice.")

def remove_from_cart():
    if not cart:
        print("Your cart is empty.")
        return
    print("Your Cart:")
    for i in range(len(cart)):
        print(f"{i+1}. {cart[i]} - Rs.{cart_prices[i]} per kg ({cart_quantities[i]} kgs)")
    choice = int(input("Enter the fruit number to remove from cart: ")) - 1
    if choice >= 0 and choice < len(cart):
        quantities[fruits.index(cart[choice])] += cart_quantities[choice]
        del cart[choice]
        del cart_prices[choice]
        del cart_quantities[choice]
        print("Fruit removed from cart.")
    else:
        print("Invalid choice.")

def view_cart():
    if not cart:
        print("Your cart is empty.")
        return
    print("Your Cart:")
    total = 0
    for i in range(len(cart)):
        print(f"{i+1}. {cart[i]} - Rs.{cart_prices[i]} per kg ({cart_quantities[i]} kgs) = Rs.{cart_prices[i] * cart_quantities[i]}")
        total += cart_prices[i] * cart_quantities[i]
    print(f"Total: Rs.{total}")
def buy_now():
    if not cart:
        print("Your cart is empty.")
        return
    address = input("Enter your address: ")
    print("Order placed successfully. Thanks for shopping!")
    view_cart()
    print(f"Delivery Address: {address}")
    cart.clear()
    cart_prices.clear()
    cart_quantities.clear()
def shopkeeper():
    while True:
        print("1. Add Fruit")
        print("2. Remove Fruit")
        print("3. Update Price")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            fruit_name = input("Enter fruit name: ")
            price = int(input("Enter price per kg: "))
            quantity = int(input("Enter quantity (in kgs): "))
            fruits.append(fruit_name)
            prices.append(price)
            quantities.append(quantity)
            print(f"{fruit_name} added successfully.")
        elif choice == "2":
            view_fruits()
            choice = int(input("Enter the fruit number to remove: ")) - 1
            if choice >= 0 and choice < len(fruits):
                del fruits[choice]
                del prices[choice]
                del quantities[choice]
                print("Fruit removed successfully.")
            else:
                print("Invalid choice.")
        elif choice == "3":
            view_fruits()
            choice = int(input("Enter the fruit number to update price: ")) - 1
            if choice >= 0 and choice < len(fruits):
                price = int(input("Enter new price per kg: "))
                prices[choice] = price
                print("Price updated successfully.")
            else:
                print("Invalid choice.")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
def customer():
    while True:
        print("1. View Fruits")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Buy Now")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            view_fruits()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            remove_from_cart()
        elif choice == "4":
            view_cart()
        elif choice == "5":
            buy_now()
        elif choice == "6":
            print("Thanks for shopping with Us")
            break
        else:
            print("Invalid choice. Please try again.")
def main():
    while True:
        print("1. Customer")
        print("2. Shopkeeper")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            customer()
        elif choice == "2":
            shopkeeper()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
