# Task1

# sales = [1200,450,980,1500,3000]

# Writing data into file.
# fl = open("sales_data.txt","w")
# for sale in sales:
#     fl.write(f"{sale}\n")
# fl.close()

# Read data from sales_data.txt file.
# fl_read = open("sales_data.txt","r")
# for ln in fl_read.readlines():
#     print(ln)
# fl_read.close()

# Reopen that file with write mode and override with comma sign in single line.
# fl = open("sales_data.txt","w")
# count = 0
# for ln in sales:
#     if count == 0:
#         fl.write(f"{ln}")
#     else:
#         fl.write(f",{ln}")
#     count+=1
# fl.close()

# Read one more time to confirm data override with comma seprated with single line.
# fl = open("sales_data.txt","r")
# for ln in fl.readlines():
#     print(ln)
# fl.close()



# TASK 2

# Read() method used
# fl = open("sales_data.txt","r")
# print("Read()...")
# print(fl.read())
# fl.close()

# ReadLine() method used
# fl = open("sales_data.txt","r")
# print("ReadLine()...")
# while(True):
#     line = fl.readline()
#     print(line)
#     if not line:
#         break
# fl.close()

# ReadLines() method used
# fl = open("sales_data.txt", "r")
# print("ReadLines()...")
# for line in fl.readlines():
#     print(line)


# TASK 3

# with open("sales_data.txt","a") as file:
#     for ln in ["5000","2500","1700"]:
#         file.write(f"{ln}\n")

# fl = open("sales_data.txt", "r")
# lines = fl.readlines()
# print(lines)
# print(f"Total lines {len(lines)}")
# fl.close()


# TASK 4


# total_sale_list = []
# with open("sales_data.txt","r") as line:
#     total_sale_list = line.readlines()
# sale_list = []
# for line in total_sale_list:
#     line = line.replace("\n","")
#     if line.isdecimal() or line.isdigit():
#         sale_list.append(int(line))

# print(f"Total Sales {sum(sale_list)}")
# print(f"Highest Sales {max(sale_list)}")
# print(f"Minimum Sales {min(sale_list)}")
# print(f"Average Sales {sum(sale_list) / len(sale_list)}")



# TASK 5

# with open("products.txt","a") as prd:
#     count = 0
#     while(True):
#         product_input = input("Enter Product Name")
#         product_price = input("Enter Product Price")
#         prd.write(f"{product_input}|{product_price}\n")
#         count += 1
#         if count == 3:
#             break

# file = open("products.txt","r")
# for fl in file.readlines():
#     product = fl.split("|")
#     print(f"Product name is {product[0]} and price is {product[1]}")
# file.close()



# TASK 6

# import os
# file = input("Enter file name to print.")
# if os.path.exists(file):
#     print("File is avaialble")
#     fl = open(file, "r")
#     print(fl.readlines())
#     fl.close()
# else:
#     print("File not found. Please check filename.")


# TASK 7

# prices = {"Mouse":500, "Keyboard":800, "Monitor":7000, "Pendrive":400, "Camera":5000}
# discount = input("Enter Discount.")
# if discount.isdecimal() or discount.isdigit():
#     discount = float(discount)
#     total_discount = 0
#     with open("discount_report.txt", "a") as file:
#         for key,value in prices.items():
#             td = value*discount/100
#             total_discount += td
#             file.write(f"{key}|{value}|{value-(td)}\n")
#     file = open("discount_report.txt","r")
#     total_item  = 0
#     print("Product | Original Price | Discounted Price")
#     for line in file.readlines():
#         ln = line.split("|")
#         print(f"{ln[0]}|{ln[1]}|{ln[2]}")
#         total_item += 1
#     print(f"Total Item is {total_item}")
#     print(f"Average Discount Price {total_discount / total_item}")
# else:
#     print("Enter Discount is not properly added.")