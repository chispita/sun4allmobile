use DBSunMobile;

DROP TABLE images;
CREATE TABLE images(
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        description VARCHAR(50),
        browser VARCHAR(100),
        source_ip VARCHAR(15),
        created TIMESTAMP DEFAULT NOW(),
        deleted TIMESTAMP
); 

DROP TABLE points;
CREATE TABLE points(
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        images_id int,
        x double,
        y double,
        browser VARCHAR(100),
        source_ip VARCHAR(15),
        created TIMESTAMP DEFAULT NOW(),
        deleted TIMESTAMP
);

DROP TABLE cellresults;
CREATE TABLE cellresults(
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        image_name VARCHAR(50) NOT NULL,
        browser VARCHAR(100),
        source_ip VARCHAR(15),
        created TIMESTAMP DEFAULT NOW(),
        deleted TIMESTAMP
); 

DROP TABLE cellmarks;
CREATE TABLE cellmarks(
        id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        typeofmarking INT NOT NULL,
        x double NOT NULL,
        y double NOT NULL,
        result_id INT,
        browser VARCHAR(100),
        source_ip VARCHAR(15),
        created TIMESTAMP DEFAULT NOW(),
        deleted TIMESTAMP,
        FOREIGN KEY (result_id) REFERENCES cellresults (id)
);
