import pymysql

class Address(object):
    def __init__(self, adrid, person, street, zipcode, city, state):
        self.adrid = adrid
        self.person = person
        self.street = street
        self.zipcode = zipcode
        self.city = city
        self.state = state

    def __str__(self):
        return str( "[id:"+str(self.adrid) +
        " size: " + str(self.person) +
        " street:" + str(self.street) +
        " zip:" + str(self.zipcode) +
        " city: " + str(self.city) +
        " state:" + str(self.state)+"]")
