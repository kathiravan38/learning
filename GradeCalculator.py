#grade calculator
def calculate(lst):
    total, avg, percentage = 0, 0.0, 0.0
    for i in lst:
        total += i
    avg = total // len(lst)
    percentage = (total / 500) * 100
    return total, avg, percentage

def grade(percentage):
    print("\n**grade checker for percentage**")
    if (percentage >= 80):
        print("A grade")
    elif (percentage >= 60):
        print("B grade")
    elif (percentage >= 50):
        print("C grade")
    else:
        print("D grade")

def pass_or_fail(lst):
    print("\n**pass or fail checker**")
    i=0
    while(i<len(lst)):
        if lst[i]>45:
            print(f"pass in subject {i+1}")
        else:
            print(f"fail in subject {i+1}")
        i+=1

lst = []
i=1
while(i<=5):
    n=int(input(f"enter the mark for subject {i}: "))
    if(n>=0 and n<100):
        lst.append(n)
    else:
        print("enter the valide mark")
    i+=1
pass_or_fail(lst)
total, avg, percentage = calculate(lst)
print(f"\ntotal mark for 5 subjects: {total}")
print(f"average mark for 5 subjects: {avg}")
print(f"percentage mark for 5 subjects: {round(percentage, 2)}")
grade(percentage)

