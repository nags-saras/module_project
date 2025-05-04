

def first_N_prime(  N):
    """Return the first n prime numbers."""
    x=2
    count_prime=0
    prime=[]
    while count_prime<N:
        for i in range(2,x):
            if x%i==0:
                break
        else:
            prime.append(x)
            count_prime+=1
        x+=1
    return prime



class employees:
    def __init__(self,name, employee_id, position, salary, department):
        self.name=name
        self.employee_id=employee_id
        self.position=position
        self.salary=salary
        self.department=department
    
    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.employee_id}")
        print(f"Position: {self.position}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")
    
