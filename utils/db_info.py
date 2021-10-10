# Database Information
host = "localhost"
db_name = "photoclub"
port  = 3306
user = "root"
pwd = "pwd"
charset = "utf8"

# Database Table Information
tables = {
    "user" : """
        id INT(3) NOT NULL AUTO_INCREMENT,
        name VARCHAR(5) NOT NULL,
        major VARCHAR(15) NULL,
        number INT(2) NOT NULL,
        profile VARCHAR(20) NULL,
        position VARCHAR(10) NULL,
        graduate INT(1) NOT NULL,
        PRIMARY KEY(id)
    """,

    "photo" : """
        id INT(3) NOT NULL,
        file VARCHAR(20) NOT NULL,
        photo_title VARCHAR(20) NULL,
        loc VARCHAR(15) NULL,
        dsc VARCHAR(30) NULL,
        PRIMARY KEY(id)
    """,

    "site" : """
        no INT(4) NOT NULL AUTO_INCREMENT,
        poster VARCHAR(10) NOT NULL,
        intro VARCHAR(300) NOT NULL,
        PRIMARY KEY(no)
    """,

    "history" : """
        no INT(4) NOT NULL AUTO_INCREMENT,
        file VARCHAR(20) NOT NULL,
        event_title VARCHAR(30) NOT NULL,
        year INT(4) NULL,
        loc VARCHAR(15) NULL,
        dsc VARCHAR(30) NULL,
        PRIMARY KEY(no)
    """,

    "club_event" : """
        no INT(4) NOT NULL AUTO_INCREMENT,
        title VARCHAR(15) NOT NULL,
        year INT(4) NOT NULL,
        loc VARCHAR(15) NULL,
        PRIMARY KEY(no)
    """,

    "faq" : """
        no INT(4) NOT NULL AUTO_INCREMENT,
        question VARCHAR(80) NOT NULL,
        answer VARCHAR(100) NOT NULL,
        PRIMARY KEY(no)
    """,
}

manager_password = "tkwls406?"