# big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

# # Print only positive numbers:
# for i in big_number_list:
#     if i < 0:
#         break
#     print(i)

# # break = the loop stops after the first time its condition is not met
# # continue = the loop continues and skips any indexes that does not meets its condition

# for i in range(1):
#     print("WARNING")

# result = [x**2 for x in range(1, 13) if x % 2 == 0]

# print(result)


# def square_point(x, y, z):
#     x_squared = x * x
#     y_squared = y * y
#     z_squared = z * z
#     # Return all three values:
#     return x_squared, y_squared, z_squared


# a, b, c = square_point(3, 4, 5)

# print(a, b, c)
# square_point()

# txt = 'She said "Never let go"\.'
# print(txt)  # She said "Never let go".

# str = "yellow"

# asd = str[4:6]

# print(asd)

# my_dictionary = {"song": "Estranged", "artist": "Guns N' Roses"}
# print(my_dictionary["song"])
# my_dictionary["song"] = "Paradise City"
# print(my_dictionary["song"])


for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
