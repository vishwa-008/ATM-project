import time,sys,os
class atm:
    def __init__(self,bal):
        self.bal=bal

    def again(self):
        time.sleep(1)
        rest=int(input('''
                   1.back
                   2.quit
'''))
        if rest==1:
            o1.transaction()
            o1.again()
        elif rest==2:
            print('''
                   please collect your card
                *****THANK YOU , COME AGAIN*****
                     ****CODE BY VISHWA ****''')
        else:
            print("invalid choice")


    def language(self):
        lan=int(input('''
>>>>>>>>>>>>>>>>>>>>>Please select your language<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                         1.Tamil
                         2. english
'''))




    def withdraw(self):
    
        withd=int(input("please enter your 4 digit pin:"))
        if withd==1234:
            withdamt=int(input("please enter your amount:"))
            if withdamt>=100 and withdamt<=self.bal:
                print("please collect your amount")
                self.bal=self.bal-withdamt
                print("your balance is",self.bal)
            else:
                print("you are unable to withdraw your amount")
        else:
            print("your password is incorrect")
            balan=int(input("if you want to enter again press 1"))
            if balan==1:
                o1.withdraw()

        


    def deposit(self):
        dep=int(input('''
                     cash must be above 100rs
                    please insert your cash
'''))
        if dep>=100:
                print(" your amount i succesfully deposited")
                self.bal=self.bal+dep
                print("your balance is",self.bal)
    
        else:
            print("your amount is below 100")

    def balance(self):
        balanc=int(input("please enter your 4 digit pin:"))
        if balanc==1234:
            print("processing...")
            time.sleep(3)
            print("your balance is",self.bal)
            time.sleep(1)
        else:
            print("your password is incorrect")
            balan=int(input("if you want to enter again press 1"))
            if balan==1:
                o1.balance()

    def accounttype(self):
        accho=int(input('''
>>>>>>>>>>>>>>>>>>>>>>>>choose your account type<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                            1.savings A/C
                            2.current A/C
'''))


    


    def transaction(self):
        transty=int(input('''
>>>>>>>>>>>>>>>>>>>please choose your transaction<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                            1.banking
                            2.registration
                            3.mini statement
                            4.services
                            5.Balance enquiry
                            6.withdraw amount
                            7.deposit money
                            
'''))

    
        if transty==1:
            print("please contack your nearby bank")
              
        elif transty==2:
            print("curretly registration not available")

        elif transty==3:
            print("currently registration not available")

        elif transty==4:
            print("please call 1234")

        elif transty==5:
            o1.balance()

        elif transty==6:
            o1.withdraw()

        elif transty==7:
            o1.deposit()

        else:
            print("invalid choice")

    



o1=atm(1000)
print("=========================WELCOME TO  MARI AMMAN ATM ============================")
print("please insert your card and wait for 5 seconds")
time.sleep(3)
msg="Do not remove your card"
msg2="processing...."
for char in msg:
    sys.stdout.write(char)
    time.sleep(0.1)
print("")
for char2 in msg2:
    sys.stdout.write(char2)
    time.sleep(0.1)

time.sleep(3)
o1.language()
o1.accounttype()
o1.transaction()
o1.again()








    
                  
   
 
