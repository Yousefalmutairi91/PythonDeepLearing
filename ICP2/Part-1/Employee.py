# Create class Employee
class Employee(object):

    # count the number of Employees
    numOfEmployee = 0
    balanceOfEmp = 0
    salaryBalance = 0
    payRate = 10

    payRoll = []

    # Employee class constructor
    def __init__(self, id, fname, lname, department, salary, isEmployee=True):
        self.id = id
        self.fname = fname
        self.lname = lname
        #self.balance = balance
        self.department = department
        self._salary = salary
        self.isEmployee = isEmployee
        Employee.numOfEmployee = Employee.numOfEmployee + 1

    def giveRaise(self, id, raiseAmount):
        print("\n gine raise fun ", id, raiseAmount)
        with open('input.txt', "r") as openFile:
            for line in openFile:
                phrases = line.split()
                i = 0
                while i < len(phrases):
                    if "NEW" in phrases[i]:
                        print("NEwd", phrases[1])
                        if id == phrases[5]:
                            print("I am ", phrases[2])

                        i += 1
                    else:
                        break

        newRaise = int(phrases[5]) * int(raiseAmount) / 100
        print(newRaise)
        newSalary = int(raiseAmount) + int(phrases[5])
        #raiseAmount =+ self.salary
        print(int(raiseAmount))
        print("I am the salary before raise: ", self._salary)
        self.setSalary = newSalary
        print("I am the salary after raise: ", self._salary)
        return int(newSalary)

    @property
    def setSalary(self):
        return self._salary

    @setSalary.setter
    def setSalary(self, newSalary):
        self._salary = newSalary

    #print(giveRaise(0, 1000, 20))

    def Pay (self, paymentAmount, currBalance):
        newbalance = paymentAmount + currBalance
        self.balanceOfEmp = newbalance
        return newbalance

    def Fire (self, id):
        for employee in self.payRoll:
            if self.getEmpId() == id:
                self.payRoll.remove(employee)
        self.isEmployee = False
        return

    def isEmployed(self):
        isEmp = False
        return isEmp

    def getBalance(self):
        newSalary = self.salary + self.balanceOfEmp
        return newSalary

    def getSalary(self):
        return self.salary

    def setBalance(self):
        newBalanceSalary = self.salary + self.balanceOfEmp
        return newBalanceSalary

    def payRollFun(self):

        for i in range(1, 10):
            self.payRoll.append(i)
            #print(i)

    # Get All Variables
    def getAll(self):
        allElements = [self.name, self.id, self.salary, self.department]
        return allElements

    # Insert Data into list
    def insertDataList(self, listInit, datas):
        for data in datas:
            listInit.append(data)
        return listInit

    # Get Employee ID
    def getEmpId(self):
        return self.id

    def setPayRateToZero(self):
        setToZero = self.payRate = 0
        return setToZero

    def printEmpInfo(self):
        return "\n-------------" + "\nName: " + self.name + "\nID Number: " + self.id + "\nCurrent salary: $%d" % self.salary + "\nDepartment: " + self.department

#emp = Employee('1',"Yousef", "IT", 1000)
#emp.giveRaise(5)

"""

emp1 = Employee('1',"Yousef", 1000, "IT")
emp2 = Employee('2',"Ahmed", 100, "CS")
print(emp1.salary)
print(emp1.getSalary())
emp1.setBalance()
result = emp1.giveRaise(10)
payfun = emp1.Pay(result, emp1.balanceOfEmp)
reofbal = emp1.getBalance()
print("\nCuurent Balalnce: ", reofbal)

list = []

list.append(emp1)
list.append(emp2)

print(list)
for name in list:
    print(name.name, name.id, name.salary)

for i in list:
    if i == emp1:
        list.remove(i)

for name in list:
    print(name.name, name.id, name.salary)




#emp1.payRollFun()
#print(emp1.payRoll)
#for item in emp1.getAll():
 #   emp1.payRoll.append(item)

#print(emp1.payRoll)

emp1.insertDataList(emp1.payRoll, emp1.getAll())
emp2.insertDataList(emp2.payRoll, emp2.getAll())


print(emp1.payRate)

print(emp1.setPayRateToZero())

print(emp1.printEmpInfo())

arr = []

f = open("input.txt", "w")
f.write(emp1.printEmpInfo())
f.write(emp2.printEmpInfo())

f.close()
#f.write(empget.printEmpInfo())


#print(empget)

print("\nIam at the bottom:", emp1.payRoll)
print(emp1.Fire(1))
print(emp1.payRoll)
"""