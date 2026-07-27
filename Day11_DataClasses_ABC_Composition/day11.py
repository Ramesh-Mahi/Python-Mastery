#advaced oops + dataclasses + enums + abc (abstract class)

#session 1 - dataclasses

class Employee:
    def __init__(self, id, name, salary): 
        self.id = id 
        self.name = name 
        self.salary = salary

emp1 = Employee(102, 'Rahul', 2222)
print(emp1)

from dataclasses import dataclass

@dataclass
class Employee:
    id:int
    name:str
    salary:int

emp = Employee(101, 'Mahi', 2200)
#dataclass eliminates the boilerplate code and it takes care of __repr__ and __eq__ automatically

print(emp)

#practice1 

from dataclasses import dataclass

@dataclass
class Book:
    title:str
    author:str
    price:int

book1 = Book('Wings of Fire', 'Dr. APJ', 2000)
print(book1)

#session 2 - Frozen Dataclass

from dataclasses import dataclass

@dataclass(frozen= True)
class Config:
    host:str
    port:int

config = Config('localhost', 8080)
#config.host = 'abc' # this will throw the error as fronzen is true and we can't change the values in frozen dataclass
print(config)
#configurations, constants, API settings 

#practice 
from dataclasses import dataclass

@dataclass(frozen=True)
class Tool:
    endpoint:str
    api_key:str
    timeout:int

servicenow = Tool('https://api.servicenow.com','snow_334343434',20)

print(servicenow)

#session 3 - Enum
#Enum gives you a named set of values which are typo proof and self documenting
from enum import Enum

class Status(Enum):
    OPEN = 'Open'
    CLOSED = 'Closed'
    IN_PROGRESS = 'In Progress'

print(Status.OPEN)
print(Status.OPEN.value)

from enum import Enum

class Severity(Enum):
    LOW = 'Low'
    MEDIUM = 'Medium'
    HIGH = 'High'
    CRITICAL = 'Critical'

print(Severity.CRITICAL.value)
print(Severity.LOW.value)

#session 4 - ABC - Abstract Base Classes

from abc import ABC, abstractmethod

class DataSourceConnector(ABC):
    @abstractmethod
    def fetch_incidents(self) -> list[dict]:
        pass
    
    @abstractmethod
    def fetch_meta_data(self) -> dict:
        pass

    def describe(self) -> str:
        #concrete function shared by all subclasses not abtract
        return f'Connector: {self.__class__.__name__}'

# class BrokenConnector(DataSourceConnector):
#     def fetch_incidents(self) -> list[dict]:
#         return super().fetch_incidents()
#     #here we not implemented the fetch metadata and which caused the failure at the instantiate/compile time and not run time

# c = BrokenConnector() 

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        return 'Startin the Vehicle'
    
    @abstractmethod
    def stop(self):
        return 'Stoping the Vehicle'

class Car(Vehicle):
    def start(self):
        return super().start()
    def stop(self):
        pass

class Bike(Vehicle):
    def start(self):
        pass
    def stop(self):
        pass

car = Car()
bike = Bike()
print(car.start())

#session 5 - Multiple Inheritance 

class Camera:
    def capture(self):
        print('Captured')

class Phone:
    def call(self):
        print('Calling')

class SmartPhone(Camera, Phone):
    pass

s = SmartPhone()

s.capture()

s.call()

#practice 

class Scanner:
    def scanning(self):
        print('scanning')

class Printer:
    def printing(self):
        print('printing')

class MultiFunctionPrinter(Scanner, Printer):
    pass

printer1 = MultiFunctionPrinter()
printer1.scanning()
printer1.printing()


#session 6 - method resolution order (mro)

class A:
    def show(self):
        print('A')

class B(A):
    def show(self):
        print('B')

class C(A):
    def show(self):
        print('C')

class D(B,C):
    pass

d = D()

d.show()
print(D.mro())


class Animal:
    def characters(self):
        print('Animal')

class Dog(Animal):
    def characters(self):
        print('Dog barks')

class Robot(Animal):
    def characters(self):
        print('Robot walks')

class RobotDog(Dog, Robot):
    pass 

chitti = RobotDog()
chitti.characters()
print(RobotDog.mro())

#session 7 - composition (preferred over inheritance)

class Engine:

    def start(self):
        print('Started')
    
class Car:

    def __init__(self):
        self.engine = Engine() #composition - Car has an Engine 
    
    def drive(self):
        self.engine.start()
        print('Driving')

#practice

@dataclass
class CPU:
    cores: int
    clock_speed: float

    def compute(self):
        return f'The CPU is running with cores - {self.cores} with clock speed - {self.clock_speed}'
    
@dataclass
class RAM:
    size: int

    def load(self):
        return f'The CPU is loaded with RAM - {self.size}'

@dataclass
class Disk:
    capacity:int
    kind: str = 'SSD'

    def load(self):
        return f'The Disk has capacity of {self.capacity} with {self.kind}'

@dataclass
class Computer:
    cpu: CPU
    ram: RAM 
    disk: Disk

    def boot(self):
        return '\n'.join([self.cpu.compute(), self.ram.load(), self.disk.load()])


my_pc = Computer(
    cpu=CPU(cores=8, clock_speed=3.5),
    ram=RAM(size=32),
    disk=Disk(capacity=256, kind='Nvme ssd'))

print(my_pc.boot())

#mini project 
#employee management system 

from dataclasses import dataclass, field
from enum import Enum, auto
from abc import ABC, abstractmethod

class EmployeeStatus(Enum):
    ACTIVE = auto()
    INACTIVE = auto()
    ON_LEAVE = auto()

@dataclass
class Employee:
    emp_id: str
    name: str
    salary: int
    department: str
    status: EmployeeStatus = EmployeeStatus.ACTIVE

class EmployeeOperations(ABC):

    @abstractmethod
    def add(self, employee:Employee) -> None:
        pass

    @abstractmethod
    def remove(self, employee:Employee) -> None:
        pass

    @abstractmethod
    def search(self, employee:Employee) -> None:
        pass

    @abstractmethod
    def display(self) -> None:
        pass

class EmployeeService(EmployeeOperations):
    def __init__(self):
        self._employees: dict[str, Employee] = {}
    
    def add(self, employee:Employee):
        if employee.emp_id in self._employees:
            raise ValueError(f'The Employee - {employee.emp_id} already exists')
        self._employees[employee.emp_id] = employee

    def remove(self, employee:Employee):
        if employee.emp_id not in self._employees:
            raise KeyError(f'The Employee - {employee.name} does not exists')
        del self._employees[employee.emp_id]
    
    def search(self, employee:Employee):
        return self._employees.get(employee.emp_id)
    
    def display(self):
        if not self._employees:
            print('No employees')
            return None 
        for emp in self._employees.values():
            print(f'{emp.emp_id} | {emp.name} | {emp.salary} | {emp.department} | {emp.status.name}\n')
    
    def update_salary(self, employee:Employee, new_salary:int):
        emp = self.search(employee.emp_id)
        if emp is None:
            raise KeyError(f'The emp - {emp} is not found')
        if new_salary < 0:
            raise ValueError(f'The new salary cannot be negative - {new_salary}')
        emp.salary = new_salary
    
    def update_status(self, employee:Employee, new_status):
        emp = self.search(employee.emp_id)
        if emp is None:
            raise KeyError(f'The employee not found')
        emp.status = new_status
    

svc = EmployeeService()
svc.add(Employee('E001', 'Asha', 55000, 'Engineering'))
svc.add(Employee('E002', 'Ravi', 93000, 'Data', status= EmployeeStatus.ON_LEAVE))
svc.display()

'''
Interview Questions
1. dataclasses - would eliminate the need of __init__ and automatically takes care of the __repr__ and __eq__
2. dataclass - no need to have the __init__, __repr__, __eq__ and normal class would need these 
3. fronzen = True -> this will freeze the values inside the dataclass that we provide initially and it won't be changed in the runtime
4. Enum -> eliminates the common typos like peding instead of pending in status fields. gives a fixed, named set of members, comparison by identity. this will eliminate the multiple values of the status and would keep a unique values for the status field
5. ABC -> this will enable us to create abstract class and that will act as a blue print template that need to followed for those class which inherits it
6. abstraction is the process of hiding the complexity functions and shows only the required things to the use and we don't have a separate interface in python like c# or java
7. if a subclass doesn't implement an abstract method then it will through an error bez we supposed to implement all the methods of the abstract class in the derived class 
8. Composition vs inheritance -> composition is better bez we are using the separate classes inside the single class by passing the class as a argument; it has the features but unlike inheritance it inherits all the properties to the derived class but when the requirements/complexity increases we may need to increase the classes and use multiple inheritance which may lead to confusion
9. MRO - method resolution order and python will resolve it from buttom to up in a tree structure. it follows C3 linearisation 
10. diamond inheritance - it is a problem that may occur during the multi level inheritance. when two classes derived from the same base class and another class inherits from both of the derived classes
'''        

#mentor challenge 

from dataclasses import dataclass, field
from enum import Enum, auto
from abc import abstractmethod

class Severity(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    CRITICAL = auto()

class IncidentStatus(Enum):
    ACTIVE = auto()
    RESOLVED = auto()
    PENDING = auto()

@dataclass
class Incident:
    number:int
    severity:Severity = Severity.LOW
    incidentstatus:IncidentStatus = IncidentStatus.ACTIVE
    description:str

@dataclass
class Metric:
    name:int
    value:int
    unit:str

@dataclass
class RCAReport:
    incident_id: str
    severity:Severity
    root_cause: str
    confidence: float
    recommended_action: str

    def display(self):
        print('*' * 50)
        print('RCA Report')
        print('*'* 50)
        print(f'Incident ID          : {self.incident_id}')
        print(f'Severity             : {self.severity}')
        print(f'Root Cause           : {self.root_cause}')
        print(f'Confidence           : {self.confidence:.0%}')
        print(f'Recommended Action   : {self.recommended_action}')
        print(f'*'*50)



class AIAgent(ABC):

    @abstractmethod
    def connect(self):
        print(f'Connecting to tool')
    
    @abstractmethod
    def fetch(self, incident_id: str):
        print(f'Fetching the logs')
    
    @abstractmethod
    def analyse(self, data: list):
        print('Analysing the incident')
    
    # def describe(self):
    #     return f'[{self.__class__.__name__}] ready'

class LogScaleAgent(AIAgent):

    def connect(self):
        print('Connected to Logscale')
        return True
    
    def fetch(self, incident_id:str):
        print(f'Fetching logs for {incident_id}')

        return [
            'ERROR' OutOfMemoryError in payment-service,
            'WARN' GC pause,
            'ERROR' Connection pool exhausted
        ]
       
    def analyse(self,data):
        error_count = sum(1 for line in data if line.startswith('ERROR'))
        return {'source': 'logs', 'error_count': error_count, 'raw': data}

class DynatraceAgent(AIAgent):
    
    def connect(self):
        print('Connected to Dynatrace')
        return True
    
    def fetch(self, incident_id):
        print(f'Fetching the metrics for {incident_id}')
        return [
            Metric(name='heap_usage_pct', value=98, unit='%'),
            Metric(name='db_connection_pool_used', value=100.0, unit='%'),
            Metric(name='p99_latency', value=4200,unit='ms')
        ]

    def analyse(self, data):
        breached = [m for m in data if m.value > 90]
        return {'source': 'metrics', 'breached_thresholds':breached, 'raw':data}


class ServiceNowAgent(AIAgent):
    
    def connect(self):
        print('Connected to ServiceNow tool')
        return True
    
    def fetch(self, incident_id):
        print(f'Fetching incident details for {incident_id}')
        return[
            Incident(
                incident_id = incident_id
                title = 'Payment service degraded',
                severity=Severity.CRITICAL,
                status = IncidentStatus.ACTIVE
            )
        ]

    def analyse(self, data):
        incident = data[0]
        return {'source':'incident' , 'incident':incident, 'raw':data}
    
class LLMClient:
    def summarize_root_cause(self, findings):

        log_errors = findings.get('logs', {}).get('error_count',0)

        breached = findings.get('metrics',{}).get('breached_thresholds', [])

        if log_errors and breached:
            root_cause = (
                'Memory pressure in payment-service caused connection pool'
            )
            confidence =0.9
            action=(
                'Increase heap size/ pod memory limit for payment-service'
            )
        else:
            root_cause = "Insufficient signal to confirm root cause."
            confidence = 0.35
            action = "Gather additional logs and metrics before remediation."
 
        return root_cause, confidence, action


class RCAEngine(AIAgent):

    def __init__(self, agents, llm_client):
        self._agents = agents
        self._llm = llm_client

    def run(self, incident_id):
        findings:dict = {}
        incident_severity = Severity.MEDIUM

        for agent in self._agents:
            agent.connet()
            raw_data = agent.fetch(incident_id)
            result = agent.analyse(raw_data)
            findings[result['source']] = result

            if result['source'] == 'incident':
                incident_severity = result['incident'].severity
            
        root_cause, confidence, action = self._llm.summarize_root_cause(findings)

        return RCAReport(
            incident_id=incident_id,
            severity=incident_severity,
            root_cause=root_cause,
            confidence=confidence,
            recommended_action=action
        )

if __name__ == '__main__':
    engine = RCAEngine(
        agents=[
            ServiceNowAgent(), 
            LogScaleAgent(),
            DynatraceAgent()
        ],
        llm_client=LLMClient()
    )

    report = engine.run(incident_id='INC0023445')
    print()
    report.diplay()