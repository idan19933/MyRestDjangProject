import requests
import json
from datetime import date,datetime
import requests


url = "http://127.0.0.1:8000/home/rest/workers/"

payload={}
headers = {
  'Authorization': 'Basic YWRtaW46YWRtaW4='
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

data = json.loads(response.text)

##########################################################################
# Function :# Calculating the average salary of workers
# Input: The list dictionaries with details about employees
# Output:The average salary of teh worker
##########################################################################
def getAvergeSalary(employeeData):
  employeeCount = len(employeeData)
  combinedEmployeeSalary = 0
  # calculating average salary
  for k in employeeData:
    salary = k.get('salary')
    combinedEmployeeSalary += int(salary)
  averge_salary = int(combinedEmployeeSalary/employeeCount)
  return averge_salary

##########################################################################
# Function : Returning the hire date
# Input:The converted dictionary of the employee data
# Output:The hire date of the worker
##########################################################################
def getEmployeeHireDate(hireDateText):
  hireDateTextSplit = hireDateText.split("-")
  year = int(hireDateTextSplit[0])
  month = int(hireDateTextSplit[1])
  day = int(hireDateTextSplit[2])
  hireDate = date(year,month,day)
  return hireDate

##########################################################################
# Function :# Returning the qualified employees satisfied one year working,salary threshold
# Input: The list dictionaries with details about employees
# Output:List of dictionaries with details about qualified workers
##########################################################################
def getSeniorEmployeeData(employeesInfos):
  seniorEmployeesData = []
  avergeEmployeeSalary = getAvergeSalary(employeesInfos)
  currentDate = datetime.now().date()
  # check if the salary is below the average
  for employyeInfoByType in employeesInfos:
    workerSalary = int(employyeInfoByType.get('salary'))
    isSalaryHigerThanAverge = avergeEmployeeSalary < workerSalary
    if isSalaryHigerThanAverge:
      continue
    # check if the worker works more than 1 year
    hireDateText = employyeInfoByType.get('hire_date')
    employeedDays, isEmployeedMoreThanYear = getIsEmployeeMoreThanYear(currentDate, hireDateText)

    if not isEmployeedMoreThanYear:
      continue
    # add the qualified employees to a list
    employeeName = employyeInfoByType.get('name')
    seniorEmployeeDateByType = {
      'name': employeeName,
      'work_days': employeedDays,
      'salary': workerSalary,
    }
    # return data of the qualified workers
    seniorEmployeesData.append(seniorEmployeeDateByType)
  return seniorEmployeesData


##########################################################################
# Function :return employee total work days and if he is working more than one year
# Input: the hire date of the employee and the current date
# output:return employee total work days and if he is working more than one year
##########################################################################
def getIsEmployeeMoreThanYear(currentDate, hireDateText):
  hireDate = getEmployeeHireDate(hireDateText)
  employeedDays = (currentDate - hireDate).days
  isEmployeedMoreThanYear = employeedDays > 365
  return employeedDays, isEmployeedMoreThanYear



##########################################################################
# Function :This is the main function
# Input: The list dictionaries with details about employees
# output:A text file with name, working days and salary of the workers who qualified
##########################################################################
def mainFunc(data):
  mainData = getSeniorEmployeeData(data)
  with open('mytext.txt', 'w') as file:
    for person in mainData:
        file.write('name:')
        file.write(person['name'])
        file.write('\n')
        file.write('work days:')
        file.write(str(person['work_days']))
        file.write('\n')
        file.write('salary:')
        file.write(str(person['salary']))
        file.write('\n')
        file.write('\n')
        file.write('\n')




print(mainFunc(data))
