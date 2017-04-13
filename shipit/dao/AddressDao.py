import Address
import pymysql

class Addressdao(object):
    def __init__(self, username, password, host, db):
        self.username = username
        self.password = password
        self.host = host
        self.db = db

    def query_addresses(self):
        addrlst = []
        conn = pymysql.connect(user=self.username,
                               password=self.password,
                               host=self.host,
                               database=self.db)
        cur = conn.cursor()

        cur.execute( \
        """
        SELECT *
        FROM address

        """
        )
        for row in cur:
            a = Address.Address(adrid=row[0], person=row[1], street=row[2],
                          zipcode=row[3], city=row[4], state=row[5])
            addrlst.append(a)
        cur.close()

        conn.close()
        return addrlst

    def query_address(self, adr_id):
        conn = pymysql.connect(user=self.username,
                               password=self.password,
                               host=self.host,
                               database=self.db)
        cur = conn.cursor()
        sql = "SELECT * FROM address WHERE addr_id=(%s)"
        cur.execute(sql, adr_id)

        row = cur.fetchone()

        if row:
            a = Address.Address(adrid=row[0], person=row[1], street=row[2],
                          zipcode=row[3], city=row[4], state=row[5])
        else:
            a = None

        cur.close()

        conn.close()
        return a