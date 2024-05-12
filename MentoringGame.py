import json
import random
def Save(file,backup_file):
    with open(file, "r") as file1, open(backup_file, "w") as file2:
        content = file1.read()
        file2.write(content)
def Overwrite(backup_file,file):
    with open(backup_file, "r") as file1, open(file, "w") as file2:
        content = file1.read()
        file2.write(content)
def update(filename,object,value):
    with open(filename,'r') as f:
        f_contents=f.readlines()
        f_contents[0]=json.loads(f_contents[0].replace("\'", "\""))
        f_contents[1]=json.loads(f_contents[1].replace("\'", "\""))
        f_contents[2]=float(f_contents[2])
        f_contents[3]=int(f_contents[3])
        f_contents[4]=int(f_contents[4])
        f_contents[5]=float(f_contents[5])
        f_contents[6]=str(f_contents[6])
        
        if object=="currentBuff" and type(value) is dict:
            f_contents[0]=value
        elif object=="Inventory" and type(value) is dict:
            f_contents[1]=value
        elif object=="VP" and ((type(value) is int) or (type(value) is float)):
            f_contents[2]=value
        elif object=="homeworkStreak" and type(value) is int:
            f_contents[3]=value
        elif object=="numofGachas" and type(value) is int:
            f_contents[4]=value
        elif object=="Tix" and ((type(value) is int) or (type(value) is float)):
            f_contents[5]=value
        elif object=="username" and type(value) is str:
            f_contents[6]=value
        else:
            print("Error when updating",object,"data in",filename,"with value:",value)
            return

        with open(filename,'w') as f:
            f.write('\n'.join(map(str, f_contents)))
    del f_contents
def get(filename,object):
    with open(filename,'r') as f:
        f_contents=f.readlines()
        f_contents[0]=json.loads(f_contents[0].replace("\'", "\""))
        f_contents[1]=json.loads(f_contents[1].replace("\'", "\""))
        f_contents[2]=float(f_contents[2])
        f_contents[3]=int(f_contents[3])
        f_contents[4]=int(f_contents[4])
        f_contents[5]=float(f_contents[5])
        f_contents[6]=str(f_contents[6])
        if object=="currentBuff":
            return f_contents[0]
        elif object=="Inventory":
            return f_contents[1]
        elif object=="VP":
            return f_contents[2]
        elif object=="homeworkStreak":
            return f_contents[3]
        elif object=="numofGachas":
            return f_contents[4]
        elif object=="Tix":
            return f_contents[5]
        elif object=="username":
            return f_contents[6]
        else:
            print("Error when getting",object,"data in",filename)
        del f_contents
rewards=["50 Tix","100 Tix","200 Tix","500 Tix","Cuppa Joe","Twofoldness","Fortune of The Devil"]#100 VP = 126 Tix
probabilities=[42,30,20,7,1/4,5/12,1/3]
class player:

    def __init__(self,filename,backupfilename):
        self.currentBuff=get(filename,"currentBuff")
        self.Inventory=get(filename,"Inventory")
        self.VP=get(filename,"VP")
        self.homeworkStreak=get(filename,"homeworkStreak")
        self.numofGachas=get(filename,"numofGachas")
        self.Tix=get(filename,"Tix")
        self.filename=filename
        self.backupfilename=backupfilename
        self.username=get(filename,"username")

        self.SAVEDcurrentBuff=get(backupfilename,"currentBuff")
        self.SAVEDInventory=get(backupfilename,"Inventory")
        self.SAVEDVP=get(backupfilename,"VP")
        self.SAVEDhomeworkStreak=get(backupfilename,"homeworkStreak")
        self.SAVEDnumofGachas=get(backupfilename,"numofGachas")
        self.SAVEDTix=get(backupfilename,"Tix")
        self.SAVEDfilename=backupfilename
        self.SAVEDusername=get(backupfilename,"username")

    def printIntro(self):
        randomMessage=[
            "Good to have you back, "+self.username+"!\nLet's get back to sharpening our minds and racking up that virtual currency.\nIt's time to show those problems who's boss!",
            "Hey there!\nWe hope you're ready to flex those brain muscles again.\nLet's conquer some more challenges and earn those rewards!",
            "Welcome back to the Mentoring Game, where math and coding meet fun and excitement.\nLet's get cracking on those problems and unlock some amazing virtual goodies!",
            "It's great to have you back, "+self.username+" the Mastermind!\nIt's time to earn some more VP and Tix and show off your skills to the world!",
            "Greetings, "+self.username+"!\nLet's jump right in and tackle those coding and math problems to earn rewards and make progress in the game!",
            "Welcome back to the world of Mentoring Game, where brains rule and rewards flow.\nWe're excited to have you back, "+self.username+", and can't wait to see what new heights we'll reach together."
        ]
        result=random.choices(randomMessage,weights=[1,1,1,1,1,1])
        print(result[0])

    def shop(self):
        print("----SHOP----")
        print("Twofoldness: (1100 Tix/item)")
        print("Fortune of The Devil: (1600 Tix/item)")
        print("Mystery Box: (100 Gachas/item) or (15000 Tix/item)")

    def GachaInfo(self):
        print("----GACHA INFORMATION----")
        for i in range(0,len(probabilities)):
            print(rewards[i]+": "+str(round(probabilities[i],2))+"%")

    def updateData(self):
        self.currentBuff=get(self.filename,"currentBuff")
        self.Inventory=get(self.filename,"Inventory")
        self.VP=get(self.filename,"VP")
        self.homeworkStreak=get(self.filename,"homeworkStreak")
        self.numofGachas=get(self.filename,"numofGachas")
        self.Tix=get(self.filename,"Tix")
        self.username=get(self.filename,"username")

        self.SAVEDcurrentBuff=get(self.SAVEDfilename,"currentBuff")
        self.SAVEDInventory=get(self.SAVEDfilename,"Inventory")
        self.SAVEDVP=get(self.SAVEDfilename,"VP")
        self.SAVEDhomeworkStreak=get(self.SAVEDfilename,"homeworkStreak")
        self.SAVEDnumofGachas=get(self.SAVEDfilename,"numofGachas")
        self.SAVEDTix=get(self.SAVEDfilename,"Tix")
        self.SAVEDusername=get(self.SAVEDfilename,"username")

    def save(self):#    USABLE
        print("Before:")
        self.printData()
        print()
        Save(self.filename,self.backupfilename)
        print("After:")
        self.printData()

    def load(self):#    USABLE
        print("Before:")
        self.printData()
        print()
        Overwrite(self.backupfilename,self.filename)
        print("After:")
        self.printData()

    def printAllData(self):#   USABLE
        self.updateData()
        print("----CURRENT DATA----")
        print("Username:",self.username)
        print("VP:",self.VP)
        print("Tix:",self.Tix)
        print("Current Buff:",self.currentBuff)
        print("Inventory:",self.Inventory)
        #print("Homework Streak:",self.homeworkStreak)
        print("Number of Gachas:",self.numofGachas)
        print('')
        print("----SAVED DATA----")
        print("Username:",self.SAVEDusername)
        print("VP:",self.SAVEDVP)
        print("Tix:",self.SAVEDTix)
        print("Current Buff:",self.SAVEDcurrentBuff)
        print("Inventory:",self.SAVEDInventory)
        #print("Homework Streak:",self.SAVEDhomeworkStreak)
        print("Number of Gachas:",self.SAVEDnumofGachas)
        
        print('')

    def printData(self):
        self.updateData()
        print("Username:",self.username)
        print("VP:",self.VP)
        print("Tix:",self.Tix)
        print("Current Buff:",self.currentBuff)
        print("Inventory:",self.Inventory)
        #print("Homework Streak:",self.homeworkStreak)
        print("Number of Gachas:",self.numofGachas)
        print('')

    def buy(self,itemID,quant=1):#    USABLE
        print("Before:")
        self.printData()
        print()
        if itemID == "x2" and self.Tix >= 1100*quant:#"Twofoldness"
            self.getItem("Twofoldness",quant)
            self.subTix(1100*quant)
        elif itemID == "x3" and self.Tix >= 1600*quant:#"Fortune of The Devil"
            self.getItem("Fortune of The Devil",quant)
            self.subTix(1600*quant)
        elif itemID == "MB" and self.numofGachas >= 100*quant:#"Mystery Box"
            self.getItem("Mystery Box",quant)
            self.numofGachas-=100*quant
            update(self.filename,"numofGachas",self.numofGachas)
        elif itemID == "MBT" and self.Tix >=15000*quant:#Mystery Box (Tix)
            self.getItem("Mystery Box",quant)
            self.subTix(15000*quant)
        else:
            print("Failed to purchase",itemID)
            print()
        print("After:")
        self.printData()

    def TestGacha(self,times):#    USABLE
        print("Before:")
        self.printData()
        print()
        print("Starts Test Gacha-ing",times,"time(s):")
        result=random.choices(rewards,weights=probabilities,k=times)
        rewardTix=0
        rewardCJ=0
        rewardx2=0
        rewardx3=0
        for i in result: 
            print(i)
            if i == "50 Tix":
                rewardTix+=50
            elif i == "100 Tix":
                rewardTix+=100
            elif i == "200 Tix":
                rewardTix+=200
            elif i == "500 Tix":
                rewardTix+=500
            elif i == "Cuppa Joe":
                rewardCJ+=1
            elif i == "Twofoldness":
                rewardx2+=1
            elif i == "Fortune of The Devil":
                rewardx3+=1
            else: pass
        print('')
        print("Total: (Test)")
        if rewardTix>0:
            print("- Tix:",rewardTix)
        if rewardCJ>0:
            print("- Cuppa Joe(s):",rewardCJ)
        if rewardx2>0:
            print("- Twofoldness(es):",rewardx2)
        if rewardx3>0:
            print("- Fortune(s) of The Devil:",rewardx3)
        del rewardTix
        del rewardCJ
        del rewardx2
        del rewardx3
        del result
        print("After:")
        self.printData()

    def RealGacha(self,times):#    USABLE
        print("Before:")
        self.printData()
        print()
        if self.VP < times*100:
            print("You don't have enough VP to purchase",times,"Gachas")
            return
        print("Starts Real Gacha-ing",times,"time(s):")
        self.subVP(100*times)
        update(self.filename,"numofGachas",self.numofGachas+times)
        result=random.choices(rewards,weights=probabilities,k=times)
        
        rewardTix=0
        rewardCJ=0
        rewardx2=0
        rewardx3=0
        for i in result:
            print(i)
            if i == "50 Tix":
                rewardTix+=50
            elif i == "100 Tix":
                rewardTix+=100
            elif i == "200 Tix":
                rewardTix+=200
            elif i == "500 Tix":
                rewardTix+=500
            elif i == "Cuppa Joe":
                rewardCJ+=1
            elif i == "Twofoldness":
                rewardx2+=1
            elif i == "Fortune of The Devil":
                rewardx3+=1
            else: pass
        print('')
        print("Total:")
        print("- VP:",-100*times)
        if rewardTix>0:
            print("- Tix:",rewardTix)
            self.addTix(rewardTix)
        if rewardCJ>0:
            print("- Cuppa Joe(s):",rewardCJ)
            self.getItem("Cuppa Joe",rewardCJ)
        if rewardx2>0:
            print("- Twofoldness(es):",rewardx2)
            self.getItem("Twofoldness",rewardx2)
        if rewardx3>0:
            print("- Fortune(s) of The Devil:",rewardx3)
            self.getItem("Fortune of The Devil",rewardx3)
        del rewardTix
        del rewardCJ
        del rewardx2
        del rewardx3
        del result  
        print("After:")
        self.printData()

    def addVP2(self,amount):
        print("Before:")
        self.printData()
        print()
        self.VP+=amount
        update(self.filename,"VP",self.VP)
        print("After:")
        self.printData()

    def addVP(self,amount):#    USABLE
        print("Before:")
        self.printData()
        print()
        if ("Twofoldness" in self.currentBuff) and ("Fortune of The Devil" in self.currentBuff):
                self.VP+=amount*5
                self.currentBuff["Fortune of The Devil"]-=1
                if self.currentBuff["Fortune of The Devil"]==0:
                    del self.currentBuff["Fortune of The Devil"]
                self.currentBuff["Twofoldness"]-=1
                if self.currentBuff["Twofoldness"]==0:
                    del self.currentBuff["Twofoldness"]
                update(self.filename,"VP",self.VP)
                update(self.filename,"currentBuff",self.currentBuff)
        elif ("Twofoldness" in self.currentBuff) or ("Fortune of The Devil" in self.currentBuff):
            if "Twofoldness" in self.currentBuff:
                self.VP+=amount*2
                self.currentBuff["Twofoldness"]-=1
                if self.currentBuff["Twofoldness"]==0:
                    del self.currentBuff["Twofoldness"]
                update(self.filename,"VP",self.VP)
                update(self.filename,"currentBuff",self.currentBuff)
            elif "Fortune of The Devil" in self.currentBuff:
                self.VP+=amount*3
                self.currentBuff["Fortune of The Devil"]-=1
                if self.currentBuff["Fortune of The Devil"]==0:
                    del self.currentBuff["Fortune of The Devil"]
                update(self.filename,"VP",self.VP)
                update(self.filename,"currentBuff",self.currentBuff)
        else:
            self.VP+=amount
            update(self.filename,"VP",self.VP)
        print("After:")
        self.printData()
        
    def use(self,buff,quant=1):#    USABLE
        print("Before:")
        self.printData()
        if buff=="x2":
            if "Twofoldness" in self.Inventory and self.Inventory["Twofoldness"]>=quant:
                self.removeItem("Twofoldness",quant)
                self.getBuff("Twofoldness",quant)
        elif buff=="x3":
            if "Fortune of The Devil" in self.Inventory and self.Inventory["Fortune of The Devil"]>=quant:
                self.removeItem("Fortune of The Devil",quant)
                self.getBuff("Fortune of The Devil",quant)
        elif buff=="MB":
            if "Mystery Box" in self.Inventory and self.Inventory["Mystery Box"]>=quant:
                self.removeItem("Mystery Box",quant)
                for i in range(quant):
                    randomMessage=[
                        "You've just taken the first step into the unknown. What could be hiding inside the Mystery Box?",
                        "Congratulations, you've opened the Mystery Box. What will you find inside?",
                        "Well done, Player! The Mystery Box awaits with its secrets. What will you discover?",
                        "You've opened the door to a world of possibilities. What treasures lie within the Mystery Box?",
                        "You've uncovered the Mystery Box, but what lies inside is still a mystery. Are you ready to find out?"
                    ]
                    result=random.choices(randomMessage,weights=[1,1,1,1,1],k=1)
                    print(result[0])
                print()
        elif buff=="CJ":
            if "Cuppa Joe" in self.Inventory and self.Inventory["Cuppa Joe"]>=quant:
                self.removeItem("Cuppa Joe",quant)
        else:
            print("Error when using Buff",buff)
            print()
        print("After:")
        self.printData()

    def subVP(self,amount):
        self.VP-=amount
        if self.VP<0:
            self.VP=0
        update(self.filename,"VP",self.VP)

    def addTix(self,amount):
        self.Tix+=amount
        update(self.filename,"Tix",self.Tix)

    def subTix(self,amount):
        self.Tix-=amount
        if self.Tix<0:
            self.Tix=0
        update(self.filename,"Tix",self.Tix)

    def getItem(self,item,quant=1):
        if item in self.Inventory:
            self.Inventory[item]+=quant
            update(self.filename,"Inventory",self.Inventory)
        else:
            self.Inventory.update({item:quant})
            update(self.filename,"Inventory",self.Inventory)

    def getBuff(self,buff,quant=1):
        if buff in self.currentBuff:
            self.currentBuff[buff]+=quant
            update(self.filename,"currentBuff",self.currentBuff)
        else:
            self.currentBuff[buff]=quant
            update(self.filename,"currentBuff",self.currentBuff)

    def removeItem(self,item,quant=1):
        if item in self.Inventory:
            self.Inventory[item]-=quant
            if self.Inventory[item]<=0:
                del self.Inventory[item]
            update(self.filename,"Inventory",self.Inventory)
        else:
            return

    def removeBuff(self,buff,quant=1):
        if buff in self.currentBuff:
            self.currentBuff[buff]-=quant
            if self.currentBuff[buff]<=0:
                del self.currentBuff[buff]
            update(self.filename,"currentBuff",self.currentBuff)
        else:
            return
        
    def changeUsername(self,name):
        print("Before:")
        self.printData()
        print()
        self.username=name
        update(self.filename,"username",self.username)
        print("After:")
        self.printData()
        print()