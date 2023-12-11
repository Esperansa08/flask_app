import mysql.connector
from mysql.connector import Error


def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            charset="utf8",
            database=db_name,
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


# ] = "mysql+pymysql://flask:slimdingo85@mysql:3306/flask"  #'mysql+pymysql://{}:{}@{}/{}'.format(
#     os.getenv('DB_USER', 'flask'), 'mysql+pymysql://flask:slimdingo85@mysql:3306/flask'
#     os.getenv('DB_PASSWORD', ''),
#     os.getenv('DB_HOST', 'mysql'),
#     os.getenv('DB_NAME', 'flask')
# )
connection = create_connection("127.0.0.1", "flask", "slimdingo85", "flask")
create_database_query = "CREATE DATABASE IF NOT EXISTS flask DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;"
create_database(connection, create_database_query)


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


create_user_table = """
CREATE TABLE IF NOT EXISTS user (
  id INT AUTO_INCREMENT,
  username char(50) UNIQUE NOT NULL,
  email char(50) UNIQUE NOT NULL,
  password_hash varchar(128) NOT NULL,
  PRIMARY KEY (id)
) ENGINE = InnoDB
"""

execute_query(connection, create_user_table)

create_anime_table = """
CREATE TABLE IF NOT EXISTS anime (
  id INT AUTO_INCREMENT,
  title TEXT NOT NULL,
  description TEXT NOT NULL,
  PRIMARY KEY (id)
) ENGINE = InnoDB
"""

execute_query(connection, create_anime_table)

create_users = """
INSERT INTO
  `user` (`username`, `email`, `password_hash`)
VALUES
  ('Pupkin22', 'Pupkin22@mail.ru', 'pbkdf2:sha256:260000$8XcN3mVbimW23oNz$57d5166bdcb3d6af440e8ddd1c5ed0912dcfe537f18ae922cd940475c3214629')
"""

execute_query(connection, create_users)

create_anime = """
INSERT INTO
  `anime` (`title`, `description`)
VALUES
  ('Ходячий замок', 'Восемнадцатилетняя шляпница Софи ведёт тихую и ничем не примечательную городскую жизнь. Однако типичный её распорядок рушится, когда в окрестностях города объявляется Ходячий замок Хаула — колдуна, заключившего сделку с демоном огня Кальцифером и носящего дурную славу «похитителя» девичьих сердец.'),
  ('Унесённые призраками', 'Десятилетняя Тихиро Огино вместе с родителями садится в машину, чтобы добраться до нового дома, расположенного где-то в глубинке Японии. Решив срезать путь, они попадают в необычный лес, выбравшись из которого, оказываются на прогалине, откуда можно выйти лишь сквозь мощёный тоннель. Пройдя по нему, они оказываются в пустующем заброшенном городке, в котором нет ни души, зато прилавки ломятся от деликатесов. Родители Тихиро решают перекусить, а расплатиться, когда появятся хозяева. Любопытная, как все дети, Тихиро отправляется побродить и вскоре натыкается на мальчика Хаку, потребовавшего, чтобы она немедленно ушла. Уже смеркается, и город наводняют странные звуки и тени. Вернувшись к родителям, Тихиро в ужасе видит, как те полнеют на глазах и в итоге превращаются в свиней.'),
  ('Наруто', 'В день рождения Наруто Узумаки на деревню под названием Коноха напал легендарный демон, Девятихвостый лис. Четвёртый Хокагэ ценой своей жизни спас деревню, запечатав демона в новорождённом Наруто, неосознанно обрекая его на жизнь в ненависти односельчан.');
"""

execute_query(connection, create_anime)
