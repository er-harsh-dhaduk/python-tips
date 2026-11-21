cart = []

while(True):
    user_input = input("Enter price.")
    try:
        if user_input == "q":
            break
        price = float(user_input)
        if price < 0:
            raise TypeError
    except ValueError as vr:
        print(f"{vr}")
    except TypeError as tr:
        print(f"{tr}")
    else:
        cart.append(price)
    finally:
        print(f"Total Item Is {len(cart)}")
        print(f"Total Bill Is {sum(cart)}")