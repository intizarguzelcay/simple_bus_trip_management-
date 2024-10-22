#İNTİZAR GÜZELÇAY
#18.05.2024
#Obilet ödev


from create_obilet import Obilet 

yol = {"user": "root", "password": "", "host": "127.0.0.1", "database": "obilet"}

obilet = Obilet(yol)

obilet.add_firm("KAMİL KOC")
obilet.add_firm("METRO")
obilet.add_firm("PAMUKKALE")
obilet.add_firm("ALİ ULUSOY")

obilet.add_route("İZMİR-MANİSA-SAKARYA-GEBZE-İSTANBUL")

obilet.add_trips(0,1, "İZMİR-İSTANBUL")
obilet.add_trips(0,1, "İZMİR-MANİSA")
obilet.add_trips(0,1, "MANİSA-SAKARYA")
obilet.add_trips(0,1,"SAKARYA-İSTANBUL")
obilet.add_trips(1,1, "İSTANBUL-GEBZE")
obilet.add_trips(1,1, "İSTANBUL-MANİSA")
obilet.add_trips(1,1, "İSTANBUL-İZMİR")

obilet.add_trip(15, 26, "10:00")
obilet.add_trip(16, 27 ,"12:00")
obilet.add_trip(17, 28, "11:00")

obilet.generate_trip_file()
