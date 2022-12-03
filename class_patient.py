class Patient:
    def __init__(self, id, name, diagnosis, gender, age):
        self.id = id 
        self.name = name
        self.diagnosis = diagnosis
        self.gender = gender
        self.age = age
  
    def set_name(self,name):
        self.name = name
    def set_diagnosis(self,diagnosis):
        self.diagnosis = diagnosis
    def set_gender(self,gender):
        self.gender = gender
    def set_age(self,age):
        self.age = age

    def get_id(self,id_user):
        if self.id==id_user:
            return True
        else :
            return False

    def __str__(self):
        return f"{self.id:>10s}{self.name:>10s}{self.diagnosis:>10s}{self.gender:>10s}{self.age:>10s}"
    
    def formatPatientInfo(self):
        return f"{self.id}_{self.name}_{self.diagnosis}_{self.gender}_{self.age}\n"