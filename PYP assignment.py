#Mitchell Tang Kai Yang
#TP060964

def option():
    try:  #check type = int
        option = int(input("\nEnter your option: "))
    except:
        option = -1
    return option

def acc():
    while True:
        print("\nEnter -1 to back to Main Menu.")
        password = input("Enter the password: ")
        if password == "-1":
            mMenu()
        elif password == "admin":
            sMenu()
        else:
            print("Incorrect password")
            continue
    
def search(user):
    while True:
        print("\nEnter -1 to back to Menu.")
        sID = str(input("Enter the patient ID: "))
        if sID == "-1":
            menu(user)

        #check input not "", space & check input is 5 char
        if sID == "" or sID.isspace() == True or len(sID) != 5:
            print("There are no such ID")
            continue

       #check 1st char of input is alphabet & others are digits
        if sID[0].isalpha() == False or sID[1:4].isdigit() == False:
            print("There are no such ID")
            continue
        else:
            sID = sID.capitalize()
            break
    try:
        fhand = open("patients.txt", "r")
    except:
        print("No patient registered / Data file not found.")
        menu(user)

    content1 = []
    content2 = []
    exist = 0
    lineNo = 0
    lines=fhand.readlines()
    for line in lines:
        stripLine = line.rstrip()
        data1 = stripLine.split(", ")
        content1.append(data1)
        if not sID in content1[lineNo][0]:
            lineNo = lineNo + 1
            continue
        else:
            exist = 1
    fhand.close()
    
    try:
        fhand = open("vaccination.txt", "r")
    except:
        print("No patient registered / Data file not found.")
        menu(user)
    lines=fhand.readlines()
    for line in lines:
        stripLine = line.rstrip()
        data2 = stripLine.split(", ")
        content2.append(data2)
    fhand.close()
    
    if exist == 1:#check patient's existence
        print("Patient found.")
    else:
        print("Patient not found.")

    return content1, content2, lineNo, exist

def update(file, content): 
    if file == 1:
        fhand = open("patients.txt", "w")
        for line in content:
            fhand.write(", ".join(line) + "\n")
    else:
        fhand = open("vaccination.txt", "w")
        for line in content:
            fhand.write(", ".join(line) + "\n")
    fhand.close()
    return

def sMenu():
    user = "s"
    while True:
        print("\nCovid-19 Vaccination Record Management System")
        print("\nStaff Menu")
        print("~"*25)
        print("\n1) New Patient Registration")
        print("2) Vaccine Administration")
        print("3) Search Patient Record & Vaccination Status")
        print("4) Statistical Information on Patients Vaccinated")
        print("5) Modify Patient's Details")
        print()
        print("6) Logout")
        op = option()
        if 1 <= op <= 6:
            if op == 1:
                registration(user)
            elif op == 2:
                administration()
            elif op == 3:
                pRecord(user)
            elif op == 4:
                info(user)
            elif op == 5:
                modify()
            else:
                mMenu()
        else:
            print("The value entered is not available in option.")
            print()
            continue

def mMenu():
    user = "p"
    while True:
        print("\nCovid-19 Vaccination Record Management System")
        print("\nMain Menu")
        print("~"*25)
        print("\n1) New Patient Registration")
        print("2) Search Patient Record & Vaccination Status")
        print("3) Statistical Information on Patients Vaccinated")
        print()
        print("4) Login As Staff")
        print("5) Exit")
        op = option()
        if 1 <= op <= 5:
            if op == 1:
                registration(user)
            elif op == 2:
                pRecord(user)
            elif op == 3:
                info(user)
            elif op == 4:
                acc()
            else:
                print("Thank you for using our system.")
                exit()
        else:
            print("The value entered is not available in option.")
            print()
            continue
        
def menu(user):
        if user == "s":
            sMenu()
        else:
            mMenu()

def vaccine(age, user):
    age = int(age)
    while True:
        #vaccines list
        print("\nVaccines that currently available.")
        print("~"*25)
        print()
        print("   Vaccine Code - Dosage Required - Interval Between Doses - Age group")
        print("1)      AF      -        2        -  2 weeks(or 14 days)   -    >=12  ")
        print("2)      BV      -        2        -  3 weeks(or 21 days)   -    >=18  ")
        print("3)      CZ      -        2        -  3 weeks(or 21 days)   -    12-45 ")
        print("4)      DM      -        2        -  4 weeks(or 28 days)   -    >=12  ")
        print("5)      EC      -        1        -           N/A          -    >=18  ")
        print()
        print("6) Menu")
        print("Patient's age: ",age)


        if age > 45:
            print("\nPatient are eligible for all vaccine EXCEPT CZ.")
            op = option()
            if 1 <= op <= 6:
                if op == 1:
                    vCode = "AF"
                elif op == 2:
                    vCode = "BV"
                elif op == 4:
                    vCode = "DM"
                elif op == 5:
                    vCode = "EC"
                elif op == 6:
                    menu(user)
                else:
                    print("Patient are not eligible for this vaccine")
                    continue
            else:
                print("The input is not available in option.")
                print()
                continue
            
        elif age >= 18:
            print("\nPatient are eligible for all vaccine.")
            op = option()
            if 1 <= op <= 6:
                if op == 1:
                    vCode = "AF"
                elif op == 2:
                    vCode = "BV"
                elif op == 3:
                    vCode = "CZ"
                elif op == 4:
                    vCode = "DM"
                elif op == 5:
                    vCode = "EC"
                else:
                    menu(user)
            else:
                print("The input is not available in option.")
                print()
                continue

        else:
            print("\nPatient are eligible for all vaccine EXCEPT BV & EC.")
            op = option()
            if 1 <= op <= 6:
                if op == 1:
                    vCode = "AF"
                elif op == 3:
                    vCode = "CZ"
                elif op == 4:
                    vCode = "DM"
                elif op == 6:
                    menu(user)
                else:
                    print("Patient are not eligible for this vaccine")
                    continue
            else:
                print("The input is not available in option.")
                print()
                continue
        break
    return vCode
            
def registration(user):
            
    def alphabet(j = "0"):
        alphabetList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        ab = alphabetList[int(j)]
        return ab
    
    print("\nRegistering new patient...")
    while True:
        #VC list
        print("\nAvailable Vaccination Centre")
        print("~"*25)
        print("\n1) Vaccination Centre 1")
        print("2) Vaccination Centre 2")
        print()
        print("3) Menu")

        op = option()
        if 1 <= op <= 3:
            if op == 1:
                vc = "VC1"
                break
            elif op == 2:
                vc = "VC2"
                break
            else:
                menu(user)
        else:
            print("The input is not available in option.")
            print()
            continue
        
    while True:
        print("\nEnter -1 to back to Menu.")
        name = input("Enter the name : ")
        if name == "-1":
            menu(user)
        elif name == "" or name.isspace()== True:
            print("Please enter the name.")
            continue
        else:
            break
    while True:
        try:   #check type = int
            print("\nEnter -1 to back to Menu.")
            age = int(input("Enter the age: "))
        except:
            print("Invaild Input")
            print()
            continue
        if age == -1:
            menu(user)
        elif age < 12:
            print("Patient are not eligible for vaccination")
            print()
            menu(user)
        else:
            break
    
    while True:
        try:   #check type = int
            print("\nEnter -1 to back to Menu.")
            cNum = int(input("Enter the contact number: "))
        except:
            print("Invaild Input")
            print()
            continue
        if cNum == -1:
            menu(user)
        elif len(str(cNum)) > 15:
            print("In our world there are no contact number that are more then 15 digit.")
            continue
        else:
            break
    
    vCode = vaccine(age, user)

    try:
        fhand = open("patients.txt", "r")
    except:
        fhand = open("patients.txt", "w")
        fhand.close()
        fhand = open("patients.txt", "r")
    ID = len(fhand.readlines()) # get the latest number of patient
    fhand.close()

    j = 0
    while True:
        if ID > 9999:
            ID = ID - 9999
            j = j + 1
            continue
        else:
            break
    ab = alphabet(j)
    
    ID = str(ID).zfill(4)
    ID = ab + ID
    status = "NEW"
    IBD = "None"
    fhand = open("patients.txt", "a")
    fhand.write("%s, %s, %s, %s, %s, %s\n" % (ID, name, age, cNum, vc, vCode))
    fhand.close()
    fhand = open("vaccination.txt", "a")
    fhand.write("%s, %s, %s, %s, %s, %s\n" %(ID, name, vc, vCode, status, IBD))
    fhand.close()
    print("\nRegistration completed.")
    print("***Patient's ID is", ID)
    print()
    return

def administration():
    print("\nAdministrating...")
    
    def showData():
        print()
        print("Patient ID: ", content2[lineNo][0])
        print("Patient name: ", content2[lineNo][1])
        print("Vaccination Centre: ", content2[lineNo][2])
        print("Vaccine chosen: ", content2[lineNo][3])
        print("Patient current status: ", content2[lineNo][4])
        print("Interval between doses: ", content2[lineNo][5])
        print()
        return
    
    content1, content2, lineNo, exist = search("s")
    if exist == 0:
        administration()
    elif content2[lineNo][4] == "COMPLETED":
        showData()
        print("Patient has completed vaccination.")
        administration()
    else:
        while True:
            showData()
            print()
            print("Patient completed Dose ?")
            print("~"*25)
            print("1) Dose 1")
            print("2) Dose 2")
            print()
            print("3) Display patient vaccination status")
            print("4) Vaccine Administration")
            print("5) Staff Menu")

            op = option()
            if 1 <= op <= 5:
                if op == 1:
                    if content2[lineNo][4] == "NEW":
                        if content2[lineNo][3] == "EC":
                            content2[lineNo][4] = "COMPLETED"
                            print()
                            print("Patient has completed vaccination")
                        else:
                            if content2[lineNo][3] == "AF":
                                content2[lineNo][5] = "2 weeks(or 14 days)"
                            elif content2[lineNo][3] == "DM":
                                content2[lineNo][5] = "4 weeks(or 28 days)"
                            else:
                                content2[lineNo][5] = "3 weeks(or 21 days)"
                            content2[lineNo][4] = "COMPLETED-D1"
                            print()
                            print("Patient has completed Dose 1")
                        update(2, content2)
                        showData()
                    else:
                        print()
                        print("Patient has taken Dose 1 before.")
                        continue

                    
                elif op == 2:
                    if content2[lineNo][4] == "COMPLETED-D1":
                        content2[lineNo][4] = "COMPLETED"
                        content2[lineNo][5] = "None"
                        update(2, content2)
                        print()
                        print("Patient has completed vaccination")
                        showData()
                    else:
                        print()
                        print("Patient have not taken Dose 1 before.")
                        continue
                    
                elif op == 3:
                    continue
                elif op == 4:
                    administration()
                else:
                    sMenu()
            else:
                print("The input is not available in option.")
                print()
                continue
            administration()
            
def pRecord(user):
    print("\nSearching patient's detail...")
    content1, content2, lineNo, exist = search(user)
    
    if exist == 1:
        print("\nPatient ID: ", content1[lineNo][0])
        if user == "s":
            print("Patient's name: ", content1[lineNo][1])
            print("Patient's age: ", content1[lineNo][2])
            print("Patient's contact number: ", content1[lineNo][3])
        print("Vaccination Centre: ", content1[lineNo][4])
        print("Vaccine chosen: ", content1[lineNo][5])
        if content1[lineNo][5] == "EC":
            DR = 1
        else:
            DR = 2
        print("Dosage Required: ", DR)
        print("Patient current status: ", content2[lineNo][4])
        print("Interval between doses: ", content2[lineNo][5])
    pRecord(user)

def info(user):
    vc1 = 0
    vc1w = 0
    vc1c = 0
    vc2 = 0
    vc2w = 0
    vc2c = 0
    try:
        fhand = open("vaccination.txt", "r")
    except:
        print("No patient registered / Data file not found.")
        menu(user)
    lines = fhand.readlines()
    for line in lines:
        if "COMPLETED" in line:
            if "VC1" in line:
                vc1 = vc1 + 1
                if "COMPLETED-D1" in line:
                    vc1w = vc1w + 1 
            else:
                vc2 = vc2 + 1
                if "COMPLETED-D1" in line:
                    vc2w = vc2w + 1
        else:
            continue
    fhand.close()
    vc1c = vc1 - vc1w
    vc2c = vc2 - vc2w
    print("\nVaccination Centre 1")
    print("~"*25)
    print("Patients vaccinated: ", vc1)
    print("Patients waiting for dose 2: ", vc1w)
    print("Patients completed vaccination: ", vc1c)

    print("\nVaccination Centre 2")
    print("~"*25)
    print("Patients vaccinated: ", vc2)
    print("Patients waiting for dose 2: ", vc2w)
    print("Patients completed vaccination: ", vc2c)

    print("\nTotal of Vaccination Centre 1 & 2")
    print("~"*25)
    print("\nTotal patients vaccinated: ", vc1 + vc2)
    print("Total patients waiting for dose 2: ", vc1w + vc2w)
    print("Total patients completed vaccination: ", vc1c + vc2c)

def modify():
    print("\nModifying patient's detail...")
    content1, content2, lineNo, exist = search("s")
    while True:
        print("\nPatient ID: ", content1[lineNo][0])
        print("Patient current status: ", content2[lineNo][4])
        print("1) Patient name: ", content1[lineNo][1])
        print("2) Patient's age: ", content1[lineNo][2])
        print("3) Patient's contact number: ", content1[lineNo][3])
        print("4) Vaccination Centre: ", content1[lineNo][4])
        print("5) Vaccine chosen: ", content1[lineNo][5])
        print()
        print("6) Back")
        print("7) Staff Menu")
        op = option()
        if 1 <= op <= 7:
            if op == 1:
                while True:
                    print("\nEnter -1 to return.")
                    name = input("Enter new name : ")
                    if name == "-1":
                        break
                    elif name == "" or name.isspace()== True:
                        print("Please enter new name.")
                        continue
                    else:
                        content1[lineNo][1] = name
                        content2[lineNo][1] = name
                        break
            elif op == 2:
                while True:
                    try:   #check type = int
                        print("\nEnter -1 to return.")
                        age = int(input("Enter new age: "))
                    except:
                        print("Invaild Input")
                        print()
                        continue
                    if age == -1:
                        break
                    elif age < 12:
                        print("Below 12 years old are not eligible for vaccination")
                        print()
                        continue
                    else:
                        if age >= int(content1[lineNo][2]):
                            content1[lineNo][2] = str(age)
                            break
                        else:
                            print("Patient's age should not be decreasing")
                            continue
            elif op == 3:
                while True:
                    try:   #check type = int
                        print("\nEnter -1 to return.")
                        cNum = int(input("Enter new contact number: "))
                    except:
                        print("Invaild Input")
                        print()
                        continue
                    if cNum == -1:
                        break
                    elif len(str(cNum)) > 15:
                        print("In our world there are no contact number that are more then 15 digit.")
                        continue
                    else:
                        content1[lineNo][3] = str(cNum)
                        break
            elif op == 4:
                while True:
                    #VC list
                    print("\nAvailable Vaccination Centre")
                    print("~"*25)
                    print("\n1) Vaccination Centre 1")
                    print("2) Vaccination Centre 2")
                    print()
                    print("3) Return")

                    op = option()
                    if 1 <= op <= 3:
                        if op == 1:
                            vc = "VC1"
                        elif op == 2:
                            vc = "VC2"
                        else:
                            break
                        content1[lineNo][4] = vc
                        content2[lineNo][2] = vc
                        break
                    else:
                        print("The input is not available in option.")
                        print()
                        continue
            elif op == 5:
                if content2[lineNo][4] == "NEW":
                    vCode = vaccine(content1[lineNo][2], "s")
                    content1[lineNo][5] = vCode
                    content2[lineNo][3] = vCode
                else:
                    print("Patient can only change vaccine chosen before taking any dose.")
            elif op == 6:
                modify()
            else:
                sMenu()
            update(1, content1)
            update(2, content2)
            continue
        else:
            print("The input is not available in option.")
            print()
            continue               
        
mMenu()
