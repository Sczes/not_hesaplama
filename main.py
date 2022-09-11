vize1 = int(input("Ilk vize sonucunuzu girin: "))
vize2 = int(input("Ikinci vize sonucunuzu girin: "))
final = int(input("Final sonucunuzu girin: "))

a = vize1*0.3
b = vize2*0.3
c = final*0.4
total = a+b+c 

if(total>=90):
    print("AA")
elif(85<=total<90):
    print("BA")
elif(80<=total<85):
    print("BB")
elif(75<=total<80):
    print("CB")
elif(70<=total<75):
    print("CC")
elif(65<=total<70):
    print("DC")
elif(60<=total<65):
    print("DD")
elif(55<=total<60):
    print("FD")
else:
    print("FF")
    