from animal import Animal

class Bird(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, warna, paruh):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.paruh = paruh

    def info_bird(self):
        super().info_animal()
        print("warna\t\t\t:", self.warna, 
              "\nJenis paruh\t\t:", self.paruh)
        
bird = Bird("elang", "daging", "digunung", "bertelur", "coklat", "panjang dan kuat")
burung = Bird("burung hantu", "serangga", "dipohon", "bertelur", "hitam", "pendek")
lovebrid= Bird("lovebird", "Sayuran", "dipohon", "bertelur", "hijau", "pendek")
print('\t\tini elang')
bird.info_bird()
print('\t\tini Burung hantu')
burung.info_bird()
print('\r\tini Burung Lovebird')
lovebrid.info_bird()