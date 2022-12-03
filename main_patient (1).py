import class_patient

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
    P_file= open(r"C:\Users\qiaom\Desktop\project\patients.txt")
    for P_line in P_file:
        P_items = P_line.rstrip().split("_")
        patient = class_patient.Patient(P_items[0], P_items[1], P_items[2], P_items[3], P_items[4])
        patient_list.append(patient)
    P_file.close()
    return patient_list

def searchPatientByld():
    List = readPatientsFile()
    id_user = str(input("enter ID plz: "))
    for X in List:
        if X.get_id(id_user) == True:
            print(X)
            return X
             
def editPatientInfo():
    
    list = []
    
    f=open(r"C:\Users\qiaom\Desktop\project\patients.txt","a")
    object_patient = searchPatientByld()
    name = str(input("Enter name plz: "))
    diagnosis = str(input("Enter Diagnsis plz: "))
    gender = str(input("Enter Gender plz: "))
    age = int(input("Enter age plz: "))
    object_patient.set_name(name)
    object_patient.set_diagnosis(diagnosis)
    object_patient.set_gender(gender)
    object_patient.set_age(age)
    list = object_patient 
    f.write("\n" + list)
    f.close()
    return list
    
def displayPatientList():
    patient_list = readPatientsFile()
    for p in patient_list:
        print (p)
   
def writePatientsListToFile(patient_list):
    P_file=open(r"C:\Users\qiaom\Desktop\project\patients.txt","a")
    for x in patient_list:
        P_line= class_patient.Patient.formatPatientInfo(x)
        P_file.write(P_line)
    P_file.close()

def addPatientToList(patient_list):
    P_info = enterPatientInfo()
    patient_list.append(P_info)
    return patient_list
    
def main():
    
    patient_list = []
    
    menu_number=float(input("Patient Menu\n0-Return to main Menu\n1-Display patient's List\n2-Search for patient by ID\n3-Add patient\n4-Edit patient info\nEnter option: "))
    while menu_number != "":
        if menu_number == 0:
            #Return to main menu
            pass
        elif menu_number == 1:
            displayPatientList()
        elif menu_number == 2:
            searchPatientByld()
        elif menu_number == 3:
            addPatientToList(list)
            writePatientsListToFile(list)
        elif menu_number == 4:
            editPatientInfo()
            writePatientsListToFile(list)
        
        menu_number=float(input("\n Patient Menu\n0-Return to main Menu\n1-Display patient's List\n2-Search for patient by ID\n3-Add patient\n4-Edit patient info\nEnter option: "))
        
if __name__ == "__main__":    

    main()