
import tornado.ioloop
import tornado.web
from config import config
import os
import dao
from handlers import PackageHandler, PersonHandler, VehicleStationHandler


def make_app(address_dao, package_dao, vehicle_dao, station_dao):

    settings = {
        "static_path": os.path.join(os.path.dirname(__file__), os.pardir, "web"),
        "cookie_secret": "__TODO:_GENERATE2_YOUR_OWN_RANDOM_VALUE_HERE__",
        "xsrf_cookies": True,
    }
    print(settings['static_path'])
    return tornado.web.Application([
        (r"/packages", PackageHandler, dict(package_dao=package_dao,
                                           address_dao=address_dao)),
        (r"/vehicles", VehicleStationHandler, dict(vehicle_dao=vehicle_dao,
                                                station_dao=station_dao)),

       (r'/(.*)', tornado.web.StaticFileHandler, {'path': settings['static_path']}),
    ], **settings)

if __name__ == "__main__":
    #start the server
    packagedao = dao.Packagedao(**config)
    addressdao = dao.Addressdao(**config)
    vehicledao = dao.Vehicledao(**config)
    stationdao = dao.Stationdao(**config)

    app = make_app(addressdao, packagedao, vehicledao, stationdao)
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
