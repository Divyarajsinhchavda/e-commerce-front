"""Module under test: LearnSphere course fee and enrollment rules."""
def course_fee(price, coupon_percent=0):
    """Fee after discount. price: 1 to 50000, coupon: 0 to 50 (percent)."""
    for value in (price, coupon_percent):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("price and coupon must be numbers")
    if not 1 <= price <= 50000:
        raise ValueError("price must be between 1 and 50000")
    if not 0 <= coupon_percent <= 50:
        raise ValueError("coupon must be between 0 and 50")
    return round(price - price * coupon_percent / 100, 2)
def enrollment_status(is_logged_in, payment_done, seats_left):
    """What happens when the student presses the Enroll button."""
    if not isinstance(seats_left, int) or isinstance(seats_left, bool):
        raise TypeError("seats_left must be an integer")
    if seats_left < 0:
        raise ValueError("seats_left cannot be negative")
    if not is_logged_in:
        return "Login Required"
    if not payment_done:
        return "Payment Pending"
    return "Enrolled" if seats_left > 0 else "Waitlisted"
