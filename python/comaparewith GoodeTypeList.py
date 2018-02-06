mixed_list = ['magical unicorns',19,'hello',98.98,'world']
integer_list = [1,2,3,4,5]
string_list = ["Spiff", "Moon", "Robot"]

def identify_list_type(lst):
    new_string = ''
    total = 0

    for item in lst:
        if isinstance(item, int) or isinstance(item, float):
            total += item
        elif isinstance(item, str):
            new_string += item

    if new_string and total:
        print "The array you entered is of mixed type"
        print "String:", new_string
        print "Total:", total

    elif new_string:
        print "The array you entered is of string type"
        print "String:",new_string

    else:
        print "The array you entered is of number(float or int) type"
        print "Total:", total

print identify_list_type(mixed_list)
print identify_list_type(integer_list)
print identify_list_type(string_list)