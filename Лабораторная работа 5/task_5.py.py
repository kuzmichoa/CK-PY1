import random
import string
from random import sample
def get_random_password() -> str:
    Latters = string.ascii_uppercase
    latt = string.ascii_lowercase
    num = string. digits
    all = Latters + latt + num
    pass_ = "". join(random.sample(all, 8))
    return pass_
    ...  # TODO написать функцию генерации случайных паролей


print(get_random_password())
