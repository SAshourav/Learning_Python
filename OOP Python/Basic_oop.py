class Customer:
    def __init__(self, name,membership_type):
        self.name = name
        self.membership_type = membership_type

    @property
    def name(self):
        print("Getting name")
        return self._name

    @name.setter
    def name(self,name):
        print("Setting the name")
        self._name = name

    def update_membership(self, new_membership):
        #What we can do?
        #invoke an API
        #update database
        #charge the customer
        #pretty much anything
        self.membership_type = new_membership

    def read_customer():
        print("reading the customer")

    def __str__(self):
        print("Coverting to String")
        return self.name+" "+self.membership_type

    def print_all_customers(customers): #not defining the self
        for customer in customers:
            print(customer)

    def __eq__(self, other):
        if self.name == other.name and self.membership_type == other.membership_type:
            return True
        return False

    __repr__ = __str__

c1 = Customer("Hasib", "Gold")
print(c1.name, c1.membership_type)

c2 = Customer("Sabbir", "Silver")
print(c2.name, c2.membership_type)

customers = [c1,c2] #list of customer
print(customers[0].name)

c1.update_membership("Bronze")
print(customers[0].membership_type)

Customer.read_customer() #as we don't used self so, we need to directly address the class not the object

print(customers[0]) # this would have give us an error if we didn't used the __str__ method

Customer.print_all_customers(customers)

print(customers[0] == customers[1])

#if we don't use the __eq__ method then it will compare based on id of the object and
#every object has different object id

print(customers) #solved using __repr__