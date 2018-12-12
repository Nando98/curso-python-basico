# Working with Strings

my_string = "Hello world! 'Fernando' "
print(my_string)

# Saltos de linea
my_text = "Esto tiene saltos de linea.\nNo se que es lo que pase"
print(my_text)


course = "Python 3"
student = "Fernando"

# Concatenando strings
#   Forma 1
message_one = "Nuevo curso de " + course + " por " + student
#   Forma 2
message_two = "Nuevo curso de %s por %s" %(course, student)
#   Forma 3
message_three = "Nuevo curso de {} por {}".format(course, student)
print(message_three)

