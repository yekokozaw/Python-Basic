str = "Hello from python"

print("Str[1,3]",str[1:3])
print("Str[1:", str[1:])

application_type = "application/w-xxx-form-urlencoded"
type = application_type[application_type.find("/")+1:]  
#find
print("Type ",type)

date_str = "3-08-2021"
date_str_list = date_str.split("-")
print("date list ",date_str_list)

date_str_new = '/'.join(date_str_list)
print(date_str_new)