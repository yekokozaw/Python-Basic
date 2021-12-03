number_of_subj = int(input("Enter number of subject => "))

pass_mark = 40
isPass = True

for i in range(number_of_subj):
    mark = float(input("Enter mark for subject "+str(i)+" "))
    isPass=isPass and mark>=pass_mark

if isPass:
    print("Pass the exam")
else:
    print("Fail the exam")