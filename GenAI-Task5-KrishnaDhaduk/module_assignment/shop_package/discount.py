def apply_discount(price, percent):
    """Return discounted price."""
    return price + (price * percent / 100)

def flat_discount(price):
    """Return flat 50 amount discount."""
    if price < 50:
        return 0
    return price - 50