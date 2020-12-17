# lucky_numbers = [4, 8, 15, 16, 23, 42]
# friends = ["Kevin", "Karen", "Jim", "Alan", "Oscar", "Toby"]
# lucky2 = lucky_numbers.copy()
# print(lucky2)
#
# coordinates = (4, 5)
# print(coordinates)

# def say_hi(name, age):
#     print("Hello " + name + ". You are " + str(age))
#
# say_hi("Mike", 34)
# say_hi("Steve", 88)

# def cube(num):
#     return num*num*num
# result = cube(4)
# print(result)

# is_male = False
# is_tall = False
#
# if is_male and is_tall:
#     print("You are a male")
# elif is_male and not(is_tall):
#     print("You are a short male")
# elif not(is_male) and is_tall:
#     print("You are a tall male")
# else:
#     print("You are not a male and not tall")

# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3
#
# print(max_num(300, 40, 5))

# num1 = float(input("Enter first number: "))
# op = input("Enter operator number: ")
# num2 = float(input("Enter 2nd number: "))

# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "/":
#     print(num1 / num2)
# elif op == "*":
#     print(num1 * num2)
# else:
#     print("Invalid operator")
#
# monthConversions = {
#     0: "January",
#     "Feb": "February",
#     "Mar": "March",
#     "Mai": "Mai",
# }
# print(monthConversions.get(0))
#
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
#
# print("Done with loop")

#create variables
# secret_word = "giraffe"
# guess = ""
# #variables that keep track how often user typed in the word
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False
#
# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("Enter guess: ")
#         guess_count += 1
#     else:
#         out_of_guesses = True
# if out_of_guesses:
#     print("Out of Guesses, GAME OVER")
# else:
#     print("You win!")
# friends = ["Jim", "Karen", "Kevin"]
# for index in range(5):
#     if index == 0:
#         print("First Iteration")
#     else:
#         print("Not first")
base = int(input("Enter a Base: "))
poww = int(input("Enter the Power: "))

def raise_to_power(base, poww):
    result = 1
    for index in range(poww):
        result = result * base
    return result
print(raise_to_power(base, poww))



