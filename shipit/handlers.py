
import json
import Package
import Vehicle
import Station
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

class VehicleStationHandler(CorsHandler):

    def initialize(self, vehicle_dao, station_dao):
        self.vehicle_dao = vehicle_dao
        self.station_dao = station_dao

    def get(self):
        """
            [
                {
                    "id": '1x23',
                    "company": "van stackers",
                    "location": {
                      "station_id": 1,
                      "station_street": "123 Code St",
                      "station_city":"Minneapolis",
                      "station_state":"MN",
                      "station_zip": "55414"
                },
            ]
        """
        vehicles = self.vehicle_dao.query_vehicles()
        stations = self.station_dao.query_stations()

        # create an index of addresses
        station_lookup = { a.stationid : a for a in stations }

        vehicle_jsons = []
        for v in vehicles:
            # first convert vehicle attributes to json
            vj = vehicle_to_json(v)


            # then convert the nested addresses to json
            #TODO MAKE THIS THING WORK
            # locationj = station_to_json(station_lookup[vj['location']])
            # vj['location'] = locationj
            #
            # vehicle_jsons.append(vj)

        self.write(tornado.escape.json_encode(vehicle_jsons))
                # for p in packages:
                #     # first convert package attributes to json
                #     pj = package_to_json(p)
                #     # then convert the nested addresses to json
                #     srcj = address_to_json(address_lookup[pj['src']])
                #     pj['src'] = srcj
                #
                #     dstj = address_to_json(address_lookup[pj['dst']])
                #     pj['dst'] = dstj
                #     package_jsons.append(pj)
                #
                # self.write(tornado.escape.json_encode(package_jsons))

def station_to_json(addr):
    aj = {
      "stationid": st.adrid,
      "st_street":  st.street,
      "st_city": st.city,
      "st_state": st.state,
      "st_zip":  st.zipcode,
      "phonenumber" : st.phonenumber
    }

    return aj



def vehicle_to_json(v):
    vj = {'id':v.id,
        'company':v.company,
        'location':v.location
        }

    return vj
