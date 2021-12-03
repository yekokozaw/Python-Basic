my_tuple = "hello",2
print("Two element tuple",my_tuple)     #as a literal

lst = [1,"Two",3]
my_tuple = tuple(lst)
print("Tuple constructor ",my_tuple)

one_to_ten = range(0,10)
my_tuple = tuple(one_to_ten)
print("Tuple constructor from range",my_tuple)
print("Tuple [1:5]",my_tuple[1:5])
print("Tuple reverse ",my_tuple[:-1])