class Employee:
    
    #constructor initializing
    def __init__(self):
        print('Employee Created')

    #Deleting(Calling constructor)
    def __del__(self):
        print('Destructor called, Employee Deleted')

emp = Employee()
del emp