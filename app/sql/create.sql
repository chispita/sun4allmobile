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
