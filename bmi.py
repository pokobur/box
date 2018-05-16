ask1 = input("身長を入力してください\n")
ask2 = input("体重を入力してください\n")

hei = float(ask1) / 100
wei = float(ask2)
bmi = float(wei) / float(hei) / float(hei)
print ("bmi= ",end="")
print (round(bmi,2))
#print ('bmi= ' + str(bmi))  ←　小数がたくさん出てくる　　bmi= 15.615704937537183
