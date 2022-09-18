from init import argon2Hasher
import binascii


def encode(password):
    hash = argon2Hasher.hash(password)
    return hash

def verify(password):
    verifyValid = argon2Hasher.verify(hash, password)
    return verifyValid
