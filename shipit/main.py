import pymysql
import Package as p
import Packagedao as pdao
from config import config



if __name__ == '__main__':

    ## PRETEND WE READ A PACKAGE ID FROM USER
    pid = '13'

    ###
    p = p.Package(pid, 1, 1, 2)

    # we want to save p to the database

    #instead of login info store in different file and gitignore that
    packagedao = pdao.Packagedao(config.username, config.password,
                                 config.host, config.database)
    #queury package check for same
    package = packagedao.query_package(p.id)
    print(package)



    #save package to db
    packagedao.insert_package(p)


    package = packagedao.query_package(p.id)
    print(package)
