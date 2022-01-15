
# Create class Fulltime Employee and inherit from Employee class
from Employee import Employee



class PartTimeEmployee(Employee):

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

    def iAmPartTimeEmployee(self):
        return 'I am part time employee class.'

    def createNewAccountEmployee(self, id, fname, lname, department, salary):
        PartTimeEmp = Employee(id, fname, lname, department, salary)
        return PartTimeEmp
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
                        #print(self.giveRaise(int(phrases[1]), int(phrases[2])))


                        #self.giveRaise(phrases[2])
                        #print(self.giveRaise(str(phrases[2])))

                        #self.giveRaise(phrases[1], phrases[2])

                        i += 1
                    break





PartTimeEmp = PartTimeEmployee()
PartTimeEmp.addEmployee(PartTimeEmp.createNewAccountEmployee('1', "James", "James", "AB", 1000))
PartTimeEmp.addEmployee(PartTimeEmp.createNewAccountEmployee('2', "John", "James","BB", 2000))
PartTimeEmp.addEmployee(PartTimeEmp.createNewAccountEmployee('3', "Yousef", "James","CB", 3000))
PartTimeEmp.addEmployee(PartTimeEmp.createNewAccountEmployee('4', "Marry", "James","DB", 4000))
#PartTimeEmp.removeEmployee('2')
PartTimeEmp.FireEmp('input.txt')

PartTimeEmp.displayEmp()




#print("\n I am ", Yousef.name)
print(PartTimeEmp.numberOfEmployee())
print(PartTimeEmp.iAmPartTimeEmployee())

