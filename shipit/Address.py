import pymysql
import pytest

class Address(object):
    def __init__(self, adrid, person, street, zipcode, city, state):
        self.adrid = adrid
        self.person = person
        self.street = street
        self.zipcode = zipcode
        self.city = city
        self.state = state


        # if any(x.isalpha() for x in person) and any(x.isspace() for x in person):
        #     raise Exception("people's names cannot contain numbers/missing a space!")
        # if any(x.isalpha() for x in city) and any(x.isspace() for x in city):
        #     raise Exception("cities cannot contain numbers/missing a space!")
        # if len(state) < 2:
        #     raise Exception("database only accepts state abbreviations")

    def __str__(self):
        return str( "[id:"+str(self.adrid) + "," +
        "person:" + str(self.person) + "," +
        "street:" + str(self.street) + "," +
        "zip:" + str(self.zipcode) + "," +
        "city:" + str(self.city) + "," +
        "state:" + str(self.state)+"]")

    def __repr__(self):
        return str(str(self.adrid) + "," +
                   str(self.person) + "," +
                   str(self.street) + "," +
                   str(self.zipcode) + "," +
                   str(self.city) + "," +
                   str(self.state))