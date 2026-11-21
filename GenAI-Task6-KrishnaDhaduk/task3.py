def check_age(age):
    try:
        if age >=1 and age <=120:
            pass
        else:
            raise ValueError
    except ValueError:
        print(f"{age} Invalid age or its not between 1 to 120 year of age.")
    else:
        print(f"Your age is {age}")


check_age(int(input("Enter Age")));
