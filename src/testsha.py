from init import argon2Hasher

password = str(input("Print your password: "))

hash = argon2Hasher.hash(password)
print("Argon2 hash (random salt):", hash)

verifyValid = argon2Hasher.verify(hash, password)
print("Argon2 verify (correct password):", verifyValid)
