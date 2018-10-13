from django.test import TestCase

# Create your tests here.

import string
import random


def generate_random_code(length=8):
    import random
    s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.sample(s, length))
