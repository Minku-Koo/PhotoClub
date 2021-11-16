# Database Information
host = $HOST
db_name = $DB_NAME
port  = $PORT
user = $USER
pwd = $PASSWORD
charset = "utf8"

# Database Table Information
tables = {
    "user" : """
        id INT(3) NOT NULL AUTO_INCREMENT,
        name VARCHAR(5) NOT NULL,
        major VARCHAR(15) NULL,
        number INT(2) NOT NULL,
        profile VARCHAR(30) NULL,
        position VARCHAR(10) NULL,
        graduate INT(1) NOT NULL,
        PRIMARY KEY(id)
    """,

    "photo" : """
        id INT(4) NOT NULL AUTO_INCREMENT,
        user_id INT(5) NOT NULL,
        file VARCHAR(40) NOT NULL,
        PRIMARY KEY(id)
    """,

    "site" : """
        no INT(4) NOT NULL AUTO_INCREMENT,
        poster VARCHAR(30) NOT NULL,
        intro VARCHAR(700) NOT NULL,
        student_intro VARCHAR(700) NOT NULL,
        graduated_intro VARCHAR(700) NOT NULL,
        PRIMARY KEY(no)
    """,

    "history" : """
        no INT(4) NOT NULL AUTO_INCREMENT,
        file VARCHAR(50) NOT NULL,
        event_title VARCHAR(40) NOT NULL,
        year INT(4) NULL,
        PRIMARY KEY(no)
    """,

    "club_event" : """
        no INT(4) NOT NULL AUTO_INCREMENT,
        title VARCHAR(200) NOT NULL,
        year INT(4) NOT NULL,
        PRIMARY KEY(no)
    """,

    "faq" : """
        no INT(4) NOT NULL AUTO_INCREMENT,
        question VARCHAR(200) NOT NULL,
        answer VARCHAR(300) NOT NULL,
        PRIMARY KEY(no)
    """,
}

manager_password = $M_PASSWORD
