from random import randint
#tried to make id a unique random number but save 4 later
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

class Package(object):
    def __init__(self, id, size_id, src_id, dst_id):
        self.id = id
        self.size_id = size_id
        self.src_id = src_id
        self.dst_id = dst_id

    def __str__(self):
        return str( "P[id:"+str(self.id) + " size: " + str(self.size_id) +
        " src:" + str(self.src_id) + " dst:" + str(self.dst_id)+"]")
