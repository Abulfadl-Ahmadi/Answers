import random
import string


def id_generator(size=16, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))
