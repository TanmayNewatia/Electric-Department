#Project(By Tanmay Newatia)
     
def vspacing():
    print("\n",end=" ")

def hspacing():
    print("\t "*10,"\t",end=" ")

def line():
    print("-"*195)

def invalin():
    print("Invalid Input, Please try again.".center(195,"!"))

def con1():
    global con,cur
    con=mysql.connector.connect(host='localhost',user='root',password='root')
    #if con.is_connected:
        #print("Connection Established.")                                       #For Checking Connection with Mysql
    cur=con.cursor()

def emplogin():
    global rowcount,i,con,cur,bdata,empid,log_in_v,cur2,con2,tsli
    con1()
    con2=mysql.connector.connect(host='localhost',user='root',password='root',database='emplogindetails')
    cur2=con2.cursor()
    for i in range(3,0,-1):
        vspacing()
        hspacing()
        empid=str(input("Employee ID : "))
        query='select * from emplogindetails where UserID="{}"'.format(empid)
        cur2.execute(query)
        bdata=cur2.fetchall()
        rowcount=cur2.rowcount
        if rowcount==1:
            if bdata[0][2]=="BLOCKED":
                vspacing()
                print("Sorry! Your Account is Blocked, Please request for Unblocking.".center(195,"!"))
                break
            from getpass import getpass
            hspacing()
            emppass=getpass(prompt="\t\t\t\t\t\t\t\t\t\t\t Password : ", stream=None)
            query='select * from emplogindetails where UserID="{}" and Password="{}"'.format(empid,emppass)
            cur2.execute(query)
            cur2.fetchall()
            rowcount=cur2.rowcount
            if rowcount==1:
                from time import localtime
                log_in=localtime()
                log_in_v=str(log_in[0])+"-"+str(log_in[1])+"-"+str(log_in[2])+"  "+str(log_in[3])+":"+str(log_in[4])+":"+str(log_in[5])
                tsli=(log_in[3]*60+log_in[4])*60+log_in[5]                                                                                  #tsli:- Totalsecondlogin
                query='insert into emplogs values("{}","{}",{},{})'.format(empid,log_in_v,"NULL","NULL")
                cur2.execute(query)
                con2.commit()
                vspacing()
                print("Successfully Logged In".center(195,'='))
                vspacing()
                hspacing()
                print("Hello",empid.capitalize())
                break
            elif i!=1:
                vspacing()
                print(("Incorrect Employee ID or Password, Please try again.({} Attempts Left)".format(i-1)).center(195,'!'))
            else:
                query="update emplogindetails set account_status='BLOCKED' where UserID='{}'".format(empid)
                cur2.execute(query)
                con2.commit()
                vspacing()
                print("Account Blocked.".center(195,'='))
        elif i!=1:
            vspacing()
            print("No User Found, Please try again.({} Attempts Left)".format(i-1).center(195,'!'))
        else:
            vspacing()
            print("Sorry, You Exceed the Attempts Limit.".center(195,"="))
            
def cuslogin():
    global rowcount,i,cur,con,cusid,cdata,sisu,na
    vspacing()
    hspacing()
    cusid=str(input("Customer ID : "))
    query='select * from cuslogindetails where CustomerID="{}"'.format(cusid)
    cur.execute(query)
    cdata=cur.fetchall()
    crowcount=cur.rowcount
    while crowcount==0:
        vspacing()
        print("No Account Found. Please Try Again or Create New Account.".center(195,"!"))
        vspacing()
        hspacing()
        na=str(input("""Do you want to Sign 'U'p
                        \t\t\t\t\t\t\t\t or Try 'A'gain
                        \t\t\t\t\t\t\t\t or 'Q'uit? : """))
        while na not in ('U','u','A','a','q','Q'):
            vspacing()
            invalin()
            vspacing()
            hspacing()
            na=str(input("""Do you want to Sign 'U'p
                            \t\t\t\t\t\t\t\t or Try 'A'gain
                            \t\t\t\t\t\t\t\t or 'Q'uit? : """))
        if na in ("U","u"):
            break
        if na in ("a","A"):
            vspacing()
            hspacing()
            cusid=str(input("Customer ID : "))
            query='select * from cuslogindetails where CustomerID="{}"'.format(cusid)
            cur.execute(query)
            cdata=cur.fetchall()
            crowcount=cur.rowcount
        if na in ("Q","q"):
            vspacing()
            print("Thanks for Using Electricity Department Application.".center(195,"="))
            break
    if crowcount!=0 or na in ("a","A"):
        for i in range(3,0,-1):
            if na not in ("a","A","U","u") and sisu not in ("I","i"):
                vspacing()
                hspacing()
                cusid=str(input("Customer ID : "))
                query='select * from cuslogindetails where CustomerID="{}"'.format(cusid)
                cur.execute(query)
                cdata=cur.fetchall()
                crowcount=cur.rowcount
            if crowcount==1:
                if cdata[0][3]=="BLOCKED":
                    vspacing()
                    print("Sorry! Your Account is Blocked, Please request for Unblocking.".center(195,"!"))
                    break
                from getpass import getpass
                hspacing()
                cuspass=getpass(prompt="\t\t\t\t\t\t\t\t\t\t\t Password : ", stream=None)
                query='select * from cuslogindetails where CustomerID="{}" and Password="{}"'.format(cusid,cuspass)
                cur.execute(query)
                cur.fetchall()
                c2rowcount=cur.rowcount
                if c2rowcount==1:
                    vspacing()
                    print("Successfully Logged In".center(195,'='))
                    vspacing()
                    hspacing()
                    print("Hello",cusid.capitalize())
                    break
                elif i!=1:
                    vspacing()
                    print(("Incorrect Customer ID or Password, Please try again.({} Attempts Left)".format(i-1)).center(195,'!'))
                else:
                    query="update cuslogindetails set account_status='BLOCKED' where CustomerID='{}'".format(cusid)
                    cur.execute(query)
                    con.commit()
                    vspacing()
                    print("Account Blocked.".center(195,'='))
                    query='select * from cuslogindetails where CustomerID="{}"'.format(cusid)
                    cur.execute(query)
                    cdata=cur.fetchall()

def finaldec():
    global userdec
    vspacing()
    hspacing()
    userdec=str(input("Are you sure, 'Y'es/'N'o  : "))
    while userdec not in ('Y','y','N','n'):
        vspacing()
        invalin()
        vspacing()
        hspacing()    
        userdec=str(input("Are you sure, 'Y'es/'N'o : "))

def databasecreator():
    global con,cur,databasename,confirmation
    con1()
    cur.execute("create database if not exists {}".format('employee'))
    databasename='employee'
    con=mysql.connector.connect(host='localhost',user='root',password='root',database=databasename)
    cur=con.cursor()

def tablecreator():
    global con,cur,databasename,tablename,columnlist,columntypelist,tabledatatype,choicetable
    cur.execute("create table if not exists cus_info(Customer_No bigint primary key,Meter_No varchar(30) unique,Date_of_connection date not null,Name varchar(50) not null,Address varchar(200) not null,Mobile_No bigint not null,Email_ID varchar(50) not null,Aadhar_Card_No bigint unique,BPL char(1) not null,BPLNo varchar(30) unique,Zone varchar(30) not null,District varchar(30) not null,Tariff_Category varchar(50) not null,Sactioned_Load varchar(15) not null)")
    tablename='cus_info'
    cur.execute("create table if not exists bills(Customer_No bigint not null, Month varchar(30) not null, Billamount float not null, foreign key bills(Customer_NO) references cus_info(Customer_No))")
    choicetable='bills'
    cur.execute("create table if not exists del_cus_info(Customer_No bigint primary key,Meter_No varchar(30) unique,Date_of_connection date not null,Name varchar(50) not null,Address varchar(200) not null,Mobile_No bigint not null,Email_ID varchar(50) not null,Aadhar_Card_No bigint unique,BPL char(1) not null,BPLNo varchar(30) unique,Zone varchar(30) not null,District varchar(30) not null,Tariff_Category varchar(50) not null,Sactioned_Load varchar(15) not null,Reason varchar(50))")
    
def recordcreator():
    global con,cur,databasename,tablename,columnlist,columntypelist,tabledatatype,choicetable
    cur.execute("desc {}".format(tablename))
    tabledata=list(cur.fetchall())
    rowcount=cur.rowcount                                                                                       #no of rows from table received
    cur.execute("select Customer_No,Meter_No from {}".format(tablename))
    tabledata1=cur.fetchall()
    tdl=[]                                                                                                      #tdl:-tabledatalist    
    tdtl=[]                                                                                                     #tdlt:-tabledatatypelist    
    col=[]                                                                                                      #col:- columnconstraintlist
    for i in range(0,rowcount):
        tdl.append(tabledata[i][0])
        tdtl.append(tabledata[i][1])
        col.append(tabledata[i][3])
    cur.execute("select * from {}".format(tablename))
    recorddata=cur.fetchall()
    rowcount=cur.rowcount
    if recorddata!=[]:
        vspacing()
        print("Last Entered Record is: ".center(195,' '))
        vspacing()
        for i in range(0,len(tabledata)):
                print("\t"*10,tabledata[i][0].center(20,' '),":",str(recorddata[rowcount-1][i]).center(20,' '))
    else:
        vspacing()
        print("No Records Present.".center(195,'-'))
    while True:
        vl=[]                                                                                                       #valuelist to be empty(assigning valuelist)
        i=0
        while i<len(tdl):
            if 'double' not in tdtl[i] and 'float' not in tdtl[i] and 'int' not in tdtl[i]:
                vspacing()
                hspacing()
                vs="Enter Value for , "+tdl[i].capitalize()+" : "                                                              #vs: valuestring
                if tdl[i]=="Tariff_Category":
                    vst="Enter Value for , "+tdl[i].capitalize()+''' \n\t\t\t\t\t\t\t\t\t\t\t\tDO : Domestic
                                                                    \t\t\t\tND : Non-Domestic
                                                                    \t\t\t\tIN : Industrial
                                                                    \t\t\t\tAG : Agriculture
                                                                    \t\t\t\tPU : Public Utilities
                                                                    \t\t\t\tAD : Advertisements
                                                                    \t\t\t\tCS : Charging Station'''+": "
                    vd=str(input(vst))
                    tcd={"DO":"Domestic","ND":"Non-Domestic","IN":"Industrial","AG":"Agriculture","PU":"Public Utilities","AD":"Advertisements","CS":"Charging Station"}
                    while vd.upper() not in tcd.keys():
                        vspacing()
                        print("Invalid Data Entered, Please try again.".center(195,"!"))
                        vspacing()
                        hspacing()
                        vd=str(input(vst))
                    vd=tcd[vd]
                elif tdl[i]=="Date_of_connection":
                    vst="Enter Value for , "+tdl[i].capitalize()+' (YYYY-MM-DD) : '
                    vd=str(input(vst))
                    while len(vd)<10 or vd.isalpha():
                        vspacing()
                        print("Invalid Data Entered, Please try again.".center(195,"!"))
                        vspacing()
                        hspacing()
                        vd=str(input(vst))
                elif tdl[i]=="Meter_No":
                    vd=str(input(vs))
                    for a in range(0,len(tabledata1)):
                        while vd==tabledata1[a][1]:
                            vspacing()
                            print("Duplicate Meter_No Entered, Please try again.".center(195,"!"))
                            vspacing()
                            hspacing()
                            vd=str(input(vs))
                else:
                    vd=str(input(vs))                                                                                           #vd: valuedata
                while len(vd)<1 or vd.isspace():
                    vspacing()
                    print("No Data Entered / Invalid Data Entered, Please Enter Valid Data.".center(195,"!"))
                    vspacing()
                    hspacing()
                    vd=str(input(vs))
                if vd.isalnum() or vd.isalpha() or "-" in vd or "@" in vd or "." in vd or "," in vd or " " in vd:
                    if "date" in tdtl[i] and "-" in vd:
                        vdc="'{}'".format(vd)
                        vl.append(vdc)
                        i+=1
                    elif vd not in ("NULL","null") and "date" not in tdtl[i]:
                        vdc="'{}'".format(vd)                                                                                       #vdc: valuedataconversion into format of entering data into Mysql
                        vl.append(vdc)                                                                                              #vl: valuelist
                        i+=1
                    elif vd in ("NULL","null"):
                        vl.append(vd)
                        i+=1
                    else:
                        vspacing()
                        print("Invalid Data Entered, Please try again.".center(195,"!"))
                        continue
                else:
                    vspacing()
                    print("Invalid Data Entered, Please try again.".center(195,"!"))
                    continue
            else:
                vspacing()
                hspacing()
                vs="Enter Value for , "+tdl[i]+" : "                                                              #vs: valuestring
                if tdl[i]=="Customer_No":
                    vd=input(vs)
                    for a in range(0,len(tabledata1)):
                        while int(vd)==tabledata1[a][0]:
                            vspacing()
                            print("Duplicate Customer_No Entered, Please try again.".center(195,"!"))
                            vspacing()
                            hspacing()
                            vd=input(vs)
                else:
                    vd=input(vs)
                while len(vd)<1 or vd.isspace():
                    print("No Data Entered / Invalid Data Entered, Please Enter Valid Data.".center(195,"!"))
                    vd=str(input(vs))
                if vd.isnumeric() or vd.isdecimal():
                    vdc=float(vd)
                    vdc=str(vd)
                    vl.append(vdc)
                    i+=1
                else:
                    vspacing()
                    print("Invalid Data Entered, Please try again.".center(195,"!"))
                    continue
        string=vl[0]
        for i in range(1,len(vl)):        
            string+=', '+vl[i]
        query="insert into {} values({})".format(tablename,string)
        cur.execute(query)
        con.commit()
        vspacing()
        print("Record Saved.".center(195,'='))
        vspacing()
        hspacing()
        cnr=str(input("Do you want to Enter another record? ('Y'es/'N'o) : "))                                              #cnr:- choice for new record
        while cnr not in ('N','n') and cnr not in ('Y','y'):
            vspacing()
            invalin()
            vspacing()
            hspacing()
            cnr=str(input("Do you want to Enter another record? ('Y'es/'N'o) : "))
        if cnr in ('N','n'):
            finaldec()
            if userdec in ('y','Y'):
                vspacing()
                print(("record entering database terminated".title()).center(195,'='))                                                            #"str".title() function used
                con.close()
                logout()
                break
            if userdec in ('n','N'):
                break
        if cnr in ('Y','y'):
            vspacing()
            print("You can enter value for the record again.".center(195,'-'))
        

def login():
    global stage1
    vspacing()
    hspacing()
    stage1=str(input("""'E'mployee Login 
                        \t\t\t\t\t\t\t\t 'C'onsumer Login : """))
    while stage1 not in ('e','E','c','C','ADMIN'):
        vspacing()
        invalin()
        vspacing()
        hspacing()
        stage1=str(input("""'E'mployee Login 
                            \t\t\t\t\t\t\t\t 'C'onsumer Login : """))

def shutdown():
    global stage1,userdec
    vspacing()
    hspacing()
    stage1=str(input("""'E'mployee Login 
                        \t\t\t\t\t\t\t\t 'C'onsumer Login
                        \t\t\t\t\t\t\t\t To 'Q'uit        : """))
    while stage1 not in ('e','E','C','c','q','Q','ADMIN'):
        vspacing()
        invalin()
        vspacing()
        hspacing()
        stage1=str(input("""'E'mployee Login 
                            \t\t\t\t\t\t\t\t 'C'onsumer Login
                            \t\t\t\t\t\t\t\t To 'Q'uit        : """))
    

def taskemp():
    global stage2
    vspacing()
    hspacing()
    stage2=str(input("""Enter 'N'ew Record
                        \t\t\t\t\t\t\t\t'B'ill Generation
                        \t\t\t\t\t\t\t\t'F'ind Consumer
                        \t\t\t\t\t\t\t\t To 'D'elete/ To 'M'odify Record : """))
    
def recordsearcher():
    global con,cur,databasename,columnlist,columntypelist,tabledatatype,choicetable,userdec,primarycolumn,fv,stage2
    databasecreator()
    tablecreator()
    cur.execute("desc {}".format(tablename))
    data=cur.fetchall()
    for i in range(0,len(data)):
        if data[i][3]=='PRI' or data[i][3]=='MUL':
            primarycolumn=data[i][0]
    fvs="To Find {}:-".format(primarycolumn)                                                #fvs:- findingvaluestring
    choice2=0
    userdec=0
    while True:
        if choice2 in ('T','t') and userdec in ('y','Y'):
            break
        vspacing()
        hspacing()
        fv=(input(fvs))                                                                      #fv:- findingvalue
        while len(fv)<1 or fv.isspace() or fv.isalpha():
            vspacing()
            print("No Data Entered / Invalid Data Entered, Please Enter Valid Data.".center(195,"!"))
            vspacing()
            hspacing()
            fv=(input(fvs))
        if fv.isnumeric() and len(fv)>=1:
            fv=int(fv)
        query="select * from {} where {}={}".format(tablename,primarycolumn,fv)
        cur.execute(query)
        data1=cur.fetchall()
        while data1==[]:
            if userdec in ('Y','y'):
                break
            elif userdec==0:
                cstr="""No Record Found, Please try 'A'gain,
                        \t\t\t\t\t\t\t\t or 'T'erminate Database :- """
                vspacing()
                hspacing()
                choice2=str(input(cstr))
                while choice2 not in ('A','a','T','t'):
                    vspacing()
                    invalin()
                    vspacing()
                    hspacing()
                    choice2=str(input(cstr))
                if choice2 in ('T','t'):
                    finaldec()
                    if userdec in ('y','Y'):
                        vspacing()
                        if stage2 in ("F","f"):
                            print(("Consumer Finding Database terminated".title()).center(195,'='))                                                            #"str".title() function used
                            con.close()
                            logout()
                        elif stage1=="ADMIN":
                            print("Customer Information Database Terminated".center(195,"="))
                            admlogout()
                        break
                    elif userdec in ('n','N'):
                        continue
                elif choice2 in ('A','a'):
                    vspacing()
                    hspacing()
                    fv=(input(fvs))                                                                      #fv:- findingvalue
                    while len(fv)<1 or fv.isspace() or fv.isalpha():
                        vspacing()
                        print("No Data Entered / Invalid Data Entered, Please Enter Valid Data.".center(195,"!"))
                        vspacing()
                        hspacing()
                        fv=(input(fvs))
                    if fv.isnumeric() and len(fv)>=1:
                        fv=int(fv)
                    query="select * from {} where {}={}".format(tablename,primarycolumn,fv)
                    cur.execute(query)
                    data1=cur.fetchall()
        if choice2 not in ('t','T'):
            vspacing()
            print("Details of Consumer Number : {} are as follows".format(fv).center(195,'-'))
            vspacing()
            for i in range(1,len(data)):
                print("\t"*10,data[i][0].center(20,' '),":- ",str(data1[0][i]).center(20,' '))
            vspacing()
            hspacing()
            choice=str(input("Do you want to fetch bills of the consumer?('Y','N') :- "))
            while choice not in ('Y','y','N','n'):
                vspacing()
                hspacing()
                invalin()
                vspacing()
                hspacing()
                choice=str(input("Do you want to fetch bills of the consumer?('Y','N') :- "))
            if choice in ('Y','y'):
                tablecreator()
                cur.execute("desc {}".format(choicetable))
                data2=cur.fetchall()
                query1="select * from {} where {}={}".format(choicetable,primarycolumn,fv)
                cur.execute(query1)
                data3=cur.fetchall()
                if data3!=[]:
                    vspacing()
                    print("Past Bills of Consumer Number : {} are as follows".format(fv).center(195,'-'))
                    vspacing()
                    print("\t"*10,"Month".center(20," "),"Billamount".center(22," "))
                    vspacing()
                    for i in range(0,len(data3)):
                        print("\t"*10,data3[i][1].center(19,' ')," : ",str(data3[i][2]).center(19,' '))
                else:
                    vspacing()
                    print("No bills found.".center(195,'-'))
                vspacing()
                hspacing()
                choice1=str(input("Do you want to Search another record? ('Y','N'):- "))
            elif choice in ('N','n'):
                vspacing()
                hspacing()
                choice1=str(input("Do you want to Search another record? ('Y','N'):- "))
            while choice1 not in ('Y','y','N','n'):
                vspacing()
                hspacing()
                invalin()
                vspacing()
                hspacing()
                choice1=str(input("Do you want to Search another record? ('Y','N'):- "))
            if choice1 in ('N','n'):
                finaldec()
                if userdec in ('y','Y'):
                    vspacing()
                    if stage2 in ("F","f"):
                        print(("Consumer Finding Database terminated".title()).center(195,'='))                                                            #"str".title() function used
                        con.close()
                        logout()
                    elif stage1=="ADMIN":
                        print("Customer Information Database Terminated".center(195,"="))
                        admlogout()
                    break
                if userdec in ('n','N'):
                    break
            if choice1 in ('Y','y'):
                vspacing()
                print("You can search another record.".center(195,'-'))
        
def billgeneration():
    global con,cur,databasename,tablename,columnlist,columntypelist,tabledatatype,choicetable,userdec,primarycolumn
    databasecreator()
    tablecreator()
    cur.execute("desc {}".format(tablename))
    data=cur.fetchall()
    for i in range(0,len(data)):
        if data[i][3]=='PRI' or data[i][3]=='MUL':
            primarycolumn=data[i][0]
    fvs="To Find {}:- ".format(primarycolumn)                                                #fvs:- findingvaluestring
    choice2=0
    userdec=0
    while True:
        if choice2 in ('T','t') and userdec in ('y','Y'):
            break
        vspacing()
        hspacing()
        fv=(input(fvs))                                                                      #fv:- findingvalue
        while len(fv)<1 or fv.isspace() or fv.isalpha():
            vspacing()
            print("No Data Entered / Invalid Data Entered, Please Enter Valid Data.".center(195,"!"))
            vspacing()
            hspacing()
            fv=(input(fvs))
        if fv.isnumeric() and len(fv)>=1:
            fv=int(fv)
        query="select * from {} where {}={}".format(tablename,primarycolumn,fv)
        cur.execute(query)
        data1=cur.fetchall()
        while data1==[]:
            if userdec in ('Y','y'):
                break
            if userdec in ('n','N'):
                vspacing()
                hspacing()
                fv=(input(fvs))                                                                      #fv:- findingvalue
                while len(fv)<1 or fv.isspace() or fv.isalpha():
                    vspacing()
                    print("No Data Entered / Invalid Data Entered, Please Enter Valid Data.".center(195,"!"))
                    vspacing()
                    hspacing()
                    fv=(input(fvs))
                if fv.isnumeric() and len(fv)>=1:
                    fv=int(fv)
                query="select * from {} where {}={}".format(tablename,primarycolumn,fv)
                cur.execute(query)
                data1=cur.fetchall()
            elif userdec==0:
                cstr="""No Record Found, Please try 'A'gain,
                        \t\t\t\t\t\t\t  or 'T'erminate Database :- """
                vspacing()
                hspacing()
                choice2=str(input(cstr))
                while choice2 not in ('A','a','T','t'):
                    vspacing()
                    invalin()
                    vspacing()
                    hspacing()
                    choice2=str(input(cstr))
                if choice2 in ('T','t'):
                    finaldec()
                    if userdec in ('y','Y'):
                        vspacing()
                        print(("Bill Generation Database terminated".title()).center(195,'='))                                                            
                        con.close()
                        logout()
                        break
                    elif userdec in ('n','N'):
                        continue
                elif choice2 in ('A','a'):
                    vspacing()
                    hspacing()
                    fv=(input(fvs))                                                                      #fv:- findingvalue
                    while len(fv)<1 or fv.isspace() or fv.isalpha():
                        vspacing()
                        print("No Data Entered / Invalid Data Entered, Please Enter Valid Data.".center(195,"!"))
                        vspacing()
                        hspacing()
                        fv=(input(fvs))
                    if fv.isnumeric() and len(fv)>=1:
                        fv=int(fv)
                    query="select * from {} where {}={}".format(tablename,primarycolumn,fv)
                    cur.execute(query)
                    data1=cur.fetchall()
        if choice2 not in ('t','T'):
            vspacing()
            for i in range(0,len(data)):
                print("\t"*10,data[i][0].center(20,' '),":",str(data1[0][i]).center(20,' '))
        vspacing()
        hspacing()
        dec=str(input("Do you want to generate bill of above consumer? ('Y','N') :- "))
        while dec not in ('Y','y','N','n'):
            vspacing()
            invalin()
            vspacing()
            hspacing()
            dec=str(input("Do you want to generate bill of above consumer? ('Y','N') :- "))
        if dec in ('y','Y'):
            tablecreator()
            vspacing()
            hspacing()
            year=(input("Bill of Year :- "))
            while len(year)<4 or year.isspace():
                print("Invalid Data Entered, Please Enter Data in YYYY format.".center(195,"!"))
                year=(input("Bill of Year :- "))
            if len(year)==4 and year.isnumeric():
                year=int(year)
            vspacing()
            hspacing()
            month=eval(input("Bill of Month(s) (Month's Number) :- "))
            while len(month)<1:
                print("Invalid Data Entered, Please Enter a Month's Number.".center(195,"!"))
                month=eval(input("Bill of Month(s) :- "))
            monthdic={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
            alpmonth=''
            for i in month:
                while i not in (1,2,3,4,5,6,7,8,9,10,11,12):
                    vspacing()
                    print("Invalid Month entered, Please try again.".center(195,'!'))
                    vspacing()
                    hspacing()
                    month=str(input("Bill of Month :- "))
                if i in (1,2,3,4,5,6,7,8,9,10,11,12):
                    alpmonth+=monthdic[i]+"-"
            alpmonth=alpmonth[0:len(alpmonth)-1]
            vspacing()
            hspacing()
            prr=(input("Meter's Present Reading :- "))                                                               #prr:- PresentReading
            while len(prr)<1 or prr.isspace():
                vspacing()
                print("Invalid Data Entered / Invalid Data Entered, Please Enter Numeric Data.".center(195,"!"))
                vspacing()
                hspacing()
                prr=(input("Meter's Present Reading :- "))
            if len(prr)>=1 and prr.isnumeric():
                prr=int(prr)
            hspacing()
            par=(input("Meter's Previous Reading :- "))                                                              #par:- PastReading
            while len(par)<1 or par.isspace():
                vspacing()
                print("Invalid Data Entered / Invalid Data Entered, Please Enter Numeric Data.".center(195,"!"))
                vspacing()
                hspacing()
                par=(input("Meter's Past Reading :- "))
            if len(par)>=1 and par.isnumeric():
                par=int(par)
            mf=1                                                                                                        #mf:- MultiplicationFactor
            uu=prr-par
            if data1[0][12]=="Domestic":
                if data1[0][13]<="2kW":
                    fr=20
                if data1[0][13]>"2kW" and data1[0][13]<="5kW":
                    fr=50
                if data1[0][13]>"5kW" and data1[0][13]<="15kW":
                    fr=100
                if data1[0][13]>"15kW" and data1[0][13]<="25kW":
                    fr=200
                if data1[0][13]>"25kW":
                    fr=250
                if uu <= 200:
                    ec=3
                elif uu > 200 and uu <= 400:
                    ec=4.50
                elif uu > 400 and uu <= 800:
                    ec=6.50
                elif uu > 800 and uu <=1200:
                    ec=7.00
                elif uu > 1200:
                    ec=8.00
            if data1[0][12]=="Non-Domestic":
                if data1[0][13]<="3kVA":
                    fr=250
                    ec=6
                if data1[0][13]>"3kVA":
                    fr=250
                    ec=8.5
            if data1[0][12]=="Industrial":
                fr=250
                ec=7.75
            if data1[0][12]=="Agriculture":
                fr=125
                ec=1.50
            if data1[0][12]=="Public Utilities":
                fr=250
                ec=6.25
            if data1[0][12]=="Advertisement":
                fr=250
                ec=8.50
            if data1[0][12]=="Charging Station":
                ec=4.25
                fr=1    
            fr=fr*(len(month))    
            total=(uu*mf*ec)+fr+((8/100)*(fr+(uu*mf*ec)))+((3.8/100)*(fr+(uu*mf*ec)))
            monthc="'{}'".format(alpmonth+","+str(year))
            cur.execute("select * from {}".format(choicetable))
            data2=cur.fetchall()
            choice3=0
            for i in range(0,len(data2)):
                if fv==data2[i][0] and (alpmonth+","+str(year))==str(data2[i][1]):
                    vspacing()
                    print("You cannot generate bill as it already exists.".center(195,'='))
                    vspacing()
                    hspacing()
                    choice3=str(input("Do you want to generate another bill? ('Y','N') :- "))
            if choice3==0:
                query="insert into {} values({},{},{})".format(choicetable,fv,monthc,total)
                cur.execute(query)
                con.commit()
                vspacing()
                print("Bill Generated as Below".center(195,'-'))
                cur.execute("desc {}".format(choicetable))
                data4=cur.fetchall()
                cur.execute("select * from {}".format(choicetable))
                data3=cur.fetchall()
                vspacing()
                for i in range(0,len(data3)):
                    for j in range(0,len(data4)):
                        if fv==data3[i][0] and (alpmonth+","+str(year))==str(data3[i][1]):
                            print("\t"*10,data4[j][0].center(20,' '),":- ",str(data3[i][j]).center(20,' '))
                vspacing()
                hspacing()
                choice3=str(input("Do you want to generate another bill? ('Y','N') :- "))
        if dec in ('n','N'):
                vspacing()
                hspacing()
                choice3=str(input("Do you want to generate another bill? ('Y','N') :- "))
        while choice3 not in ('Y','y','N','n'):
            vspacing()
            invalin()
            vspacing()
            hspacing()
            choice3=str(input("Do you want to generate another bill? ('Y','N') :- "))
        if choice3 in ('Y','y'):
            vspacing()
            print("You can generate another bill.".center(195,'-'))
            continue
        if choice3 in ('N','n'):
            finaldec()
            if userdec in ('Y','y'):
                vspacing()
                print("Bill Generation Database Terminated.".center(195,'='))
                logout()
                break
            if userdec in ('n','N'):
                continue
                
def recordmodifier():
    global con,cur,databasename,tablename,columnlist,columntypelist,tabledatatype,choicetable,primarycolumn,fv,userdec
    databasecreator()
    tablecreator()
    cur.execute("desc {}".format(choicetable))
    tabledata=list(cur.fetchall())
    rowcount1=cur.rowcount
    cur.execute("desc {}".format(tablename))
    data=list(cur.fetchall())
    rowcount=cur.rowcount                                                                                       #no of rows from table received
    for i in range(0,len(data)):
        if data[i][3]=='PRI' or data[i][3]=='MUL':
            primarycolumn=data[i][0]
    fvs="To Find {}:-".format(primarycolumn)                                                #fvs:- findingvaluestring
    choice2=0
    userdec=0
    while True:
        if choice2 in ('T','t') and userdec in ('y','Y'):
            break
        vspacing()
        hspacing()
        fv=(input(fvs))                                                                      #fv:- findingvalue
        while len(fv)<1 or fv.isspace() or fv.isalpha():
            vspacing()
            print("No Data Entered / Invalid Data Entered, Please Enter Valid Data.".center(195,"!"))
            vspacing()
            hspacing()
            fv=(input(fvs))
        if fv.isnumeric() and len(fv)>=1:
            fv=int(fv)
        query="select * from {} where {}={}".format(tablename,primarycolumn,fv)
        cur.execute(query)
        data1=cur.fetchall()
        query1="select * from {} where {}={}".format(choicetable,primarycolumn,fv)
        cur.execute(query1)
        data2=cur.fetchall()
        while data1==[]:
            if userdec in ('Y','y'):
                break
            if userdec in ('n','N'):
                vspacing()
                hspacing()
                fv=(input(fvs))                                                                      #fv:- findingvalue
                while len(fv)<1 or fv.isspace() or fv.isalpha():
                    vspacing()
                    print("No Data Entered / Invalid Data Entered, Please Enter Valid Data.".center(195,"!"))
                    vspacing()
                    hspacing()
                    fv=(input(fvs))
                if fv.isnumeric() and len(fv)>=1:
                    fv=int(fv)
                query="select * from {} where {}={}".format(tablename,primarycolumn,fv)
                cur.execute(query)
                data1=cur.fetchall()
                query1="select * from {} where {}={}".format(choicetable,primarycolumn,fv)
                cur.execute(query1)
                data2=cur.fetchall()
            elif userdec==0:
                cstr="""No Record Found, Please try 'A'gain,
                        \t\t\t\t\t\t\t\t or 'T'erminate Database :- """
                vspacing()
                hspacing()
                choice2=str(input(cstr))
                while choice2 not in ('A','a','T','t'):
                    vspacing()
                    invalin()
                    vspacing()
                    hspacing()
                    choice2=str(input(cstr))
                if choice2 in ('T','t'):
                    finaldec()
                    if userdec in ('y','Y'):
                        vspacing()
                        print(("Consumer Modifying Database terminated".title()).center(195,'='))                                                            
                        con.close()
                        logout()
                        break
                    elif userdec in ('n','N'):
                        continue
                elif choice2 in ('A','a'):
                    vspacing()
                    hspacing()
                    fv=(input(fvs))                                                                      #fv:- findingvalue
                    while len(fv)<1 or fv.isspace() or fv.isalpha():
                        vspacing()
                        print("No Data Entered / Invalid Data Entered, Please Enter Valid Data.".center(195,"!"))
                        vspacing()
                        hspacing()
                        fv=(input(fvs))
                    if fv.isnumeric() and len(fv)>=1:
                        fv=int(fv)
                    query="select * from {} where {}={}".format(tablename,primarycolumn,fv)
                    cur.execute(query)
                    data1=cur.fetchall()
                    query1="select * from {} where {}={}".format(choicetable,primarycolumn,fv)
                    cur.execute(query1)
                    data2=cur.fetchall()
        if choice2 not in ('t','T'):
            vspacing()
            for i in range(0,len(data)):
                print("\t"*10,data[i][0].center(20,' '),":- ",str(data1[0][i]).center(20,' '))
            if data2!=[]:
                for i in range(1,3):
                    print("\t"*10,tabledata[i][0].center(20,' '),":- ",str(data2[0][i]).center(20,' '))
                for i in range(1,len(data2)):
                    for j in range(1,3):
                        print("\t"*10,tabledata[j][0].center(20,' '),":- ",str(data2[i][j]).center(20,' '))
            vspacing()
            hspacing()
            dec=str(input("Do you want to modify this record? ('Y','N') :- "))
            while dec not in ('Y','y','N','n'):
                vspacing()
                invalin()
                vspacing()
                hspacing()
                dec=str(input("Do you want to modify this record? ('Y','N') :- "))
            if dec in ('n','N'):
                vspacing()
                hspacing()
                choice=str(input("Do you want to modify another record? ('Y','N') :- "))
            if dec in ('y','Y'):
                vspacing()
                hspacing()
                uc=str(input("What is to be updated?(Column Name) :- "))                                                                     #uc:- updatevalue'scolumn  
                tdl=[]                                                                                                      #tdl:-tabledatalist
                tdtl=[]                                                                                                     #tdlt:-tabledatatypelist
                col=[]                                                                                                      #col:- columncnstraintlist
                for i in range(0,rowcount):
                    tdl.append(data[i][0].lower())
                    tdtl.append(data[i][1].lower())
                    col.append(data[i][3].lower())
                for i in range(0,rowcount1):
                    tdl.append(tabledata[i][0].lower())
                    tdtl.append(tabledata[i][1].lower())
                    col.append(tabledata[i][3].lower())
                while uc.lower() not in tdl:
                    vspacing()
                    print("Incorrect Column input, please try again.".center(195,'!'))
                    vspacing()
                    hspacing()
                    uc=str(input("What is to be updated?(Column Name) :- "))
                if uc.lower() in ('month',"billamount"):
                    vspacing()
                    hspacing()
                    ov=str(input("Present Value of '{}' :- ".format(uc)))                                                       #ov:- old value of column
                    while len(ov)<1 or ov.isspace():
                        print("No Data Entered / Invalid Data Entered, Please Enter Valid Data.".center(195,"!"))
                        ov=str(input("Present Value of '{}' :- ".format(uc)))  
                    ov="'{}'".format(ov)
                    vspacing()
                    hspacing()
                    uv=str(input("New Value of '{}' :- ".format(uc)))
                    while len(uv)<1 or uv.isspace():
                        print("No Data Entered / Invalid Data Entered, Please Enter Numeric Data.".center(195,"!"))
                        uv=str(input("New Value of '{}' :- ".format(uc)))
                    uv="'{}'".format(uv)
                    query="update {} set {}={} where {}={} and {}={}".format(choicetable,uc,uv,uc,ov,primarycolumn,fv)
                    cur.execute(query)
                    con.commit()
                elif uc.lower() in tdl:
                    vspacing()
                    hspacing()
                    uv=str(input("New Value of '{}' :- ".format(uc)))                                                                                #uv:- udpatevalue
                    while len(uv)<1 or uv.isspace():
                        print("No Data Entered / Invalid Data Entered, Please Enter Valid Data.".center(195,"!"))
                        uv=str(input("New Value of '{}' :- ".format(uc)))
                    uvc=uv.split(" ")                                                                                                           #uvc:- updatevalueconversion
                    uvc="0".join(uvc)
                    uv="'{}'".format(uv)
                    if uvc.isalnum and uv not in ("NULL","null"):
                        query="update {} set {}={} where {}={}".format(tablename,uc,uv,primarycolumn,fv)
                        cur.execute(query)
                        con.commit()
                vspacing()
                print("Changes Saved.".center(195,'='))
                vspacing()
                hspacing()
                choice=str(input("Do you want to modify another record? ('Y','N') :- "))
            while choice not in ('Y','y','N','n'):
                vspacing()
                invalin()
                vspacing()
                hspacing()
                choice=str(input("Do you want to modify another record? ('Y','N') :- "))
            if choice in ('N','n'):
                finaldec()
                if userdec in ('y','Y'):
                    vspacing()
                    print(("Consumer Modifying Database terminated".title()).center(195,'='))                                                            #"str".title() function used
                    con.close()
                    logout()
                    break
                if userdec in ('n','N'):
                    continue
            if choice in ('Y','y'):
                vspacing()
                print("You can modify another record.".center(195,'-'))
                
def recordremover():
    global con,cur,databasename,tablename,columnlist,columntypelist,tabledatatype,choicetable,primarycolumn,fv,userdec
    databasecreator()
    tablecreator()
    cur.execute("desc {}".format(tablename))
    data=cur.fetchall()
    for i in range(0,len(data)):
        if data[i][3]=='PRI' or data[i][3]=='MUL':
            primarycolumn=data[i][0]
    fvs="To Find {}:-".format(primarycolumn)                                                #fvs:- findingvaluestring
    choice2=0
    userdec=0
    while True:
        if choice2 in ('T','t') and userdec in ('y','Y'):
            break
        vspacing()
        hspacing()
        fv=(input(fvs))                                                                      #fv:- findingvalue
        while len(fv)<1 or fv.isspace() or fv.isalpha():
            vspacing()
            print("No Data Entered / Invalid Data Entered, Please Enter Valid Data.".center(195,"!"))
            vspacing()
            hspacing()
            fv=(input(fvs))
        if fv.isnumeric() and len(fv)>=1:
            fv=int(fv)
        query="select * from {} where {}={}".format(tablename,primarycolumn,fv)
        cur.execute(query)
        data1=cur.fetchall()
        while data1==[]:
            if userdec in ('Y','y'):
                break
            if userdec in ('n','N'):
                vspacing()
                hspacing()
                fv=(input(fvs))                                                                      #fv:- findingvalue
                while len(fv)<1 or fv.isspace() or fv.isalpha():
                    vspacing()
                    print("No Data Entered / Invalid Data Entered, Please Enter Valid Data.".center(195,"!"))
                    vspacing()
                    hspacing()
                    fv=(input(fvs))
                if fv.isnumeric() and len(fv)>=1:
                    fv=int(fv)
                query="select * from {} where {}={}".format(tablename,primarycolumn,fv)
                cur.execute(query)
                data1=cur.fetchall()
            elif userdec==0:
                cstr="""No Record Found, Please try 'A'gain,
                        \t\t\t\t\t\t\t\t or 'T'erminate Database :- """
                vspacing()
                hspacing()
                choice2=str(input(cstr))
                while choice2 not in ('A','a','T','t'):
                    vspacing()
                    invalin()
                    vspacing()
                    hspacing()
                    choice2=str(input(cstr))
                if choice2 in ('T','t'):
                    finaldec()
                    if userdec in ('y','Y'):
                        vspacing()
                        print(("Consumer Deleting Database terminated".title()).center(195,'='))                                                            
                        con.close()
                        logout()
                        break
                    elif userdec in ('n','N'):
                        continue
                elif choice2 in ('A','a'):
                    vspacing()
                    hspacing()
                    fv=(input(fvs))                                                                      #fv:- findingvalue
                    while len(fv)<1 or fv.isspace() or fv.isalpha():
                        vspacing()
                        print("No Data Entered / Invalid Data Entered, Please Enter Valid Data.".center(195,"!"))
                        vspacing()
                        hspacing()
                        fv=(input(fvs))
                    if fv.isnumeric() and len(fv)>=1:
                        fv=int(fv)
                    query="select * from {} where {}={}".format(tablename,primarycolumn,fv)
                    cur.execute(query)
                    data1=cur.fetchall()
        if choice2 not in ('t','T'):
            vspacing()
            for i in range(0,len(data)):
                print("\t"*10,data[i][0].center(20,' '),":- ",str(data1[0][i]).center(20,' '))
            vspacing()
            hspacing()
            dec=str(input("Do you want to delete this record? ('Y','N') :- "))
            while dec not in ('Y','y','N','n'):
                vspacing()
                invalin()
                vspacing()
                hspacing()
                dec=str(input("Do you want to delete this record? ('Y','N') :- "))
            if dec in ('n','N'):
                vspacing()
                hspacing()
                choice=str(input("Do you want to delete another record? ('Y','N') :- "))
            if dec in ('Y','y'):
                vspacing()
                hspacing()
                reason=str(input("Enter Reason for Deletion: "))
                while len(reason)<1:
                    vspacing()
                    print("No Data Entered / Invalid Data Entered, Please try again.".center(195,"!"))
                    vspacing()
                    hspacing()
                    reason=str(input("Enter Reason for Deletion: "))
                cur.execute("insert into del_cus_info(customer_no,meter_no,date_of_connection,name,address,mobile_no,email_id,aadhar_card_no,bpl,bplno,zone,district,tariff_category,sactioned_load) select * from {} where {}={}".format(tablename,primarycolumn,fv))
                con.commit()
                cur.execute("update del_cus_info set reason='{}' where {}={}".format(reason,primarycolumn,fv))
                con.commit()
                cur.execute("delete from {} where {}={}".format(choicetable,primarycolumn,fv))
                con.commit()
                query="delete from {} where {}={}".format(tablename,primarycolumn,fv)
                cur.execute(query)
                con.commit()
                vspacing()
                print("Record Deleted".center(195,'='))
                vspacing()
                hspacing()
                choice=str(input("Do you want to delete another record? ('Y','N') :- "))
            while choice not in ('Y','y','N','n'):
                vspacing()
                invalin()
                vspacing()
                hspacing()
                choice=str(input("Do you want to delete another record? ('Y','N') :- "))
            if choice in ('N','n'):
                finaldec()
                if userdec in ('y','Y'):
                    vspacing()
                    print(("Consumer Deleting Database terminated".title()).center(195,'='))                                                            #"str".title() function used
                    con.close()
                    logout()
                    break
                if userdec in ('n','N'):
                    continue
                if choice in ('Y','y'):
                    vspacing()
                    print("You can delete another record.".center(195,'-'))

def admin():
    global admchoice
    vspacing()
    hspacing()
    admchoice=str(input("""Enter 'N'ew Employee ID
                           \t\t\t\t\t\t\t\t'U'nblocking/'B'locking Employee ID
                           \t\t\t\t\t\t\t\t'C'hecking Customer Information
                           \t\t\t\t\t\t\t\tEmployee 'W'orking Hours: """))
    while admchoice.lower() not in ('n','u','b','c','w','password'):
        vspacing()
        invalin()
        vspacing()
        hspacing()
        admchoice=str(input("""Enter 'N'ew Employee ID
                           \t\t\t\t\t\t\t\t'U'nblocking/'B'locking Employee ID
                           \t\t\t\t\t\t\t\t'C'hecking Customer Information
                           \t\t\t\t\t\t\t\tEmployee 'W'orking Hours: """))

def admlogout():
    global admchoice
    vspacing()
    hspacing()
    admchoice=str(input("""Enter 'N'ew Employee ID
                           \t\t\t\t\t\t\t\t'U'nblocking/'B'locking Employee ID
                           \t\t\t\t\t\t\t\t'C'hecking Customer Information
                           \t\t\t\t\t\t\t\tEmployee 'W'orking Hours
                           \t\t\t\t\t\t\t\t To 'L'ogout      : """))
    while admchoice not in ('N','n','B','b','u','U','c','C','W','w','L','l','password'):
        vspacing()
        invalin()
        vspacing()
        hspacing()
        admchoice=str(input("""Enter 'N'ew Employee ID
                               \t\t\t\t\t\t\t\t'U'nblocking/'B'locking Employee ID
                               \t\t\t\t\t\t\t\t'C'hecking Customer Information
                               \t\t\t\t\t\t\t\tEmployee 'W'orking Hours:
                               \t\t\t\t\t\t\t\t To 'L'ogout      : """))

def logout():
    global stage2
    vspacing()
    hspacing()
    stage2=str(input("""Enter 'N'ew Record
                        \t\t\t\t\t\t\t\t'B'ill Generation
                        \t\t\t\t\t\t\t\t'F'ind Consumer
                        \t\t\t\t\t\t\t\t To 'D'elete/ To 'M'odify Record
                        \t\t\t\t\t\t\t\t To 'L'ogout      : """))
    while stage2 not in ('N','n','B','b','F','f','D','d','M','m','L','l'):
        vspacing()
        invalin()
        vspacing()
        hspacing()
        stage2=str(input("""Enter 'N'ew Record
                            \t\t\t\t\t\t\t\t'B'ill Generation
                            \t\t\t\t\t\t\t\t'F'ind Consumer
                            \t\t\t\t\t\t\t\t To 'D'elete/ To 'M'odify Record
                            \t\t\t\t\t\t\t\t To 'L'ogout      : """))

#Maincode
import mysql.connector

vspacing()
print("Electricity Department of India".center(195,'='))
stage1,stage2,i,cdec,rowcount,userdec=0,0,0,0,100,0
cdata=["BLOCKED"]
while True:
    if cdata==[] or cdata[0][3]=="BLOCKED" or stage1 in ('q','Q') or cdec in ('Y','y','N','n'):
        break
    if stage2 in ('L','l'):
        shutdown()
        while stage1 in ('Q','q'):
            finaldec()
            if userdec in ('Y','y'):
                vspacing()
                print(("Program Terminated.").center(195,'='))
                break
            elif userdec in ('N','n'):
                shutdown()
    if stage2==0:
        login()                                                                                         #stage1
    stage2=0
    if stage1 in ('E','e'):
        emplogin()
        if i==1 and rowcount==0:
            break
        if bdata[0][2]=="BLOCKED":
            break
        while stage1 in ('E','e'):
            while stage2 in ('L','l'):
                finaldec()
                if userdec in ('Y','y'):
                    from time import localtime
                    log_out=localtime()
                    log_out_v=str(log_out[0])+"-"+str(log_out[1])+"-"+str(log_out[2])+"  "+str(log_out[3])+":"+str(log_out[4])+":"+str(log_out[5])
                    tslo=(log_out[3]*60+log_out[4])*60+log_out[5]                                                                                   #tslo:- Totalsecondlogout
                    tws=tslo-tsli                                                                                                                   #tws:- totalworkseconds
                    twm=tws//60                                                                                                                      #twm:- totalworkminute
                    tws=tws-(twm*60)
                    twh=twm//60
                    twm=twm-(twh*60)
                    work_time=str(twh)+":"+str(twm)+":"+str(tws)
                    query="update emplogs set log_out='{}' where UserID='{}' and log_in='{}'".format(log_out_v,empid,log_in_v)
                    query2="update emplogs set work_time='{}' where UserID='{}' and log_in='{}'".format(work_time,empid,log_in_v)
                    cur2.execute(query)
                    cur2.execute(query2)
                    con2.commit()
                    con2.close()
                    vspacing()
                    print("Successfully Logged Out.".center(195,'='))
                    break
                elif userdec in ('N','n'):
                    logout()
            if stage2 in ('L','l'):
                break
            if stage2==0 and rowcount==1:
                taskemp()
            while stage2 not in ('N','n','B','b','F','f','D','d','M','m') and rowcount==1:
                vspacing()
                invalin()
                taskemp()
            while stage2 in ('N','n'):                                                              #stage2
                vspacing()
                print("Record Entering Database Initiated.".center(195,'='))
                databasecreator()
                tablecreator()
                recordcreator()
            while stage2 in ('B','b'):
                vspacing()
                print("Bill Generation Database Initiated.".center(195,'='))
                billgeneration()
            while stage2 in ('F','f'):
                vspacing()
                print("Consumer Finding Database Initiated.".center(195,'='))
                recordsearcher()
            while stage2 in ('D','d') or stage2 in ('M','m'):
                if stage2 in ('D','d'):
                    vspacing()
                    print("Consumer Deletion Program Initiated.".center(195,'='))
                    recordremover()
                elif stage2 in ('M','m'):
                    vspacing()
                    print("Consumer Details Modifying Program Initiated.".center(195,'='))
                    recordmodifier()
            
    na=0                                                                                                    #conpart
    while stage1 in ('C','c'):
        con2=mysql.connector.connect(host='localhost',user='root',password='root',database='employee')
        cur2=con2.cursor()
        con1()
        cur.execute("create database if not exists cuslogindetails")
        con=mysql.connector.connect(host='localhost',user='root',password='root',database='cuslogindetails')
        cur=con.cursor()
        cur.execute("create table if not exists cuslogindetails(CustomerNo bigint(20) primary key, CustomerID char(50) unique, Password char(50) not null, account_status varchar(30) default 'ACTIVE')")
        if na==0:
            vspacing()
            hspacing()
            sisu=str(input("""Sign 'U'p
                            \t\t\t\t\t\t\t\t or Sign 'I'n :- """))                                      #sisu:- SignIn SignUp
            while sisu not in ('U','u','I','i'):
                vspacing()
                print("Invalid Input, Please try again.".center(195,'!'))
                vspacing()
                hspacing()
                sisu=str(input("""Sign 'U'p
                                \t\t\t\t\t\t\t or Sign 'I'n :- """))
        if na in ("u","U"):
            sisu="U"
            na=0
        if sisu in ('I','i'):
            cuslogin()
            if na in ("u","U"):
                continue
            if cdata==[] or cdata[0][3]=="BLOCKED":
                break
            if rowcount==0 and i==1:
                break
            cur.execute("select customerno from cuslogindetails where customerid='{}'".format(cusid))
            data=cur.fetchall()
            cusno=data[0][0]
            cur2.execute("desc cus_info")
            data3=cur2.fetchall()
            cur2.execute("select customer_no from cus_info")
            data2=cur2.fetchall()
            query="select Customer_no,Meter_no,date_of_connection,Name,Address,Mobile_no,Email_id,Zone,District,Tariff_Category,Sactioned_Load from cus_info where customer_no={}".format(cusno)
            cur2.execute(query)
            data4=cur2.fetchall()
            cur2.execute("select month, billamount from bills where customer_no={}".format(cusno))
            data5=cur2.fetchall()
            vspacing()
            print("Your Details".center(195,'-'))
            vspacing()
            j=0
            for i in range(0,len(data3)):
                if data3[i][0].lower() in ("customer_no","meter_no","date_of_connection","name","address","mobile_no","email_id","zone","district","tariff_category","sactioned_load"):
                    print("\t"*10,str(data3[i][0]).center(20,' '),":",str(data4[0][j]).center(20,' '))
                    j+=1
            vspacing()
            hspacing()
            cdec=str(input("Do you want to Check your past bills? ('Y','N') :- "))
            if cdec not in ('Y','y','N','n'):
                vspacing()
                invalin()
                vspacing()
                hspacing()
                cdec=str(input("Do you want to Check your past bills? ('Y','N') :- "))
            if cdec in ('Y','y'):
                if data5==[]:
                    vspacing()
                    print("No Bills Present.".center(195,'-'))
                else:
                    vspacing()
                    print("Your Past Bills are as follows :- ".center(195,'-'))
                    vspacing()
                    print("\t"*10,"Month".center(20," "),"Billamount".center(20," "))
                    vspacing()
                    for i in range(0,len(data5)):
                        print("\t"*10,data5[i][0].center(19,' ')," : ",str(data5[i][1]).center(19,' '))
            vspacing()
            print("Thank you for using Electricity Department Application.".center(195,'='))
            con.close()
            con2.close()
            break
        if sisu in ('U','u'):
            con=mysql.connector.connect(host='localhost',user='root',password='root',database='cuslogindetails')
            cur=con.cursor()
            cur2.execute("select customer_no from cus_info")
            data2=str(cur2.fetchall())
            cur.execute("select customerno from cuslogindetails")
            data=cur.fetchall()
            cur.execute("select customerid from cuslogindetails")
            data1=cur.fetchall()
            vspacing()
            print("Kindly Enter Below Details: ".center(195,"-"))
            vspacing()
            hspacing()
            cusno=(input("Customer Number :- "))
            while len(cusno)<1 or cusno.isspace() or cusno.isalpha():
                vspacing()
                print("Invalid Data Entered, Please Enter Valid Data.".center(195,"!"))
                vspacing()
                hspacing()
                cusno=(input("Customer Number :- "))
            while str(cusno) not in str(data2):
                vspacing()
                print("Customer Number not Found, Please try again.".center(195,'-'))
                vspacing()
                hspacing()
                cusno=str(input("""Customer Number
                                \t\t\t\t\t\t\t or 'E'xit:- """))
                while cusno not in str(data2) and cusno not in ('E','e'):
                    vspacing()
                    invalin()
                    vspacing()
                    hspacing()
                    cusno=str(input("""Customer Number
                                    \t\t\t\t\t\t\t or 'E'xit:- """))
                if cusno in ('E','e'):
                    vspacing()
                    print("Sign Up Page Closed.".center(195,"="))
                    break
            if str(cusno) in str(data) and str(cusno) in str(data2):
                vspacing()
                print(("Customer Number: "+str(cusno)+", CustomerID already registered.").center(195,'-'))
                continue
            if cusno not in ('E','e'):
                vspacing()
                hspacing()
                cusid=str(input("Customer ID :- "))
                while cusid in data1:
                    vspacing()
                    print("Sorry! Customer ID is not available, Please choose another one.".center(195,'-'))
                    vspacing()
                    hspacing()
                    cusid=str(input("Customer ID :- "))
                vspacing()
                hspacing()
                cuspass=str(input("Create Password :- "))
                hspacing()
                ccuspass=str(input("Confirm Password :- "))
                while cuspass!=ccuspass:
                    vspacing()
                    print("Create Password and Confirm Password Didn't Matched, Please try Again.".center(195,"!"))
                    vspacing()
                    hspacing()
                    cuspass=str(input("Create Password :- "))
                    hspacing()
                    ccuspass=str(input("Confirm Password :- "))
                if cuspass==ccuspass:
                    query="insert into cuslogindetails values({},'{}','{}','{}')".format(int(cusno),cusid,cuspass,"ACTIVE")
                    cur.execute(query)
                    con.commit()
                    vspacing()
                    print("Account Successfully Signed Up.".center(195,"-"))
                    continue
    userdec=0
    while stage1=="ADMIN":
        if userdec in ('y','Y'):
            con.close()
            con2.close()
            break
        from getpass import getpass
        try:
            f=open("pass.txt","x")                                                                          #relative path would be added later
        except:
            f=open("pass.txt","r")
        f=open("pass.txt","r")
        pasdata=f.read()
        pasdata=pasdata.split()
        if len(pasdata)==0:
            f=open("pass.txt","w")
            f.write("Password: admin")
            f=open("pass.txt","r")
            pasdata=f.read()
            pasdata=pasdata.split()
        vspacing()
        Pass=getpass(prompt="\t\t\t\t\t\t\t\t\t\t\t Password: ", stream=None)
        if Pass==pasdata[1]:
            vspacing()
            print("Hello Admin.".center(195,"-"))
            databasecreator()
            tablecreator()
            con1()
            cur.execute("create database if not exists emplogindetails")
            con2=mysql.connector.connect(host='localhost',user='root',password='root',database='emplogindetails')
            cur2=con2.cursor()
            cur2.execute("create table if not exists emplogindetails(UserID char(20) primary key not null, Password char(36) not null, account_status varchar(20) default 'ACTIVE')")
            cur2.execute("create table if not exists emplogs(UserID char(20) not null, log_in varchar(50), log_out varchar(50), work_time varchar(30), Foreign Key emplogs(UserID) references emplogindetails(UserID))")
            admin()
            pas=0
            while True:
                if admchoice in ('L','l'):
                    break
                while admchoice.lower()=='n':
                    cur2.execute("desc emplogindetails")
                    data=list(cur2.fetchall())
                    vspacing()
                    print("Employee Login Details Database Initiated.".center(195,"="))
                    while True:
                        vdl=[]
                        for i in range(0,2):
                            vspacing()
                            hspacing()
                            vs="Enter Value for "+data[i][0]+" : "
                            vd=input(vs)
                            if data[i][0]=="UserID":
                                cur2.execute("select UserID from emplogindetails where UserID='{}'".format(vd))
                                cur2.fetchall()
                                rowcount=cur2.rowcount
                                while rowcount!=0:
                                    vspacing()
                                    print("Duplicate UserID Entered, Please try another ID.".center(195,"!"))
                                    vspacing()
                                    hspacing()
                                    vd=input(vs)
                                    cur2.execute("select UserID from emplogindetails where UserID='{}'".format(vd))
                                    cur2.fetchall()
                                    rowcount=cur2.rowcount
                            while len(vd)<1 or vd.isspace():
                                vspacing()
                                print("Invalid Data Entered, Please try again.".center(195,"!"))
                                vspacing()
                                hspacing()
                                vd=input(vs)
                            vd="'{}'".format(vd)
                            vdl.append(vd)
                        string=vdl[0]
                        for i in range(1,len(vdl)):
                            string+=","+vdl[i]
                        string+=","+"'ACTIVE'"
                        cur2.execute("insert into emplogindetails values({})".format(string))
                        con2.commit()
                        vspacing()
                        hspacing()
                        ch=input("Do you want to enter another Login Detail? ('Y'/'N') : ")
                        while ch.lower() not in ('y','n'):
                            vspacing()
                            invalin()
                            vspacing()
                            hspacing()
                            ch=int(input("Do you want to enter another Login Detail? ('Y'/'N') : "))
                        if ch.lower()=='y':
                            vspacing()
                            print("You can enter another Login Detail.".center(195,"-"))
                            continue
                        if ch.lower()=='n':
                            finaldec()
                            if userdec in ('y','Y'):
                                vspacing()
                                print(("employee login details database terminated".title()).center(195,'='))                                                            #"str".title() function used
                                admlogout()
                                break
                while admchoice.upper()=="U" or admchoice.upper()=="B":
                    vspacing()
                    print("BLOCKING/UNBLOCKING Database Initiated.".center(195,'='))
                    while True:
                        vspacing()
                        hspacing()
                        fv=input("Find: Employee ID :- ")
                        cur2.execute("select UserID,account_status from emplogindetails where UserID='{}'".format(fv))
                        data=cur2.fetchall()
                        if cur2.rowcount!=0:
                            if data[0][1]=="BLOCKED" and admchoice.upper()=="U" or data[0][1]=="ACTIVE" and admchoice.upper()=="B":
                                vspacing()
                                print("\t\t\t\t\t\t\t\t\t\t\tUserID          :  ",data[0][0])
                                print("\t\t\t\t\t\t\t\t\t\t\tAccount_Status  :  ",data[0][1])
                                vspacing()
                                hspacing()
                                if data[0][1]=="BLOCKED" and admchoice.upper()=="U":
                                    ch=input("Do you want to unblock this Employee ID? ('Y'|'N') : ")
                                elif data[0][1]=="ACTIVE" and admchoice.upper()=="B":
                                    ch=input("Do yout want to block this Employee ID? ('Y'|'N') : ")
                                while ch.upper() not in ("Y",'N'):
                                    vspacing()
                                    invalin()
                                    vspacing()
                                    hspacing()
                                    if data[0][1]=="BLOCKED" and admchoice.upper()=="U":
                                        ch=input("Do you want to unblock this Employee ID? ('Y'|'N') : ")
                                    elif data[0][1]=="ACTIVE" and admchoice.upper()=="B":
                                        ch=input("Do yout want to block this Employee ID? ('Y'|'N') : ")
                                if ch.upper()=="Y":
                                    if data[0][1]=="BLOCKED" and admchoice.upper()=="U":
                                        cur2.execute("update emplogindetails set account_status='ACTIVE' where UserID='{}'".format(fv))
                                    elif data[0][1]=="ACTIVE" and admchoice.upper()=="B":
                                        cur2.execute("update emplogindetails set account_status='BLOCKED' where UserID='{}'".format(fv))
                                    con2.commit()
                                    vspacing()
                                    if data[0][1]=="BLOCKED" and admchoice.upper()=="U":
                                        print("Employee ID Unblocked.".center(195,"-"))
                                    elif data[0][1]=="ACTIVE" and admchoice.upper()=="B":
                                        print("Employee ID Blocked.".center(195,"-"))
                                if ch.upper()=="N":
                                    vspacing()
                                    print("No changes made.".center(195,"-"))
                            elif data[0][1]=="BLOCKED" and admchoice.upper()=="B" or data[0][1]=="ACTIVE" and admchoice.upper()=="U":
                                if data[0][1]=="BLOCKED" and admchoice.upper()=="B":
                                    vspacing()
                                    print("Employee ID is already BLOCKED.".center(195,"-"))
                                elif data[0][1]=="ACTIVE" and admchoice.upper()=="U":
                                    vspacing()
                                    print("Employee ID is already ACTIVE/UNBLOCKED.".center(195,"-"))
                            vspacing()
                            hspacing()
                            chch=input("Do you want to 'B'LOCK/'U'NBLOCK another Employee ID? ('BY'|'UY'|'N') : ")
                            while chch not in ('N','n','BY','by','bY','By','Uy','uy','UY','uY'):
                                vspacing()
                                invalin()
                                vspacing()
                                hspacing()
                                chch=input("Do you want to 'B'LOCK/'U'NBLOCK another Employee ID? ('BY'|'UY'|'N') : ")
                            if chch.lower() in ('by','uy'):
                                admchoice=chch.upper()[0]
                                vspacing()
                                print("You can BLOCK/UNBLOCK another Employee ID.".center(195,"-"))
                                continue
                            elif chch in ('n','N'):
                                finaldec()
                                if userdec in ('y','Y'):
                                    vspacing()
                                    print("BLOCKING/UNBLOCKING Database Terminated".center(195,'='))
                                    admlogout()
                                    break
                        else:
                            vspacing()
                            print("No Employee ID found. Please try again.".center(195,"!"))
                while admchoice in ("C","c"):
                    vspacing()
                    print("Customer Information Database Initiated.".center(195,"="))
                    recordsearcher()        
                while admchoice.lower()=="w":
                    vspacing()
                    print("Employee Working Hours Database Initiated.".center(195,"="))
                    while True:
                        vspacing()
                        hspacing()
                        fv=input("Enter Employee ID : ")
                        cur2.execute("select * from emplogs where userid='{}'".format(fv))
                        data=cur2.fetchall()
                        row=cur2.rowcount
                        if row!=0:
                            vspacing()
                            line()
                            print("\t\t\t\tEmployee ID\t\t\t\tLog In Time\t\t\t\tLog Out Time\t\t\t\tTotal Work Time")
                            line()
                            vspacing()
                            for i in range(0,row):
                                print("\t\t\t\t"+data[i][0].center(11," ")+"\t\t\t\t"+data[i][1].center(11," ")+"\t\t\t"+data[i][2].center(12," ")+"\t\t\t"+data[i][3].center(15," "))
                                line()
                        else:
                            vspacing()
                            print(("No Login/Logout by {}".format(fv)).center(195,"-"))
                        vspacing()
                        hspacing()
                        ch=input("Do you want to check another Employee Working Hours? ('Y','N') : ")
                        while ch.lower() not in ("y","n"):
                            vspacing()
                            invalin()
                            vspacing()
                            hspacing()
                            ch=input("Do you want to check another Employee Working Hours? ('Y','N') : ")
                        if ch.lower()=="y":
                            vspacing()
                            print("You can Check another Employee Working Hours.".center(195,"-"))
                            continue
                        elif ch.lower()=="n":
                            finaldec()
                            if userdec in ('y','Y'):
                                vspacing()
                                print("Employee Working Hours Database Terminated.".center(195,"="))
                                admlogout()
                                break                
                while admchoice.lower()=='password':
                    vspacing()
                    hspacing()
                    pas=input("Do you want to change password? ('Y','N') : ")
                    while pas not in ('y','Y','n','N'):
                        vspacing()
                        invalin()
                        vspacing()
                        hspacing()
                        pas=input("Do you want to change password? ('Y','N') : ")
                    if pas in ('y','Y'):
                        vspacing()
                        ppas=getpass(prompt="\t\t\t\t\t\t\t\t\t\t\t Your Previous Password was: ")
                        npas=getpass(prompt="\t\t\t\t\t\t\t\t\t\t\t New Password: ")
                        if ppas==pasdata[1]:
                            f=open("pass.txt","w")
                            f.write("Password: {}".format(npas))
                            f.close()
                            vspacing()
                            input("Password Changed. Press Enter to Continue".center(195,"-"))
                            print("\n"*60)
                            admlogout()
                        else:
                            vspacing()
                            print("Previous Password is Invalid, Please try again.".center(195,"!"))
                    if pas in ('n',"N"):
                        print("\n"*60)
                        admlogout()
                while admchoice.upper()=="L":
                    finaldec()
                    if userdec in ('y','Y'):
                        vspacing()
                        print("Successfully Logged Out".center(195,'='))
                        stage2='l'
                        break
                    if userdec in ('n','N'):
                        admlogout()                 
        else:
            vspacing()
            print("Invalid Password, Please try again.".center(195,"!"))
        
        
