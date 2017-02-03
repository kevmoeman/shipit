class Vehicle(object):
    def __init__(self, id, company):
        self.id = id
        self.company = company

    def __str__(self):
        return str( "P[id:"+str(self.id) + " companyt: " + str(self.company)+"]")
