name = "aras"
print("aras")
print(name)
print(f"{name}")

a = 5
b = 3
c = a + b
print(c)
print(a + b)
print(f"{a + b}")

lang = "Python"
print(f"{lang.lower()} is a programming language")

pi = 3.14159
print(f"Pi: {pi:.2f}")

from datetime import datetime
now = datetime.now()
print(f"datetime: {now:%Y-%m-%d %H:%M:%S}")

x = input("adjective:")
y = input("noun:")
z = input("verb:")
print(f"{x} {y} {z}")