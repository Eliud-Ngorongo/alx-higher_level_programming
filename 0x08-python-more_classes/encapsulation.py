class Employees():
    def __init__(self):
        self.company = "Marina Stores"
        self.__office = "Sales"
    def identify (self):
        return self.company
    def dept(self):
        return self.__office
    def set__office(self, department):
        self.__office = department
    def get__office(self):
        return self.__office

ruth = Employees()
ruth.set__office("production")
print(f"ruth works at {ruth.identify()} in the {ruth.dept()} department")

