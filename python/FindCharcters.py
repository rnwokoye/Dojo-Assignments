# # Copied solution
# word_list = ['hello','world','my','name','is','Anna']
# char = 'o'
#
# def find_character(word_list, char):           # declare the functin and variables
#     new_list = []                              # Declare an empty list to hold our new list
#     for i in range(0, len(word_list)):          # The for loop
#
#         if word_list[i].find(char) != -1:       # .find function used
#             new_list.append(word_list[i])       # .append function to add to list
#
#     print new_list
#
# test_list = ['hello','world','my','name','is','Anna']
# find_character(test_list, 'o')

z = []
word_2 = ['hello','world','my','name','is','Anna']
for element in word_2:
    #print element
    if element.find('o') > 0:
        #print element
        z.append(element)
print z
    #print element.find('o')
print type(z)

