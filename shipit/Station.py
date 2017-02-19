class Station(object):
    def __init__(self, stationid, phonenumber, st_street, st_zipcode, st_city, st_state):
        self.stationid = stationid
        self.phonenumber = phonenumber
        self.st_street = st_street
        self.st_zipcode = st_zipcode
        self.st_city = st_city
        self.st_state = st_state

    def __str__(self):
        return str( "[stationid:"+str(self.stationid) +
        " phonenumber: " + str(self.phonenumber) +
        " st_street:" + str(self.st_street) +
        " st_zipcode:" + str(self.st_zipcode) +
        " st_city: " + str(self.st_city) +
        " st_state:" + str(self.st_state)+"]")
