# group 17
# database CITADEL
# python code for queries

import subprocess as sp
import pymysql
import pymysql.cursors

# redirected from query 2
def personDied():
    print("ono ;-; who died???")
    try:
        name = (input("Enter the name of the person who died: ")).split(' ')
        fname = name[0]
        lname = name[1]
        query = "UPDATE PEOPLE SET Status_Dead_or_Alive = 'Dead' WHERE Fname = '" + fname + "' AND Lname = '" + lname + "'"
        print(query)
        cur.execute(query)
        con.commit()
        print("Updated person status.")

            
        cool = int(input("Is it a cool death? 1 for yes, 0 for no "))
        if cool:
            query = "SELECT PID FROM PEOPLE WHERE Fname = '" + fname + "' AND Lname = '" + lname + "'"
            try:
                cur.execute(query)
                value = cur.fetchall()
                pid=value[0]["PID"]
           
                when = input("When did they die? ")
                weapon = input("What weapon was used to kill them? ")
                manner = input("How did they die? ")
                place = input("WHere did they die? ")
                try:
                    query = "INSERT INTO COOL_DEATHS(Person_Dead_PID, When_, Weapon_Used, Manner_of_killing, Place) VALUES(%d,'%s','%s','%s', '%s')" % (
                        pid, when, weapon,manner,place)
                    print(query)
                    cur.execute(query)
                    con.commit()
                    print("Inserted into COOL_DEATHS")
                    try:
                        resp = int(input("Were certain people responsible for this? Enter 1 for yes, 0 for no: "))
                        if (resp ==1):
                            num = int(input("How many people were responsible? "))
                            for i in range(num):
                                try:
                                    person = (input("Name (Fname Lname): ")).split(' ')
                                    query = "SELECT PID FROM PEOPLE WHERE Fname = '" + person[0] + "' AND Lname = '" + person[1] + "'"
                                    cur.execute(query)
                                    value = cur.fetchall()
                                    pid2 = value[0]["PID"]
                                    
                                    query = "INSERT INTO DIE_BY VALUES(%d, %d)" % (
                                        pid, pid2)
                                    print(query)
                                    cur.execute(query)
                                    con.commit()
                                except Exception as e:
                                    con.rollback()
                                    print("Failed to insert into DIE_BY")
                                    print(">>>>>>>>>>>>>", e)
                    except Exception as e:
                        con.rollback()
                        print("Failed to find person responsible")
                        print(">>>>>>>>>>>>>", e)
                except Exception as e:
                    con.rollback()
                    print("Failed to insert into database")
                    print(">>>>>>>>>>>>>", e)
            except Exception as e:
                con.rollback()
                print("Failed to get PID")
                print(">>>>>>>>>>>>>", e) 
    except Exception as e:
        con.rollback()
        print("Failed to update to database")
        print(">>>>>>>>>>>>>", e)
    return

# redirected from query 3
def dragonDied():
    print("ono ;-; i like dragons")
    try:
        name = input("Enter the name of the dragon who died: ")
        query = "UPDATE DRAGONS SET Status_Dead_or_Alive = 'Dead' WHERE Name = '" + name +"'"
        print(query)
        cur.execute(query)
        con.commit()
        print("Updated dragon status.")
  
        try:
            query = "DELETE FROM RIDE WHERE Dragon = '" + name + "'"
            print(query)
            cur.execute(query)
            con.commit()
            print("Deleted Dragon info from RIDE")

        except Exception as e:
            con.rollback()
            print("Failed to delete from database")
            print(">>>>>>>>>>>>>", e)
    except Exception as e:
        con.rollback()
        print("Failed to update the database")
        print(">>>>>>>>>>>>>", e)
    return

# redirected from query 5
def searchPerson():
    print("Oooh you are looking for someone?")
    fname1 = input("Enter the first few letters of the name of the person you are looking for: ")
    try:
        query = "SELECT * FROM PEOPLE WHERE Fname LIKE '"+fname1+"%'"
        cur.execute(query)
        con.commit()
        ans = cur.fetchall()
        for row in ans:
            for column in row:
                print(row[column], end='\t')
            print()
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed look for required data in the database")
        print(">>>>>>>>>>>>>", e)  

# redirected from query 6
def selectFromHouse():
    print("The prestige of a house lies with its members.")
    name = input("Enter the house name: ")
    try:
        query = "SELECT * FROM PEOPLE WHERE House_Name='"+name+"'"
        cur.execute(query)
        con.commit()
        ans = cur.fetchall()
        for row in ans:
            for column in row:
                print(row[column], end='\t')
            print()
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed look for required data in the database")
        print(">>>>>>>>>>>>>", e)  

# redirected from query 7
def selectGoodRulers():
    print("The better the ruler, the more time they rule for.")
    years = input("Enter the minimum no. of years a good ruler rules for: ")
    try:
        query = "SELECT p.Fname, p.Lname FROM PEOPLE AS p, KINGS_LANDING_RULERS AS k WHERE k.Duration_Years>='"+years+"' AND p.PID = k.PID "
        cur.execute(query)
        con.commit()
        ans = cur.fetchall()
        for row in ans:
            for column in row:
                print(row[column], end='\t')
            print()
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed look for required data in the database")
        print(">>>>>>>>>>>>>", e) 

# redirected from query 8
def civilWar():
    print("ALL MEN MUST DIE")
    name = input("Enter the kingdom where war will take place: ")
    try:
        query = "SELECT House_Name, COUNT(*) FROM People WHERE Kingdom_they_are_in='"+name+"' GROUP BY House_Name"
        cur.execute(query)
        con.commit()
        ans = cur.fetchall()
        for row in ans:
            for column in row:
                print(row[column], end='\t')
            print()
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed look for required data in the database")
        print(">>>>>>>>>>>>>", e)  

# redirected from query 9
def betterThanTargy():
    print("Targaryen's are overrated.")
    ride = int(input("Is it necessary that they ride a dragon? 1 for Yes, 0 for No "))
    if(ride):
        try:
            query = "select p.Fname, p.Lname from PEOPLE AS p, KINGS_LANDING_RULERS AS k WHERE k.PID=p.PID AND k.Duration_Years>=(SELECT AVG(Duration_Years) FROM KINGS_LANDING_RULERS WHERE House='Targaryen') AND p.PID IN (SELECT Rider_PID FROM RIDE)"
            cur.execute(query)
            con.commit()
            ans = cur.fetchall()
            for row in ans:
                for column in row:
                    print(row[column], end='\t')
                print()
            con.commit()
        except Exception as e:
            con.rollback()
            print("Failed look for required data in the database")
            print(">>>>>>>>>>>>>", e)
    else:
        try:
            query = "select p.Fname, p.Lname from PEOPLE AS p, KINGS_LANDING_RULERS AS k WHERE k.PID=p.PID AND k.Duration_Years>=(SELECT AVG(Duration_Years) FROM KINGS_LANDING_RULERS WHERE House='Targaryen')"
            cur.execute(query)
            con.commit()
            ans = cur.fetchall()
            for row in ans:
                for column in row:
                    print(row[column], end='\t')
                print()
            con.commit()
        except Exception as e:
            con.rollback()
            print("Failed look for required data in the database")
            print(">>>>>>>>>>>>>", e)

# redirected from query 10
def goodKiller():
    print("You won't ever kmow who the best killer is, because you'll never know when and how many they kill :0")
    kname = input("Enter the kingdom you are in: ")
    hname = input("Enter the house you want the killer from: ")
    cnt = input("Minimum kill count required: ")
    try:
        query = " select p1.Fname, COUNT(*) FROM PEOPLE AS p1 JOIN DIE_BY AS d1 ON (p1.PID=d1.People_Responsible_PID) WHERE (select COUNT(*) FROM PEOPLE AS p JOIN DIE_BY AS d ON (p.PID=d.People_Responsible_PID) WHERE p.PID=p1.PID)>"+cnt+" AND p1.Kingdom_they_are_in='"+kname+"' AND p1.House_Name='"+hname+"' GROUP BY PID"
        cur.execute(query)
        con.commit()
        ans = cur.fetchall()
        for row in ans:
            for column in row:
                print(row[column], end='\t')
            print()
        con.commit()
    except Exception as e:
        con.rollback()
        print("Failed look for required data in the database")
        print(">>>>>>>>>>>>>", e)  


# redirected from query 1
def addPerson():
    try:
        # Takes person details as input
        query = "SELECT MAX(PID) FROM PEOPLE"
        try:
            cur.execute(query)
            value = cur.fetchall()
            piddd=int(value[0]["MAX(PID)"])
        
            row = {}
            print("Enter person's details: ")
            name = (input("Name (Fname Lname): ")).split(' ')
            row["PID"] = piddd + 1
            row["Fname"] = name[0]
            row["Lname"] = name[1]
            row["Bdate"] = input("Birth Date (YYYY-MM-DD): ")
            row["Status"] = input("Dead/Alive: ")
            row["House"] = input("House: ")
            row["Kingdom"] = input("Kingdom of current residence: ")

            query = "INSERT INTO PEOPLE(PID, Fname, Lname, DOB, Status_Dead_or_Alive, House_Name, Kingdom_they_are_in) VALUES(%d, '%s', '%s', '%s', '%s', '%s', '%s')" % (
                row["PID"], row["Fname"], row["Lname"], row["Bdate"], row["Status"], row["House"], row["Kingdom"])

            print(query)
            cur.execute(query)
            con.commit()

            if (row["Status"] == 'Dead'):
                try:
                    cool = int(input("Is it a cool death? 1 for yes, 0 for no"))
                    if cool:
                        pid = row["PID"]
                        when = input("When did they die? ")
                        weapon = input("What weapon was used to kill them? ")
                        manner = input("How did they die? ")
                        place = input("WHere did they die? ")
                        query = "INSERT INTO COOL_DEATHS(Person_Dead_PID, When_, Weapon_Used, Manner_of_killing, Place) VALUES(%d,'%s','%s','%s', '%s')" % (
                            pid, when, weapon,manner,place)
                        print(query)
                        cur.execute(query)
                        con.commit()
                        print("Inserted into COOL_DEATHS")

                        try:
                            resp = int(input("Were certain people responsible for this? Enter 1 for yes, 0 for no: "))
                            if (resp ==1):
                                num = int(input("How many people were responsible? "))
                                for i in range(num):
                                    try:
                                        person = (input("Name (Fname Lname): ")).split(' ')
                                        query = "SELECT PID FROM PEOPLE WHERE Fname = '" + person[0] + "' AND Lname = '" + person[1] + "'"
                                        cur.execute(query)
                                        value = cur.fetchall()
                                        pid2 = value[0]["PID"]
                                        
                                        query = "INSERT INTO DIE_BY VALUES(%d, %d)" % (
                                            pid, pid2)
                                        print(query)
                                        cur.execute(query)
                                        con.commit()
                                    except Exception as e:
                                        con.rollback()
                                        print("Failed to insert into DIE_BY")
                                        print(">>>>>>>>>>>>>", e)
                        except Exception as e:
                            con.rollback()
                            print("Failed to find person responsible")
                            print(">>>>>>>>>>>>>", e)
                    
                except Exception as e:
                    con.rollback()
                    print("Failed to insert into cool_deaths")
                    print(">>>>>>>>>>>>>", e)

            print("Inserted Into Database")
        except Exception as e:
            con.rollback()
            print("Failed to get PID")
            print(">>>>>>>>>>>>>", e) 
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return

# redirected from query 4
def besthouse():    
    try:
        row = {}
        print("Enter the house you want data for, if want for all, enter \"ALL\": ")
        name = input("")
        if(name == "ALL"):
            query =  "SELECT House, AVG(Duration_Years) AS Avg_Years\
                         FROM KINGS_LANDING_RULERS\
                         GROUP BY House;"

        else:
            query = "SELECT House, AVG(Duration_Years) as Avg_Years\
                     FROM KINGS_LANDING_RULERS\
                     WHERE House = '%s';" % (name)
        
        print(query)
        cur.execute(query)
        ans = cur.fetchall()
        for row in ans:
            for column in row:
                print(row[column], end='\t')
            print()
        con.commit()

    
    except Exception as e:
        con.rollback()
        print("Failed to retrieve from database")
        print(">>>>>>>>>>>>>", e)

    return


def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        addPerson()
    elif(ch == 2):
        personDied()
    elif(ch == 3):
        dragonDied()
    elif(ch == 4):
        besthouse()
    elif(ch == 5):
        searchPerson()
    elif(ch==6):
        selectFromHouse()
    elif(ch==7):
        selectGoodRulers()
    elif(ch==8):
        civilWar()
    elif(ch==9):
        betterThanTargy()
    elif(ch==10):
        goodKiller()
    elif(ch==11):
        exit()
    else:
        print("Error: Invalid Option")


# Global
while(1):
    tmp = sp.call('clear', shell=True)

    desig = input("Designation: ")

    if (desig.lower() != "maester"):
        print("ACCESS DENIED!")
        flag = int(input("Enter 1 to continue, 2 to leave: "))
        if (flag == 1):
            continue
        else:
            exit()
    else:
        while(1):
            password = input("Password: ")
            if (password.lower() == "valar morghulis"):
                print("ACCESS ALLOWED")
                break
            else:
                print("INCORRECT PASSWORD")
                whattodo = int(input("Enter 1 to re-enter password, 2 to exit: "))
                if whattodo == 2:
                    exit()

    tmp = input("Enter any key to CONTINUE>")

    try:
        con = pymysql.connect(host='localhost',
                              port=3306,
                              user="root",
                              password="abcd1234",
                              db='CITADEL',
                              cursorclass=pymysql.cursors.DictCursor)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                
                print("1. Add person")  
                print("2. Person died")  
                print("3. Dragon died")  
                print("4. House data")  
                print("5. Search for someone")
                print("6. Data on all people from a house")
                print("7. Names of all the good rulers")
                print("8. Headcount for a civil war")
                print("9. Who rules better than a Targryen?")
                print("10. Who's the best killer here?")
                print("11. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 11:
                    exit()
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except Exception as e:
        tmp = sp.call('clear', shell=True)
        print(e)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")