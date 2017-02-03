
import json
import Package

import tornado
import tornado.web
import Address





#pieces i need get handler returning JSON list
#need helper function to create JSON list package - > JSON converter
#create personhandler retrieves a JSON list that grabs all the addresses
#return all the packages in the system when start


class CorsHandler(tornado.web.RequestHandler):

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def options(self):
        self.set_status(204)
        self.finish()

class PackageHandler(CorsHandler):
    def initialize(self, package_dao, address_dao):
        self.package_dao = package_dao
        self.address_dao = address_dao

    def post(self):
        print(self.request.body)
        self.write(tornado.escape.json_encode('{}'))

    def get(self):
        """
            [
                {
                    "id": '1x23',
                    "size": "small",
                    "src": {
                      "addr_id": 1,
                      "addr_person": "Rob Base",
                      "addr_street": "123 Code St",
                      "addr_city":"Minneapolis",
                      "addr_state":"MN",
                      "addr_zip": "55414"
                    },
                    "dst": {
                      "addr_id": 2,
                      "addr_person": "Van Stacker",
                      "addr_street": "42 Engi Ln",
                      "addr_city":"Seattle",
                      "addr_state":"WA",
                      "addr_zip": "98109"
                    }
                },
            ]
        """
        packages = self.package_dao.query_packages()
        addresses = self.address_dao.query_addresses()

        # create an index of addresses
        address_lookup = { a.adrid : a for a in addresses }

        package_jsons = []
        for p in packages:
            # first convert package attributes to json
            pj = package_to_json(p)
            # then convert the nested addresses to json
            srcj = address_to_json(address_lookup[pj['src']])
            pj['src'] = srcj

            dstj = address_to_json(address_lookup[pj['dst']])
            pj['dst'] = dstj
            package_jsons.append(pj)

        self.write(tornado.escape.json_encode(package_jsons))




def package_to_json(p):
    pj = {'id':p.id,
        'size':p.size_id,
        'src':p.src_id,
        'dst':p.dst_id}

    return pj

def address_to_json(addr):
    aj = {
      "addr_id": addr.adrid,
      "addr_person":  addr.person,
      "addr_street":  addr.street,
      "addr_city": addr.city,
      "addr_state": addr.state,
      "addr_zip":  addr.zipcode
    }

    return aj


class PersonHandler(CorsHandler):
    def initialize(self, person_dao):
        self.person_dao = person_dao

    def post(self):
        print(self.request.body)
        self.write(tornado.escape.json_encode(rtv))

    def get(self):
        addresses = self.person_dao.query_addresses()
        print(addresses)
