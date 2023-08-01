import mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", password = "password", database = "airlines_booking")
cur = mydb.cursor()
cur.execute("\
insert into flights values\
(1, 'spicejet', 'MUMBAI', 'delhi', 'SG815', '07:20:00', '09:35:00', 7200),\
(2,'spicejet','chennai','pune','SG773','13:35:00','15:15:00',8100),\
(3,'spicejet','chennai','hyderabad','SG731','06:20:00','07:30:00',5200),\
(4,'spicejet','goa','bengaluru','SG3720','08:10:00','09:55:00',6500),\
(5,'spicejet','pune','bengaluru','SG493','17:25:00','19:55:00',8500),\
(6,'VISTARA','NEW DELHI','HYDERABAD','UK-879','17:40:00','19:50:00',5000),\
(7,'VISTARA','NEW DELHI','BENGALURU','UK-811','06:15:00','09:00:00',6528),\
(8,'VISTARA','MUMBAI','JAIPUR','UK-819','20:00:OO','06:45:00',4379),\
(9,'VISTARA','CHENNAI','PUNE','UK-832','07:05:00','19:55:00',6927),\
(10,'VISTARA','LUCKNOW','GOA','UK-835','17:50:00','13:50:00',8552),\
(11,'GOAIR','MUMBAI','DELHI','G8395','01:45:00','03:30:00',5500),\
(12,'GOAIR','NEW DELHI','CHENNAI','G8461','07:45:00','22:20:00',8500),\
(13,'GOAIR','AURANGABAD','DELHI','G8492','08:00:00','23:00:00',5200),\
(14,'GOAIR','AHEMDABAD','CHANDIGARH','G8911','09:00:00','10:00:00',8800),\
(15,'GOAIR','AHEMDABAD','JAIPUR','G8702','16:30:00','17:55:00',4500),\
(16,'AIRINDIA','SRINAGAR','HYDERABAD','AI-802','14:40:00','20:00:00',9200),\
(17,'AIRINDIA','HYDERABAD','JAIPUR','AI-821','06:15:00','12:00:00',7500),\
(18,'AIRINDIA','BENGALURU','HARAYANA','AI-815','07:00:00','07:30:00',6300),\
(19,'AIRINDIA','MUMBAI','DELHI','AI-573','12:45:00','01:20:00',7800),\
(20,'AIRINDIA','LUCKNOW','MUMBAI','AI-550','23:45:00','00:00:00',7500),\
(21,'INDIGO','AGRA','BENGALURU','6E-5917','18:00:00','18:30:00',6650),\
(22,'INDIGO','AHMEDABAD','LUCKNOW','6E-544','03:50:00','04:10:00',8245),\
(23,'INDIGO','BANGKOK','DELHI','6E-0086','12:35:00','01:00:00',8500),\
(24,'INDIGO','BENGALURU','KOLKATA','6E-0954','04:25:00','04:55:00',5550),\
(25,'INDIGO','BHOPAL','SURAT','6E-0745','15:30:00','16:00:00',8500) ;\
")
mydb.commit()
