# Create class Fulltime Employee and inherit from Employee class
from Employee import Employee

class FullTimeEmployee(Employee):

    phrases =[]

    #listOfEmployee = []
    #employees = []

    # Fulltime employee class constructor
    def __init__(self, name="Kitchen", employees=[]):
        self.name = name
        self.employees = employees

    def addEmployee(self, employee):
        self.employees += [employee]

    def removeEmployee(self, employeesid):
        for employee in self.employees:
            if employee.getEmpId() == employeesid:
                self.employees.remove(employee)

    def numberOfEmployee(self):
        return len(self.employees)

    def displayEmp(self):
        for employee in self.employees:
            print(employee.id, employee.fname, employee.lname, employee.department, employee._salary)

    def iAmFullTimeEmployee(self):
        return 'I am full time employee class.'

    def writeFileTxt(self):
        print("hi")
        #f = open('testone.txt', "w")
        #f.write('I am here ')


    def readFileTxt(self):
        f = open('input.txt', "r")
        words = f.read()
        return words

    def createNewAccountEmployee(self, id, fname, lname, department, salary):
        FullTimeEmp = Employee(id, fname, lname, department, salary)
        return FullTimeEmp

    def FireEmp(self, employees):
        with open(employees, "r") as openFile:
            for line in openFile:
                phrases = line.split()
                i = 0
                while i < len(phrases):
                    if "NEW" in phrases[i]:
                        self.addEmployee(self.createNewAccountEmployee(str(phrases[1]),str(phrases[2])
                                                , str(phrases[3]), str(phrases[4]),   phrases[5]))

                        #print(str(phrases[i + 1]))
                    if "RAISE"  in phrases[i]:
                        print(phrases[i], phrases[1], phrases[2])
                        print(phrases[2])
                        i += 1
                    break

FullTimeEmp = FullTimeEmployee()
FullTimeEmp.addEmployee(FullTimeEmp.createNewAccountEmployee('1', "James", "AB", 1000, 55))
FullTimeEmp.addEmployee(FullTimeEmp.createNewAccountEmployee('2', "John", "BB", 2000, 55))
FullTimeEmp.addEmployee(FullTimeEmp.createNewAccountEmployee('3', "Yousef", "CB", 3000, 55))
FullTimeEmp.addEmployee(FullTimeEmp.createNewAccountEmployee('4', "Marry", "DB", 4000, 55))
#FullTimeEmp.removeEmployee('2')
FullTimeEmp.FireEmp('input.txt')
FullTimeEmp.displayEmp()



#print("\n I am ", Yousef.name)
print(FullTimeEmp.numberOfEmployee())
print(FullTimeEmp.iAmFullTimeEmployee())

FullTimeEmp.writeFileTxt()
#print(FullTimeEmp.readFileTxt())
"""
with open('input.txt', "r") as openFile:
    for line in openFile:
        phrases = line.split()
        i = 0
        while i < len(phrases):
            if "NEW" in phrases[i]:
                print(str(phrases[i + 1]))
                i += 1
            break
"""



"""

employee1 = Employee('0012', "Yousef", 7000, "IT", "IT")

employee2 = Employee('0039', "Mohammad", 10000, "DS", "DS")
#employee3 = FullTimeEmployee("Ahmad", '0048', 15000, "CS")
#employee4 = FullTimeEmployee("John", '0057', 20000, "BA")

print("\nName: " + employee1.name + "\nID Number: " + employee1.id
      + "\nCurrent salary: $%d" % employee1.salary + "\nDepartment: " + employee1.department)
print(employee1.giveRaise(700, 20))
print(employee1.numOfEmployee)

f = open("tinput.txt", "w")
f.write("\nName: " + employee1.name + "\nID Number: " + employee1.id
    + "\nCurrent salary: $%d" % employee1.salary + "\nDepartment: " + employee1.department)

f.write("\n---------------" + "\nName: " + employee2.name + "\nID Number: " + employee2.id
    + "\nCurrent salary: $%d" % employee2.salary + "\nDepartment: " + employee2.department)

f = open("input.txt", "r")
print(f.read())





#print("\nName: " + employee2.name + "\nID Number: " + employee2.idd
 #     + "\nCurrent salary: $%d" % employee2.salary + "\nDepartment: " + employee2.department)

#print("\nName: " + employee3.name + "\nID Number: " + employee3.idd
 #     + "\nCurrent salary: $%d" % employee3.salary + "\nDepartment: " + employee3.department)

#print("\nName: " + employee4.name + "\nID Number: " + employee4.idd
  #    + "\nCurrent salary: $%d" % employee4.salary + "\nDepartment: " + employee4.department)
"""