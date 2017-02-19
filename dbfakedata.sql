-- addr_id INTEGER,
	-- addr_person TEXT,
    -- addr_street VARCHAR(40),
-- addr_zip INTEGER,
    -- addr_city TEXT,
   --  addr_state TEXT,


INSERT INTO address(addr_id, addr_person, addr_street, 
addr_zip, addr_city, addr_state)
VALUES (1, 'ROBBY1', '9231 robby ln', 45632, 'rby', 'WI'),
(2, 'codder', '23425 codder ave', 34342, 'grn bay', 'WI'), 
(3, 'vanzee', '345345 vz cir', 22334, 'fancytown','WA');


INSERT INTO package(pkgid, packagesize_id, src_id, dst_id)
VALUES (1, 2, 3, 2), (2, 3, 2, 3), (3, 1, 1, 2);

INSERT INTO station(stationid, st_street, st_zip, st_city, 
st_state, phonenumber)
VALUES (1, '8534 industrial lane', 55345, 'Minneapolis', 'MN',
7828856666),
(2, '44325 shipper st', 55443, 'Vanville', 'OK',
9926523322);


INSERT INTO vehicle(vehicle_id, company, location)
VALUES (322322, 'Codder Direct', 2),
(623623, 'DaBoys', 1),
(123123, 'Stacker and sons', 2);

