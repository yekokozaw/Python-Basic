file = open("notes.txt","w")
file.writelines("hello\n")

for i in range(10):
    file.write(str(i)+"\r\n")


file.close
print("done")