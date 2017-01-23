import tornado.ioloop
import tornado.web
import json
import Package
import Packagedao
import config
import Address



# def package_to_json(pkg):
#     pid = Package.Package.id
#
#         ###
#     p = Package.Package(pid, 1, 1, 2)
#     pj = {'id':p.id, 'size_id':p.size_id, 'src_id':p.src_id, 'dst_id':p.dst_id}
#
#     return pj
# def address_to_json(addr):


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
    def initialize(self, dao):
        self.pdao = dao

    def post(self):
        print(self.request.body)
        self.write(tornado.escape.json_encode(rtv))

    def get(self):
        packages = self.pdao.query_packages()
        # package = self.pdao.query_package()
        # print(package_to_json(package))
        print(packages)



class PersonHandler(CorsHandler):
    def initialize(self, dao):
        self.pdao = dao

    def post(self):
        print(self.request.body)
        self.write(tornado.escape.json_encode(rtv))

    def get(self):
        addresses = self.pdao.query_addresses()
        print(addresses)

def make_app(dickhead):

    return tornado.web.Application([
        (r"/package", PackageHandler, dict(dao=dickhead)),
        (r"/address", PersonHandler, dict(dao=dickhead))
    ])

if __name__ == "__main__":
    #start the server
    packagedao = Packagedao.Packagedao(config.username, config.password,
                                     config.host, config.database)
    app = make_app(packagedao)
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
    ## PRETEND WE READ A PACKAGE ID FROM USER


    # we want to save p to the database

    #instead of login info store in different file and gitignore that

    #queury package check for same




    #save package to db
    packagedao.insert_package(p)


    package = packagedao.query_package(p.id)
    print(package)
