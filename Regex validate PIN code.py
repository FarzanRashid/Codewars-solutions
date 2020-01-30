def validate_pin(pin):
    if pin.isdigit():
        if len(pin) == 6 or len(pin) == 4:
            return True
    return False
