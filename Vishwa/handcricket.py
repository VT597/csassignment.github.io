import random
#Handcricket
a=[1,2,3,4,5,6,7,8,9,10]

print("Please type in *CAPS ONLY*")

b=input("Toss choice:H/T:")
toss=["H","T"]
k=random.choice(toss)

bb=["BAT","BOWL"]

ch=random.choice(bb)
innings=0
tosscounter=0
tosswin=0

s=0
c=0
balls=0

if(k==b):
  tosscounter=True
  tosswin=input("You have won the toss, what do you choose:BAT/BOWL:")
elif(k!=b):
  tosswin=None
  tosscounter=False
  print("You have lost the toss, Bot chooses:",ch)
else:
  print("Error,please only enter H or T")

overs=int(input("Enter the number of overs from 1 to 10:"))
if(overs<=0 or overs>=11):
  print("Error, please refresh and try again from 1 to 10 only")
  
if(overs>=1 and overs<=10):
  innings+=1
  
if(innings==1):
  if((tosswin=="BAT") and (tosscounter==True)) or ((ch=="BOWL") and (tosscounter==False)):
    for i in range(1,(overs*6)+1):
      runs=int(input("Enter the no. of runs between 1 to 10:"))
      if(runs<=0 or runs>=11):
        runs=1
        print("Error, please only enter values from 1 to 10, this ball will be counted as 1")
      d=random.choice(a)
      s=s+runs
      balls+=1
      if (runs==d):
        s=s-runs
        print("You're out! Score:",s,"Balls:",balls)
        print("Runs:",s,"You:",runs,"Opponent:",d)
        break
      print("Runs:",s,"You:",runs,"Opponent:",d)
  elif((tosswin=="BOWL") and (tosscounter==True)) or ((ch=="BAT") and (tosscounter==False)):
    for i in range(1,(overs*6)+1):
      bowl=int(input("Enter a no. between 1 to 10:"))
      if(bowl<=0) or (bowl>=11):
        print("Error, please only enter values from 1 to 10, this ball will be counted as 1")
        bowl=1
      z=random.choice(a)
      c=c+z
      balls+=1
      if(z==bowl):
        c=c-z
        print("Bot is out!,Score:",c,"Balls:",balls)
        print("Runs:",c,"You:",bowl,"Opponent:",z)
        break
      print("Runs:",c,"You:",bowl,"Opponent:",z)
  innings+=1

if(innings==2):
  balls=0
  if((tosswin=="BAT") and (tosscounter==True)) or ((ch=="BOWL") and (tosscounter==False)):
    print("Target for bot=",s+1)
    print("You're bowling now")
    for j in range(1,(overs*6)+1):
      bowl=int(input("Enter a no. between 1 to 10:"))
      if(bowl<=0) or (bowl>=11):
        print("Error, please only enter values from 1 to 10, this ball will be counted as 1 run")
        bowl=1
      z=random.choice(a)
      c=c+z
      balls+=1
      if(c>s):
        print("BOT WINS.....,Your Score:",s,"Bot score:",c)
        break
      if(c==s):
        if(z==bowl):
          print("MATCH DRAWN,Your Score:",s,"Bot score:",c)
      if(z==bowl):
        c=c-z
        print("Runs:",c,"You:",bowl,"Opponent:",z)
        print("Bot is out!,Score:",c,"Balls:",balls)
        print("YOU WIN!!, Your Score:",s,"Bot score:",c)
        break
      print("Runs:",c,"You:",bowl,"Opponent:",z)
      if(j==(overs*6)):
        if(c<s):
          print("YOU WIN!!,Your Score:",s,"Bot score:",c)
  elif((tosswin=="BOWL") and (tosscounter==True)) or ((ch=="BAT") and (tosscounter==False)):
    print("Your Target=",c+1)
    print("You're batting now")
    for j in range(1,(overs*6)+1):
      runs=int(input("Enter the no. of runs between 1 to 10:"))
      if(runs<=0 or runs>=11):
        runs=1
        print("Error, please only enter values from 1 to 10, this ball will be counted as 1")
      d=random.choice(a)
      s=s+runs
      balls+=1
      if(s>c):
        print("YOU WIN!!,Your Score:",s,"Bot score:",c)
        break
      if(c==s):
        if(runs==d):
          print("MATCH DRAWN,Your Score:",s,"Bot score:",c)
          break
      if(runs==d):
        s=s-runs
        print("Runs:",s,"You:",runs,"Opponent:",d)
        print("You're out! Score:",s,"Balls:",balls)
        print("YOU LOSE.....,Bot score:",c,"Your score:",s)
        break
      print("Runs:",s,"You:",runs,"Opponent:",d)
      if(j==(overs*6)):
        if(s<c):
          print("YOU LOSE.....,Bot score:",c,"Your score:",s)

if(j==(overs*6)):
    if(s==c):
      print("MATCH DRAWN,Your score:",s,"Bot score:",c)
    
print("Thank you for playing, Game designed by your boi VT")


 

    
    
    
  
        
  

  
    
  
