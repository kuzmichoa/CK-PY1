import random
import string
from random import sample
def get_random_password() -> str:
    up_latters = string.ascii_uppercase
    low_latters = string.ascii_lowercase
    num = string. digits
    all_ = up_latters + low_latters + num
    pass_ = "". join(random.sample(all_, 8))
    return pass_
    ...  # TODO написать функцию генерации случайных паролей


print(get_random_password())
# task 5
