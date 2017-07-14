SET FOREIGN_KEY_CHECKS=0;

truncate table scanner_details;
truncate table date_details;
truncate table version_details;
truncate table gradsys_details;
truncate table coil_details;
truncate table phantom_details;
truncate table results;
truncate table series_details;

LOAD DATA LOCAL INFILE '/home/rebecca/UHB/UHB_database_scripts/scanner_info' 
INTO TABLE scanner_details 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '' 
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE '/home/rebecca/UHB/UHB_database_scripts/date_table'
INTO TABLE date_details 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '' 
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE '/home/rebecca/UHB/UHB_database_scripts/version_table'
INTO TABLE version_details 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '' 
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE '/home/rebecca/UHB/UHB_database_scripts/gradsys_table'
INTO TABLE gradsys_details 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '' 
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE '/home/rebecca/UHB/UHB_database_scripts/coil_table'
INTO TABLE coil_details 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '' 
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE '/home/rebecca/UHB/UHB_database_scripts/phantom_table'
INTO TABLE phantom_details 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '' 
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE '/home/rebecca/UHB/UHB_database_scripts/results_table'
INTO TABLE results 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '' 
LINES TERMINATED BY '\n';

LOAD DATA LOCAL INFILE '/home/rebecca/UHB/UHB_database_scripts/series_table'
INTO TABLE series_details 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '' 
LINES TERMINATED BY '\n';

