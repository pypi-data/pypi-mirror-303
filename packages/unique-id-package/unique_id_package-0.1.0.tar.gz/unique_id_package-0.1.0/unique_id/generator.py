import random
import string

def generate_unique_id(length=16, digits_only=False):
    if digits_only:
        return ''.join(random.choices(string.digits, k=length))
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
