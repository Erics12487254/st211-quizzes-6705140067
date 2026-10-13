def apply_discount(price, percent):

    if percent < 0 or percent > 100:
        raise ValueError("Discount percent must be between 0 and 100")

    return price * (1 - percent / 100)