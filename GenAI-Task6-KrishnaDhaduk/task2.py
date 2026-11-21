prices = [120,350,'abc', 500, -200, 800]
total = 0
for price in prices:
    try:
        total += price
        if price < 1:
            raise ValueError
    except TypeError as te:
        print(f"{price} is not integer value.")
    except ValueError as ve:
        print(f"{price} is negative value or invalid value.")
    else:
        print(f"Total is {total}")