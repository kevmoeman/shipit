DROP DATABASE shipit;

CREATE DATABASE shipit;

USE shipit;

-- CREATE MY TABLES



CREATE TABLE address (
	addr_id INTEGER,
	addr_person TEXT,
    addr_street VARCHAR(40),
    addr_zip INTEGER,
    addr_city TEXT,
    addr_state TEXT,
	PRIMARY KEY(addr_id)
);
CREATE TABLE packagesize(
	packagesize_id smallint,
    size_desc VARCHAR(32),
	PRIMARY KEY(packagesize_id)
);
INSERT INTO packagesize(packagesize_id, size_desc)
VALUES (1, 'small'),(2, 'ic'),(3, 'reg');

CREATE TABLE package (
	pkgid INTEGER NOT NULL AUTO_INCREMENT,
	packagesize_id smallint,
    src_id INTEGER,
    dst_id INTEGER,
    PRIMARY KEY(pkgid),
    FOREIGN KEY(packagesize_id) REFERENCES packagesize(packagesize_id),
    FOREIGN KEY (src_id) REFERENCES address(addr_id),
    FOREIGN KEY (dst_id) REFERENCES address(addr_id)

);

CREATE TABLE vehicle (
	vehicle_id VARCHAR(10) COMMENT 'Vehicle internal company string' ,
	company VARCHAR(10),
    PRIMARY KEY(vehicle_id)
);

CREATE TABLE station (
	stationid VARCHAR(10) COMMENT 'station identification string',
	st_street VARCHAR(40),
    st_zip INTEGER,
    st_city TEXT,
    st_state TEXT,
	phonenumber BIGINT UNSIGNED,
    PRIMARY KEY(stationid)
);

CREATE TABLE package_status_codes ( -- insert status codes
	package_status_id_code INTEGER,
	PRIMARY KEY(package_status_id_code)
);

CREATE TABLE packagestate (
    package_state_id BIGINT auto_increment,
	pkgid INTEGER,
	stationid VARCHAR(10),  -- enforce @ applciation level that only 1 is set.
    vehicle_id VARCHAR(10),  -- enforce @ applciation level that only 1 is set.
	package_status_id_code INTEGER,
    ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY(package_state_id),
    FOREIGN KEY(pkgid) REFERENCES package(pkgid),
    FOREIGN KEY(stationid) REFERENCES station(stationid),
    FOREIGN KEY(package_status_id_code) REFERENCES package_status_codes(package_status_id_code)
);
CREATE TABLE vehicle_status_codes ( -- insert vehicle codes
	vehicle_state_id INTEGER,
    PRIMARY KEY(vehicle_state_id)
);

CREATE TABLE vehiclestate (
	vehicle_id VARCHAR(10),
	stationid VARCHAR(10),
	vehicle_state_id INTEGER,
	FOREIGN KEY(vehicle_id) REFERENCES vehicle(vehicle_id),
    FOREIGN KEY(stationid) REFERENCES station(stationid),
    FOREIGN KEY(vehicle_state_id) REFERENCES vehicle_status_codes(vehicle_state_id)
);

	-- FOREIGN KEY(stationid) REFERENCES station(stationid),
    -- FOREIGN KEY(vehicle_state_id) REFERENCES vehicle_status_codes(vehicle_state_id)
