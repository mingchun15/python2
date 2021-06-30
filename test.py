
#2
e=int(input("請輸入一個度數"))
if(e<120):
    print("Summer months:"+str(e*2.10))
    print("Non-Summer months:"+str(e*2.10))
elif(e>=120 and e<330):
    print("Summer months:"+str(e*3.02))
    print("Non-Summer months:"+str(e*2.68))
elif(e>=330 and e<500):
    print("Summer months:"+str(e*4.39))
    print("Non-Summer months:"+str(e*3.61))
elif(e>=500 and e<700):
    print("Summer months:"+str(e*4.97))
    print("Non-Summer months:"+str(e*4.01))
else:
    print("Summer months:"+str(e*5.63))
    print("Non-Summer months:"+str(e*4.50))
#3
tmp=["rat","ox","tiger","rabbit","dragon","snake","horse","sheep","monkey","rooster","dog","pig"]
year=int(input("輸入西元年"))
res=(year-4)%12
print(tmp[res])
#4
x=int(input("X軸的座標:"))
y=int(input("Y軸的座標:"))
if(x>0 and y>0):
    print("該點位於第一象限，離原點距離為根號"+str(x**2+y**2))
elif(x==0 and y==0):
    print("該點位於原點")
elif(x==0 and y>0):
    print("該點位於上半平面Y軸上，離原點距離為根號"+str(y**2))
elif(x<0 and y==0):
    print("該點位於左半平面Y軸上，離原點距離為根號"+str(x**2))
#5
total=i=1
m=int(input("輸入階層值M:"))
while(total<=m):
    i=i+1
    total=total*i
print("超過M為"+str(m)+"的最小階層N值為:"+str(i))
#6
a=list(input("輸入值為:"))
for j in range(len(a)-2):
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            tmp=a[i]
            a[i]=a[i+1]
            a[i+1]=tmp
for j in range(len(a)):
    c=a[::-1]
st=""
for k in a:
    st+=k
st1=""
for l in c:
    st1+=l
ans=int(st1)-int(st)
print("最大值列與最小值數列差值為:"+str(ans))
#7
n,v=map(int,input("輸入月租費型式及通話時間為").split())
def p(n,v):
    if(n==186):
        a=v*0.09
        if(a//186==1):
            c=a*0.9
        else:
            c=a*0.8
        return c
    elif(n==386):
        a=v*0.08
        if(a//386==1):
            c=a*0.8
        else:
            c=a*0.7
        return c
    elif(n==586):
        a=v*0.07
        if(a//586==1):
            c=a*0.7
        else:
            c=a*0.6
        return c
    elif(n==986):
        a=v*0.06
        if(a//986==1):
            c=a*0.6
        else:
            c=a*0.5
        return c   
print("通話費為:%f"%p(n,v))
#8
a=int(input("請輸入第一行正整數為:"))
lista=input("第二行中數列中的數字為:")
lista=lista.split()
maxcount=0
maxnum=0
for i in range(len(lista)):
    if lista.count(lista[i])>maxcount:
        maxcount=lista.count(lista[i])
        maxnum=lista[i]
if (maxcount==1):
    print("每個數剛好出現一次")
else:
    print("最大出現次數的數字為:"+str(maxnum))
    print("出現次數:"+str(maxcount))
#9
s1=input("輸入s1為:")
s2=input("輸入s2為:")
if s1 in s2:
    print("YES")
else:
    print("NO")

#11
m,d=map(int,input("輸入月及日為:").split())
if((m==1 and(d>=21 and d<=31))or(m==2) and (d>=1 and d<=18)):
    print("星座為:Aquarius")
elif((m==2 and(d>=19 and d<=29))or(m==3) and (d>=1 and d<=20)):
    print("星座為:Pisces")
elif((m==3 and(d>=21 and d<=31))or(m==4) and (d>=1 and d<=20)):
    print("星座為:Aries")
elif((m==4 and(d>=21 and d<=30))or(m==5) and (d>=1 and d<=21)):
    print("星座為:Taurus")
elif((m==5 and(d>=22 and d<=31))or(m==6) and (d>=1 and d<=21)):
    print("星座為:Gemini")
elif((m==6 and(d>=22 and d<=30))or(m==7) and (d>=1 and d<=22)):
    print("星座為:Cancer")
elif((m==7 and(d>=23 and d<=31))or(m==8) and (d>=1 and d<=23)):
    print("星座為:Leo")
elif((m==8 and(d>=24 and d<=31))or(m==9) and (d>=1 and d<=23)):
    print("星座為:Virgo")
elif((m==9 and(d>=24 and d<=30))or(m==10) and (d>=1 and d<=23)):
    print("星座為:Libra")
elif((m==10 and(d>=24 and d<=31))or(m==11) and (d>=1 and d<=22)):
    print("星座為:Scorpio")
elif((m==11 and(d>=23 and d<=30))or(m==12) and (d>=1 and d<=21)):
    print("星座為:Sagittarius")
elif((m==12 and(d>=22 and d<=31))or(m==1) and (d>=1 and d<=20)):
    print("星座為:Capricorn")
#12
a=input("請輸入一整數序列").split()
times=0
for i in range(len(a)):
    if (a.count(a[i])>times):
        times=a.count(a[i])
        n=a[i]
if (times==1):
    print("過半元素為:NO")
else:   
    print("過半元素為:"+str(n))
#13
s=input("輸入一字元為:")
if (s==s[::-1]):
    print("YES")
else:
    print("NO")
#14
n=input("輸入一字串為:")
s=len(n)
print("There are"+" "+str(s)+" "+"characters")

#17
total=0
s=input()
s=s.split()
for i in range(5):
    if (s[i]=="A"):
        n=1
    elif(s[i]=="J"):
        n=11
    elif(s[i]=="Q"):
        n=12
    elif(s[i]=="K"):
        n=13
    else:
        n=int(s[i])
    total+=n
print(total)

#19
d=int(input("組數為:"))
totalticket=[]
for i in range(d):
    ticket=input("第"+str(i+1)+"組:").split()
    totalticket.append(int(ticket[0])*250+int(ticket[1])*175)
for i in range(d):
    print("第"+str(i+1)+"組應收費用:"+str(totalticket[i]))
    

#25
string=""
while(string!="end"):
    string=input("檢測的字串(end 結束)")
    if(string=="end"):
        print("檢測結束")
    else:
        n=input("檢測的單一字元:")
        a=string.count(n)
    print("字元"+str(n)+"出現次數為"+str(a))

#28
c="1234"
A=0
B=0
b=input("輸入數字")
for i in range(4):
    for j in range(4):
        if c[i]==b[j]:
            if i==j:
               A+=1
            else:
                B+=1
        else:
            print(" ")
print(str(A)+"A"+str(B)+"B")        

#31
scores=["國文","英文","微積分","體育","程式設計"]
listscores=[]
total=0
score=0
for i in range(5):
    score=int(input(str(scores[i])+":"))
    listscores.append(score)
    total+=score
max1=max(listscores)
max2=listscores.index(max1)
min1=min(listscores)
min2=listscores.index(min1)
avg=total/len(scores)
print("平均分數:"+str(avg))
print("最高分科目:"+str(scores[max2])+str(max1)+"分")
print("最低分科目:"+str(scores[min2])+str(min1)+"分")

#32
num=int(input("請輸入一正整數:"))
if(num%2==0 and num%11==0 and num%5!=0 and num%7!=0):
    print(str(num)+"為新公倍數?:YES")
else:
    print(str(num)+"為新公倍數?:NO")
#33
sa=input("sA:")
sb=input("sB:") 
if sa in sb:
    print("Yes")
else:
    print("NO")
#46
medal=[]
medals=["金","銀","銅","優"]
n=int(input("輸入筆數n:"))
for i in range(n):
    g=input(str(medals[i]))
    medal.append(g)
for j in range(n):
    print(str(medals[j])+"牌得到"+medal[j]+"面")
#48
st=input("請輸入英文句子:")
st=st.split()
st.reverse()
print("輸出結果:"+str(st))
#49
allstudents=set(["John","Mary","Tina","Fiona","Claire","Eva","Ben","Bill","Bert"])
engpass=set(["John","Mary","Fiona","Claire","Ben","Bill"])
mapass=set(["Mary","Fiona","Claire","Eva","Ben"])
print("英文與數學都及格"+str(engpass&mapass))
print("數學不及格"+str(allstudents-mapass))
print("英文及格且數學不及格"+str(engpass&(allstudents-mapass)))

#51
a=set(["紅","豆","生","南","國","，","春","來","發","幾","枝","，","願","君","多","采","擷","，","此","物","最","相","思","。"])
b=set(["春","眠","不","覺","曉","，","處","處","聞","啼","鳥","。","夜","來","風","雨","聲","，","花","落","知","多","少","。"])
a.remove("，")
a.remove("。")
b.remove("，")
b.remove("。")
print((a&b))
#52
n1=int(input("輸入n值:"))
names=[]
mails=[]
for i in range(n1):
    name=input("請輸入姓名")
    names.append(name)
    mail=input("請輸入電子郵件")
    mails.append(mail)
find=input("請輸入要查詢電子郵件的姓名:")
b=names.count(name)
if(b==1):
    v=names.index(find)
print(str(find)+"電子郵件帳號為:"+str(mail))



