import mysql.connector as sql
c=sql.connect(host='localhost',user='root',passwd='9205',database='mobile')
c1=c.cursor()

def newrecord() :
    pid=int(input('Enter the phone code : '))
    pn=((input('enter the name of phone :')).upper()).strip()
    brand=input('enter the brand of phone :').upper()
    ava=int(input('Enter the number of phones availabla in stock :'))
    price=int(input('enter the cost price of phone  : '))
    sp=int(input('enter the selling price of phone  : '))
    c1.execute("insert into mobile (phone_code,phone_name,brand,stock_available,cost_price,Selling_price) values({},'{}','{}',{},{},{})".format(pid,pn,brand,ava,price,sp))
    c.commit()    
    print('entry succesful')

def searching() :
    zen=((input("enter the mobile name on which you want to see the details ")).upper()).strip()
    c1.execute("select * from mobile ")
    kvl=c1.fetchall()
    for sdc in kvl :
        if sdc[1]==zen :
            print(" PHONE :- ",sdc[1],"\n PHONE CODE :- ",sdc[0],"\n PHONE BRAND :- ",sdc[2]," \n COST PRICE :- ",sdc[4],"\n AVAILABLE STOCK :- ",sdc[3],"\n SELLING PRICE :- ",sdc[5])
         
def updating():
    nez=((input("enter the phone name whose stock you want to update ")).upper()).strip()
    noms=int(input("enter the new stock value "))
    c1.execute("select * from mobile ")
    cgh=c1.fetchall()
    for cg in cgh :
        if cg[1]==nez.upper():
            sqs="update mobile SET stock_available= %s where phone_name = %s "
            varc=(noms,nez)
            c1.execute(sqs,(varc))
            c.commit()
            print("successfully updated")
    
def buying():
    t=1
    c1.execute("select * from mobile")
    d=c1.fetchall()
    print("----------------------------------------------------------------------------------------")
    print("    S.NO   -    CODE    -       PHONE       -      BRAND     -  AVAILABLE  -   PRICE ")
    print("----------------------------------------------------------------------------------------")
    for i in d :
        print("    ",t,"    -   ",i[0],"    -    ",i[1],"    -    ",i[2],"    -    ",i[3],"     -  ",i[5])
        print("-----------------------------------------------------------------------------------------")
                
        t+=1
    cnu=((input('enter the customer gmail ID : ')).upper()).strip()
    phnn=((input('enter the name of phone bought : ')).upper()).strip()
    cname=((input('enter your name  : ')).upper()).strip()
    q=int(input('enter the quantity of phone : '))
    ntr=input('enter your phone number  : ')
    dtop=((input('enter the date  : ')).upper()).strip()
    adr=((input('enter your address  : ')).upper()).strip()

    c1.execute("select * from mobile ")
    fmoz=c1.fetchall()
    pz=0
            
    for rdoe in fmoz :
        if rdoe[1]==phnn :
            pz=rdoe[0]
            amto=rdoe[5]
    print("1 CASH")
    print("2 CARD")
    print("3 PAYTM")
    pnt=int(input('enter payment mode : '))
    pmmt=" "
    if pnt==1:
        pmmt+='CASH'
    elif pnt==2 :
        pmmt+='CARD'
    elif pnt==3 :
        pmmt+='PAYTM'
    
    print("------------------------------------------------------------------")
    print("                  SHIVA ELECTRONICS                               ")
    print("------------------------------------------------------------------")
    print("------------------------------------------------------------------")
    print("                                                                  ")
    print("                                              DATE=",dtop ,"      ")
    print("                                                                  ")
    print("  GMAIL ID=",cnu,"                                                ")
    print("                                                                  ")
    print("  NAME=",cname,"                                                  ")
    print("                                                                  ")
    print("  NUMBER=",ntr,"                                                  ")
    print("                                                                  ")
    print("  ADDRESS=",adr,"                                                 ")
    print("------------------------------------------------------------------")
    print("------------------------------------------------------------------")
    print("  PHONE CODE    PHONE NAME     PRICE    quantity    payable amount")
    print("                                                                  ")
    print("   ",pz,"        ",phnn,"   ",amto,"    ",q,"          ",amto*q," ")
    print("                                                                  ")
    print("  PAYMENT MODE = ",pmmt,"                                         ")
    print("                                                                  ")
    print("  THE AMOUNT OF ",amto*q," HAS BEEN RECEIVED THROUGH ",pmmt,".    ")
    print("                                                                  ")
    print("                     THANK YOU VISIT AGAIN                        ")
    print("------------------------------------------------------------------")
    
    c1.execute("select * from mobile")
    pmr=c1.fetchall()
    ln=0
    for op in pmr :
        if op[1]==phnn :
            ln=(amto*q)-(op[4]*q)
    for un in pmr :
        if un[0] == pz  :
            unhj=un[3]-q
            sql="update mobile SET stock_available= %s where phone_code= %s "
            val=(unhj,pz)
            c1.execute(sql,(val))
            c.commit()       
    c1.execute("insert into customer(gmail_id,phone_code,customer_name,phone_name,date_of_purchase,selling_price,quantity,amount_paid,mode_of_payment,customer_number,customer_address,PROFIT)value('{}',{},'{}','{}','{}',{},{},{},'{}','{}','{}',{})".format(cnu,pz,cname,phnn,dtop,amto,q,amto*q,pmmt,ntr,adr,ln))
    c.commit()
    
def oldbill():
    gmld=((input("enter your gmail id : ")).upper()).strip()
    drss=((input("enter your name : ")).upper()).strip()
    c1.execute("select * from customer  ")
    nm=0
    vru=c1.fetchall()
    for ml in vru :
      if ml[0]==gmld and ml[2]==drss:
        print("--------------------------------------------------------------")
        print("                       SHIVA ELECTRONICS                      ")
        print("--------------------------------------------------------------")
        print("--------------------------------------------------------------")
        print("                                                              ")
        print("                                           DATE=",ml[4],"     ")
        print("                                                              ")
        print("  GMAIL ID=",ml[0],"                                          ")                                                  
        print("                                                              ")
        print("  NAME=",ml[2],"                                              ")
        print("                                                              ")
        print("  NUMBER=",ml[9],"                                            ")
        print("                                                              ")
        print("  ADDRESS=",ml[10],"                                          ")
        print("--------------------------------------------------------------")
        print("--------------------------------------------------------------")
        print("  PHONE CODE   PHONE NAME    quantity   PRICE                 ")
        print("                                                              ")
        print("    ",ml[1],"     ",ml[3],"      ",ml[6],"     ",ml[7],"      ")
        print("                                                              ")
        print("  PAYMENT MODE = ",ml[8],"                                    ")
        print("                                                              ")
        print("  THE AMOUNT OF ",ml[7]," HAS BEEN RECEIVED THROUGH ",ml[8],".")
        print("                                                              ")
        print("                     THANK YOU VISIT AGAIN                    ")
        print("--------------------------------------------------------------")
      else :
        nm=1
    if nm==1:
        print(" DETAILS NOT MATCHED ")

        
if c.is_connected:
      print('   ****************** SHIVA ELECTRONICS *******************    ')
      print(' 1 . ADMIN ')
      print(' 2 . CUSTOMER ')
      print("                                              ")
      choice=int(input('enter the choice : '))
      if choice==1:
            passw=int(input("enter the password : "))
            if passw==9205 :
                  print("                                              ")
                  print('  1~ENTRY FOR A NEW MOBILE ')
                  print('  2~TO SEARCH FOR A MOBILE ')
                  print('  3~TO UPDATE THE STOCK AVAILABLE ')
                  print("                                              ")
                  choose=int(input('enter the choice for entry:'))
                  print("                                              ")
                  if choose==1:
                          newrecord()
                  elif choose==2:
                          searching()
                  elif choose==3 :
                          updating()    
                  else :
                          print(" INVALID CHOICE ")     
            else :
                  print(" INCORRECT PASSWORD  ")


      elif choice==2:
            print(' 1~ TO BUY A PHONE ')
            print(" 2~ TO SEARCH FOR AN OLD BILL ")
            bi=int(input('enter the choice'))
            if bi==1 :
                    buying()
            elif bi==2:
                    oldbill()             
            else : 
                    print(" INVALID CHOICE ")
      else :
            print("invalid choice ")
else :
     print(" NOT CONNECTED ")   
