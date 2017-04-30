import unittest

import Address

import Package
import Station
import Vehicle

class Test_Objects(unittest.TestCase):
    def test_address_values(self):
        adrid = '213',
        person = 'chester vantester',
        street = '5555 test street',
        zipcode = "55555",
        city = "testville",
        state = 'mn'


        a = Address.Address(
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
    def test_Package_values(self):
        id = '213',
        size_id = '1',
        src_id = '2',
        dst_id = "1",



        p = Package.Package(
            id=id,
            size_id=size_id,
            src_id=src_id,
            dst_id=dst_id,
        )



        self.assertEqual(p.id,id)
        self.assertEqual(p.size_id, size_id)
        self.assertEqual(p.src_id, src_id)
        self.assertEqual(p.dst_id, dst_id)


if __name__ == '__main__':
    unittest.main()