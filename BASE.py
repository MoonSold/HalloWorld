from sqlite3 import *  

MY_BASE = connect("ALL_BASE_PASSWORD.db") 

CURSOR = MY_BASE.cursor()  


CURSOR.execute("""CREATE TABLE base(SNP TEXT,PASSWORD TEXT,MAIL TEXT)""") 

CURSOR.execute("""INSERT INTO base (SNP,PASSWORD,MAIL) VALUES ("Seliverstov Nickita Denisovich","s78945","LP45@mail.ru" )""")
CURSOR.execute("""INSERT INTO base (SNP,PASSWORD,MAIL) VALUES ("Perov Michail Urievich","qwerty123","POI7@mail.ru")""")
CURSOR.execute("""INSERT INTO base (SNP,PASSWORD,MAIL) VALUES ("Anton Riabov Andreevich","s745454","ART@mail.ru")""")



MY_BASE.commit() 
MY_BASE.close()