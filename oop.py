# SOLID principles programming
class Human:
    def __init__(self, nama, umur, gender): #construtor
        self.nama = nama
        self.umur = umur
        self.gender = gender

    def memakan(self):
        return self.nama + " memakan"
    
    def meminum(self):
        return self.nama + " meminum"

hanif = Human("hanif", 20, "pria") # initialize -> mulai memanggil class untuk dirubah jadi object
print(hanif.memakan())

abdul = Human("abdul", 20, "pria")
print(abdul.memakan())

# Legacy - code sampah
class UserAuthentication:
    def login(self):
        print("login")

    def logout(self):
        print("logout")

# open-close principle -> inherintence
class UserAuthenticationExtenders(UserAuthentication):
    pass
    # override -> turunin dari parent, terus buat implementasi baru
    # def login(self): # polymorphs
    #     print("login class baru")

user = UserAuthenticationExtenders()
user.login()

# tugas
# buat 1 class
# class ini berfungsi untuk
# menemukan nilai maximum dari kelompok bilangan

# nilaiMax = PencariNilaiMax()
# print(nilaiMax.cari([1,4,6,10,0,2,30])) -> 30