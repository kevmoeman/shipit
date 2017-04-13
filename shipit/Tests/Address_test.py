import unittest

from shipit.Address import Address


class Test_Address(unittest.TestCase):
    def test_address_values(self):
        adrid = '213',
        person = 'chester vantester',
        street = '5555 test street',
        zipcode = "55555",
        city = "testville",
        state = 'mn'


        a = Address(
            adrid=adrid,
            person=person,
            street=street,
            zipcode=zipcode,
            city=city,
            state=state
        )



        self.assertEqual(a.adrid,adrid)
        self.assertEqual(a.person, person)
        self.assertEqual(a.street, street)
        self.assertEqual(a.zipcode, zipcode)
        self.assertEqual(a.city, city)
        self.assertEqual(a.state, state)
    #test the exceptions and update


if __name__ == '__main__':
    unittest.main()