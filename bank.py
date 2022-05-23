#             ------------------------------------------------------------------------------------------------------
#             --------------         The Code is writen and edited in PyCharm        -------------------------------
#             ------------------------------------------------------------------------------------------------------

import datetime, time, re, json
from datetime import date
from datetime import datetime
from json import JSONDecodeError

class Bank:
    def __init__(self):
        pass
    def Register(self,a_type, a_no, pin_no, name, phone_number, address):
        f = open('Accounts.json', 'r+')
        d = {
            'Type': a_type,
            'Account_Number': a_no,
            'Pin_No': pin_no,
            'Details': {
                'Name': name,
                'Phone_Number': phone_number,
                'Created_Date': datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
                'Address': address
            },
            'Transections': {
                'Saving_Amount': 0,
                'History': []
            }
        }

        try:
            content = json.load(f)
            if len(content) == 0:
                l = []
                l.append(d)
                json.dump(l, f)
                f.close()
                return True
            else:
                drd = False
                for i in content:
                    if i['Type'] == a_type:
                        if i['Account_Number'] == a_no:
                            drd = True
                            break

                if drd == False:
                    content.append(d)
                    f.seek(0)
                    f.truncate()
                    json.dump(content, f)
                    f.close()
                    return True
                else:
                    print('You have Account already\nPleas check details')
        except JSONDecodeError:
            l = []
            l.append(d)
            json.dump(l, f)
            f.close()
            return True

    def Log_In(self,type, a_no, pin_no):
        f = open('Accounts.json', 'r+')
        content = json.load(f)

        src = False
        for i in content:
            if i['Type'] == type:
                if i['Account_Number'] == a_no and i['Pin_No'] == pin_no:
                    src = True
                    f.close()
                    break

        if src == True:
            return True
        else:
            f.close()
            print('Your creditionals are wrong')
            return False


    def view_Balence(self, type, a_no):
        f = open('Accounts.json', 'r+')
        try:
            content = json.load(f)
            drd = False
            for i in content:
                    if i['Type'] == type:
                        if i['Account_Number'] == a_no:
                            print('Account Number is : ', a_no)
                            print('Account Holder Name is : ', i['Details']['Name'])
                            print('Your current account balence is : ', i['Transections']['Saving_Amount'])
                            drd = True
                            f.close()
                            break

            if drd == True:
                return True
            else:
                f.close()
                print('Some errors are occured\nSorry for inconvience\nTry again please')
                return False
        except JSONDecodeError:
            f.close()
            print('some error is occuring')
            return False

    def Statement(self, type, a_no):
        f = open('Accounts.json', 'r+')
        try:
            content = json.load(f)
            drd = False
            for i in content:
                if i['Type'] == type:
                    if i['Account_Number'] == a_no:
                        print('Account Number is : ', a_no)
                        print('Account Holder Name is : ', i['Details']['Name'])
                        print('Your current account balence is : ', i['Transections']['Saving_Amount'])
                        if len(i['Transections']['History']) < 5:
                            for j in (i['Transections']['History']):
                                print(j)
                            f.close()
                        else:
                            print('The last 5 Transections are - ')
                            z = 0
                            for j in (i['Transections']['History']):
                                z += 1
                                print(j)
                                if z == 5:
                                    break
                            f.close()
                        drd = True
                        break

            if drd == True:
                return True
            else:
                f.close()
                print('Some errors are occured\nSorry for inconvience\nTry again please')
        except JSONDecodeError:
            f.close()
            print('some error is occuring')
            return False

    def Credit(self, type, a_no, balence):
        f = open('Accounts.json', 'r+')
        try:
            content = json.load(f)
            drd = False
            for i in content:
                if i['Type'] == type:
                    if i['Account_Number'] == a_no:
                        g = {'Transection_Type': 'Credit',
                             'Credit_amount': balence,
                             'Date_Time': datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
                             }
                        i['Transections']['History'].insert(0, g)
                        i['Transections']['Saving_Amount'] += balence
                        print('Account Number is : ', a_no)
                        print('Account Holder Name is : ', i['Details']['Name'])
                        print('Crediting amount is : ', balence)
                        print('Your current account balence is : ', i['Transections']['Saving_Amount'])
                        drd = True
                        f.seek(0)
                        f.truncate()
                        json.dump(content, f)
                        f.close()
                        break

            if drd == True:
                return True
            else:
                f.close()
                print('Some errors are occured\nSorry for inconvience\nTry again please')
                return False
        except JSONDecodeError:
            f.close()
            print('some error is occuring')
            return False

    def Debit(self, type, a_no, balence):
        f = open('Accounts.json', 'r+')
        try:
            content = json.load(f)
            drd = False
            for i in content:
                if i['Type'] == type:
                    if i['Account_Number'] == a_no:
                        if (i['Transections']['Saving_Amount'] - balence) < 500:
                            print('Your current account balence is : ', i['Transections']['Saving_Amount'],
                                  '\nYou need to maintain minimum balence ie Rs.500/- so please draw another amount !')
                        else:
                            g = {'Transection_Type': 'Debit',
                                 'Debit_amount': balence,
                                 'Date_Time': time.asctime(time.localtime(time.time()))
                                 }
                            i['Transections']['History'].insert(0, g)
                            i['Transections']['Saving_Amount'] -= balence
                            print('Account Number is : ', a_no)
                            print('Account Holder Name is : ', i['Details']['Name'])
                            print('Crediting amount is : ', balence)
                            print('Your current account balence is : ', i['Transections']['Saving_Amount'])
                            drd = True
                            f.seek(0)
                            f.truncate()
                            json.dump(content, f)
                            f.close()
                            break

            if drd == True:
                return True
            else:
                f.close()
                print('Some errors are occured\nSorry for inconvience\nTry again please')
        except JSONDecodeError:
            f.close()
            print('some error is occuring')
            return False

bank=Bank()

#cd = bank.Credit('S', 781192968618, 50000)
#st=bank.Statement('S',781192968618)
#print(st)


vi1 = 0
while (vi1 != 3):
    print('1. Register')
    print('2. Log-in')
    print('3. Exit')

    try:
        vi1 = int(input('Enter your choice : '))
    except ValueError:
        print('You are entered invalid choice, Please enter valid choice')
        continue
    
    # Register ---------------------------------------------------------------------------------------
    
    if vi1 == 1:
        print('Choose your Account type')
        print('1. Bussiness account')
        print('2. Checking account')
        print('3. Saving account')
        try:
            vi2 = int(input('Enter your Bank account type : '))
        except ValueError:
            print('You are entered invalid choice, Please enter valid choice')
            continue
        a_type = None
        if vi2 == 1:
            a_type = 'B'
        elif vi2 == 2:
            a_type = 'C'
        elif vi2 == 3:
            a_type = 'S'
        else:
            print('You are entered invalid choice, Please enter valid choice')
            continue
        ad_nu = input(
            'Enter Your Adhar number : \nNote: The adhar number should have 12 numbers and it should not contain any spaces')
        if bool(re.match('[0-9]{12}', ad_nu)):
            ad_nu = int(ad_nu)
        else:
            print('Entered adhar number is invalid')
            ad_nu = input(
                'Enter Your Adhar number : \nNote: The adhar number should have 12 numbers and it should not contain any spaces')
            if bool(re.match('[0-9]{12}', ad_nu)):
                ad_nu = int(ad_nu)
            else:
                print('invalid adhar')
                continue
        name = input('Enter Your Name : ')
        if bool(re.match('[A-Za-z]{3,50}', name)):
            name = name
        else:
            print('Entered Name is invalid')
            name = input('Enter Your Name : ')
            if bool(re.match('[A-Za-z]{5,50}', name)):
                name = name
            else:
                print('the name should contain minimum 3 charecherstics to 50 ')
                continue
        mob_nu = input('Enter Your 10 digit Mobile Number : ')
        if bool(re.match('[6-9]{1}[0-9]{9}', mob_nu)):
            mob_nu = int(mob_nu)
        else:
            print('Entered Mobile Number is invalid ')
            mob_nu = input('Enter Your Name : ')
            if bool(re.match('[6-9]{1}[0-9]{9}', mob_nu)):
                mob_nu = int(mob_nu)
            else:
                continue
        Address = input('Enter Your Address : ')
        pin_nu = input('Enter Your 4 digit PIN Number : ')
        if bool(re.match('[0-9]{4}', pin_nu)):
            pin_nu = pin_nu
        else:
            print('Entered PIN Number is invalid ')
            pin_nu = input('Enter Your 4 digit PIN Number : ')
            if bool(re.match('[0-9]{4}', pin_nu)):
                pin_nu = pin_nu
            else:
                continue
        pin_nu2 = input('Enter you PIN number to confirm PIN')
        if pin_nu == pin_nu2:
            pin_nu = int(pin_nu)
            print('Your account is creating\nIN-PROCESS')
        else:
            print('The PIN Number is incorrect')
            continue
        regi = bank.Register(a_type, ad_nu, pin_nu, name, mob_nu, Address)
        if regi == True:
            print('Your Account is created')
            print('Your Account type is : ', a_type)
            print('Yoru Account Number is : ', ad_nu)
            print('Your PIN Number is : ', pin_nu)
            print(
                "Please don't forget yoru creditionals\nNote: \nC - Cheching account\nB - Business account\nS - Savings aacount")
        else:
            print(
                'Sorry for inconvience, because of some technical issues your account is not created\nPlease tye aggain,\nThank you !')
            
# Log-in    ---------------------------------------------------------------------------------
    
    if vi1 == 2:
        print('Enter details to log-in to your account')
        print('1. Bussines account\n2. Checking account\n3. Saving account')
        try:
            vi3 = int(input('Choose and enter you account type \nEx:- 1 or 2 or 3 '))
        except ValueError:
            print('Entered input is invalid')
            continue
        a_type = None
        if vi3 == 1:
            a_tyep = 'B'
        elif vi3 == 2:
            a_type = 'C'
        elif vi3 == 3:
            a_type = 'S'
        else:
            print('Entered input is invalid')
            continue
        ad_nu = input(
            'Enter Your Adhar number : \nNote: The adhar number should have 12 numbers and it should not contain any spaces')
        if bool(re.match('[0-9]{12}', ad_nu)):
            ad_nu = int(ad_nu)
            pass
        else:
            print('Entered adhar number is invalid')
            ad_nu = input(
                'Enter Your Adhar number : \nNote: The adhar number should have 12 numbers and it should not contain any spaces')
            if bool(re.match('[0-9]{12}', ad_nu)):
                ad_nu = int(ad_nu)
                pass
            else:
                continue
        pin_nu = input('Enter Your 4 digit PIN Number : ')
        if bool(re.match('[0-9]{4}', pin_nu)):
            pin_nu = int(pin_nu)
            pass
        else:
            print('Entered PIN Number is invalid ')
            ad_nu = input('Enter Your 4 digit PIN Number : ')
            if bool(re.match('[0-9]{4}', pin_nu)):
                pin_nu = int(pin_nu)
                pass
            else:
                continue
        login = bank.Log_In(a_type, ad_nu, pin_nu)
        if login == True:
            print('Succesfully logged in')
            vi2 = 0
            while (vi2 != 5):
                print('1. Credit amount')
                print('2. Debit amount')
                print('3. View account balence')
                print('4. Account Statement')
                print('5. Exit')
                try:
                    vi2 = int(input('Chosse and enter your choice by option\nEx:-1 or 2.....'))
                except ValueError:
                    print('Entered choice is invalid')
                    continue
                    
# Credit    -----------------------------------------------------------------------------
                
                if vi2 == 1:
                    try:
                        cr_am = int(input('Enter amount how much want you credit\nEx:-500,100  '))
                    except ValueError:
                        print('Entered amount is invalid amount')
                        continue
                    if (cr_am < 1) or (cr_am%100) != 0:
                        print('The Hundred multiple amounts only acceptable and Zero & negitive amounts are not valid')
                        continue
                    else:
                        credit = bank.Credit(a_type, ad_nu, cr_am)
                        if credit == True:
                            print('Successfully credited your amount')
                            continue
                        else:
                            print('Due to some techincal issues, process is not compleated\nTry again please')
                            continue

# Debit amount -------------------------------------------------------------------------------------------------
                elif vi2 == 2:
                    try:
                        db_am = int(input('Enter amount how much want you Debit\nEx:-500,100  '))
                    except ValueError:
                        print('Entered amount is invalid')
                    if (db_am < 1) or (db_am%100 != 0):
                        print('The Hundred multiple amounts only acceptable and Zero & negitive amounts are not valid')
                    else:
                        debit = bank.Debit(a_type, ad_nu, db_am)
                        if debit == True:
                            print('Successfully debited your amount')
                            continue
                        else:
                            print('Due to some techincal issues, process is not compleated\nTry again please')
                            continue

# Checking bank balence ------------------------------------------------------------------------------------------------
                elif vi2 == 3:
                    v_am = bank.view_Balence(a_type, ad_nu)
                    continue

# Bank Statement -------------------------------------------------------------------------------------------------------
                elif vi2 == 4:
                    a_stat = bank.Statement(a_type, ad_nu)
                    continue
                else:
                    print('Entered values is invalid')

    else:
        if vi1 == 3:
            continue
        else:
            print('Entered value is invalid')
            continue

