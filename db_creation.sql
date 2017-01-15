DROP DATABASE shipit;

CREATE DATABASE shipit;

USE shipit;

-- CREATE MY TABLES
CREATE TABLE Package (
	pkgid INTEGER,  
	size TEXT, 
	destination VARCHAR(40),
    PRIMARY KEY(pkgid)
);

CREATE TABLE Vehicle (
	vnum VARCHAR(10), 
	company VARCHAR(10),
    PRIMARY KEY(vnum)
);

CREATE TABLE Station (
	stationid VARCHAR(10), 
	description VARCHAR(40), 
	phonenumber BIGINT UNSIGNED,
    PRIMARY KEY(stationid)
);

CREATE TABLE Packagestate (
	pkgid INTEGER, 
	stationid VARCHAR(10), 
	pkg_status TEXT,
    FOREIGN KEY(pkgid) REFERENCES package(pkgid),
    FOREIGN KEY(stationid) REFERENCES station(stationid)
);

CREATE TABLE Vehiclestate (
	vnum VARCHAR(10), 
	stationid VARCHAR(10),
	vstatus TEXT,
    FOREIGN KEY(vnum) REFERENCES vehicle(vnum),
	FOREIGN KEY(stationid) REFERENCES station(stationid)
);



