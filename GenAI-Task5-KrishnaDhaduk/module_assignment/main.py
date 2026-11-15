import math_utils
from math_utils import square
from string_utils import *

import shop_package.discount as discount
import shop_package.billing as billing


print("TASK 1")
print(f"Sum of 10+30 is {math_utils.add(10,30)}")
print(f"Substraction of 30-10 is {math_utils.subscract(30,10)}")
print(f"Squire of 10*10 is {square(10,10)}")


print("TASK 2")
print(f"Capitlize Word is 'krishna dhaduk' {capitalize_words("krishna dhaduk")}")
print(f"Reverse String is 'krishna dhaduk' {reverse_string('krishna dhaduk')}")
print(f"Word Count of 'krishna dhaduk' is {word_count('krishna dhaduk')}")

print("TASK 3 & 4")
print(f"Discount 5% {discount.apply_discount(1000, 10)}")
print(f"Flat 50 discount {discount.flat_discount(150)}")

total = [100,3000,299,39,30]

print(f"Total of {total} is {billing.calculate_total(total)}")
for sale in total:
    print(f"Apply 5% tax {sale} is {billing.apply_tax(sale)}")