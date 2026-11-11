try:
    number = int(input("Enter a decimal whole number: "))

    if number < 0:
        print("Please enter zero or a positive number.")
    else:
        print("Decimal:", number)
        print("Binary:", bin(number)[2:])
        print("Hexadecimal:", hex(number)[2:].upper())

except ValueError:
    print("Please enter a whole number.")