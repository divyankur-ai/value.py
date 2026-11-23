try:
    user_age = int(input("enter your age: "))
    print("your age", user_age)

except ValueError as ex:
    print("exception:", ex)