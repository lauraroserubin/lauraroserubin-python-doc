def multiply_numbers(numbers):
    product=1
    for x in numbers:
        product*=x
    return product
print(multiply_numbers((1,2,3)))