# def NumberText(c): #6
#     #Check if the number is odd
#     if len(c)%2 !=0:
#         c= c + "1"
#     k = 0#6
#     n = 1 #4
#     result = ""
    
#     while k<len(c):
#         if len(c) > 2 and int(c[k:n]) > 10 and int(c[k:n]) < 96:
#                 formula = (int(c[k:n]) - 1) +65
#                 result = result+(str(chr(formula)))
#                 k+= 2
#                 n = n +1
#         # elif len(c) <= 2 :
#         #     for item in c:
#         #         formula = (int(item)-1)+65
#         #         result= result + str(chr(formula))
#         #     break
#         else:
#             n = n+1
            
#     return(result)

# # def NumberText(result):
# #     g =""
# #     for i in range(len(result)):
# #         if int(result[i])<96:
# #             formula = (int(result[i])-1)+65
# #             g = g + str(chr(formula))
# #     return g




# print(NumberText("12163420"))
# # text= "151122"
# # print(text[0:2])


# from string import ascii_lowercase


# LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)} 

# def alphabet_position(text):
#     text = text.lower()
#     list = []

#     numbers = [LETTERS[character] for character in text if character in LETTERS]

#     # return ''.join(numbers)
#     list.append(numbers)
#     return list
# # print(alphabet_position("ali"))
# # print(chr(42+96-1))
# e= 3
# n =3127
# result = []
# a = alphabet_position("ali")
# print(a[0])
# # for i in range(len(a)):
#     print(a[i])
#     c = str((int(items)**e)%n)
#     result.append(c)
# print(result)

text = str("54")
# if text.isnumeric():
#     print("Fuck Sandeep")

# if type(text) == int():
#     print("amrched")
# elseL

print(text.isnumeric())