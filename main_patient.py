import class_patient

def main():
    menu_number=int(input("Patient Menu\n0-Return to main Menu\n1-Display patient's List\n2-Search for patient by ID\n3-Add patient\n4-Edit patient info\nEnter option: "))
    while menu_number != "":
        if menu_number == 0:
            #Return to main menu
            pass
        elif menu_number == 1:
            displayPatientList()
        elif menu_number == 2:
            searchPatientByld()
        elif menu_number == 3:
            addPatientToList(patient_list)
            writePatientsListToFile(patient_list)
        elif menu_number ==4:
            editPatientInfo9()
            displayPatientList()
        
        menu_number=int(input("\n Patient Menu\n0-Return to main Menu\n1-Display patient's List\n2-Search for patient by ID\n3-Add patient\n4-Edit patient info\nEnter option: "))


def enterPatientInfo():
    id = str(input("Enter ID plz: "))
    name = str(input("Enter name plz: "))
    diagnosis = str(input("Enter Diagnsis plz: "))
    gender = str(input("Enter Gender plz: "))
    age = str(input("Enter age plz: "))
    info=class_patient.Patient(id,name,diagnosis,gender,age)
    return info

def readPatientsFile():
    patient_list=[]
    P_file= open(r"patients.txt")
    for P_line in P_file:
        P_items = P_line.rstrip().split("_")
        patient= class_patient.Patient(P_items[0], P_items[1], P_items[2], P_items[3], P_items[4])
        patient_list.append(patient)
    P_file.close()
    return patient_list

def searchPatientByld():

    id_user = str(input("enter ID plz: "))
    for X in patient_list:
        if X.get_id(id_user) == True:
            patient_info=X
            break
        else :
            patient_info= " "
        
    if patient_info != " " :
        print (patient_info)
        return patient_info
    else:
        print (f"patient with ID {id_user} not in the patient file")

        
def editPatientInfo9():
    object_patient=searchPatientByld()
    for P in patient_list:
        if P.id == object_patient.id:
            P.name = str(input("Enter name plz: "))
            P.diagnosis = str(input("Enter Diagnsis plz: "))
            P.gender=str(input("Enter Gender plz: "))
            P.age=input("Enter age plz: ")
   
def displayPatientList():
    for p in patient_list:
        print (p)
   

def writePatientsListToFile(patient_list):
    P_file=open(r"patients.txt","w")
    for x in patient_list:
        P_line= class_patient.Patient.formatPatientInfo(x)
        P_file.write(P_line)
    P_file.close()

def addPatientToList(patient_list):
    P_info = enterPatientInfo()
    patient_list.append(P_info)
    

if __name__=="__main__":
    patient_list = readPatientsFile()    
    main()

