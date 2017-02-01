import Vehicle


class Vehicledao(object):
    def __init__(self, username, password, host, db):
        self.username = username
        self.password = password
        self.host = host
        self.db = db

    def query_vehicles(self):
        vehiclelst = []
        conn = pymysql.connect(user=self.username,
                               password=self.password,
                               host=self.host,
                               database=self.db)
        cur = conn.cursor()

        cur.execute( \
        """
        SELECT *
        FROM vehicle
        """
        )


        for row in cur:
            print(row)
            p = Vehicle.Vehicle(id=row[0], company=row[1])
            vehiclelst.append(p)

        cur.close()

        conn.close()
        return vehiclelst

    def insert_vehicle(self, vehicle):
        #inserts a new package into the database.
        #connect to db
        conn = pymysql.connect(user=self.username,
                               password=self.password,
                               host=self.host,
                               database=self.db)
        cur = conn.cursor()
        # Insert new package
        add_vehicle_sql = \
        """
        INSERT INTO vehicle(vehicle_id, company)
        VALUES (%s, %s)
        """
        cur.execute(add_vehicle_sql, (Vehicle.id,
                                      Vehicle.company,
                                      ))
        conn.commit()
        cur.close()

        conn.close()
