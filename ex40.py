# class

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"
                ])

quoc_ca_VN = Song(["Doan quan Viet Nam di", 
                    "Trung long cuu quoc",
                    "Buoc chan ron vang tren duong gap ghenh xa"
                ])

happy_bday.sing_me_a_song()
quoc_ca_VN.sing_me_a_song()