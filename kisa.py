print("Age brackets\n")

print("")
try:
    year= int(input("year of birth in number form: "))
    age= 2019 -year
    age=int(age)
    if age< 18: 
        print ("minor")
    if 18<= age <= 36:
        print ("youth")
    if age> 36:
        print("elders")

except:
        print("only numbers allowed")