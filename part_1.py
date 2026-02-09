def userinput(new_findings=[""]):
    i=0
    while True:
        rocks= input("what rock did you find")
        new_findings.append(rocks)
        i=i+1
        if (i==3):
            return new_findings
            





# part 1.1
sample_bay= ["Basalt","silica","iron","dust"]
print(sample_bay[0])
print(len(sample_bay))
x= sample_bay[len(sample_bay)-1]
print(x)
print(sample_bay[-1])
# part 1.2
for i in sample_bay:
    print(i)


# part 1.3, function defined at the top of this file
new_findings=[]

new_findings=userinput(new_findings=[])
#for x in new_findings:
print(new_findings)





# part 1.4

if "dust"in sample_bay:
    print("yes")
    sample_bay.remove("dust") 
print(sample_bay)


