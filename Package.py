import pymysql



class Package(object):
    def __init__(self, id, size_id, src_id, dst_id):
        self.id = id
        self.size_id = size_id
        self.src_id = src_id
        self.dst_id = dst_id

    def __str__(self):
        return str( "P[id:"+str(self.id) + " size: " + str(self.size_id) +
        " src:" + str(self.src_id) + " dst:" + str(self.dst_id)+"]")
