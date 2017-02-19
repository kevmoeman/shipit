import Station
import pymysql


class Stationdao(object):
    def __init__(self, username, password, host, db):
        self.username = username
        self.password = password
        self.host = host
        self.db = db

    def query_stations(self):
        stationlst = []
        conn = pymysql.connect(user=self.username,
                               password=self.password,
                               host=self.host,
                               database=self.db)
        cur = conn.cursor()

        cur.execute( \
        """
        SELECT *
        FROM station

        """
        )
        for row in cur:
            print(row)
            a = Station.Station(stationid=row[0], phonenumber=row[1], st_street=row[2],
                          st_zipcode=row[3], st_city=row[4], st_state=row[5])
            stationlst.append(a)
        cur.close()

        conn.close()
        return stationlst

    def insert_station(self, station):
        #inserts a new package into the database.
        #connect to db
        conn = pymysql.connect(user=self.username,
                               password=self.password,
                               host=self.host,
                               database=self.db)
        cur = conn.cursor()
        # Insert new package
        add_station_sql = \
        """
        INSERT INTO station(stationid, phonenumber, st_zipcode, st_city, st_state)
        VALUES (%s, %s, %s, %s, %s)
        """
        cur.execute(add_station_sql, (station.stationid,
                                      station.phonenumber,
                                      station.st_zipcode,
                                      station.st_city,
                                      st_state))
        conn.commit()
        cur.close()

        conn.close()
