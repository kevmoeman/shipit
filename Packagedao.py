import pymysql
import Package as pkg
import Address as adr

class Packagedao(object):
    def __init__(self, username, password, host, db):
        self.username = username
        self.password = password
        self.host = host
        self.db = db

#QUERYS all packages
    def query_packages(self):
        pkglst = []
        conn = pymysql.connect(user=self.username,
                               password=self.password,
                               host=self.host,
                               database=self.db)
        cur = conn.cursor()

        cur.execute( \
        """
        SELECT *
        FROM package
        """
        )


        for row in cur:
            print(row)
            p = pkg.Package(id=row[0], size_id=row[1], src_id=row[2],
                          dst_id=row[3])
            pkglst.append(p)

        cur.close()

        conn.close()
        return pkglst

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
            print(row)
            a = adr.Address(adrid=row[0], person=row[1], street=row[2],
                          zipcode=row[3], city=row[4], state=row[5])
            addrlst.append(a)
        cur.close()

        conn.close()
        return addrlst
#querys individual packages

    def query_package(self, pkgid):
        conn = pymysql.connect(user=self.username,
                               password=self.password,
                               host=self.host,
                               database=self.db)
        cur = conn.cursor()

        cur.execute("SELECT * FROM package WHERE pkgid =%s", (pkgid))
        row = cur.fetchone()

        if row:
            p = pkg.Package(id=row[0], size_id=row[1], src_id=row[2],
                      dst_id=row[3])
        else:
            p = None

        cur.close()

        conn.close()
        return p

    def query_person(self, pkgid):
        conn = pymysql.connect(user=self.username,
                               password=self.password,
                               host=self.host,
                               database=self.db)
        cur = conn.cursor()

        cur.execute("SELECT * FROM package WHERE pkgid =%s", (pkgid))
        row = cur.fetchone()

        if row:
            p = pkg.Package(id=row[0], size_id=row[1], src_id=row[2],
                      dst_id=row[3])
        else:
            p = None

        cur.close()

        conn.close()
        return p


    def insert_package(self, package):
        #inserts a new package into the database.
        #connect to db
        conn = pymysql.connect(user=self.username,
                               password=self.password,
                               host=self.host,
                               database=self.db)
        cur = conn.cursor()
        # Insert new package
        add_package_sql = \
        """
        INSERT INTO package(pkgid, packagesize_id, src_id, dst_id)
        VALUES (%s, %s, %s, %s)
        """
        cur.execute(add_package_sql, (package.id,
                                      package.size_id,
                                      package.src_id,
                                      package.dst_id))
        conn.commit()
        cur.close()

        conn.close()

# to do add cool querie functions to see who has most packagees etc.
