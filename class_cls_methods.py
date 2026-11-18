class student:
    school = "Model college"
    @classmethod #this identify the method a class method
    #cls - refers to class itself
    def change_school(cls, new_school):
        cls.school = new_school
        #new_school - receives the new name
        #cls.school - access the class attributes
student.change_school("valley college")

print(student.school)