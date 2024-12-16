from animal import Animal

class ular(Animal):
    def __init__(self, name , makanan, hidup , berkembang_biak, warna, berbisah):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.berbisah = berbisah

    def info_ular(self):
        super().info_animal()
        print("warna\t\t\t:", self.sisik, 
              "\nJenis paruh\t\t:", self.berbisah)
        
cobra = ular('cobra', 'daging', 'rawa', 'bertelur', 'hitam', 'bebisah' )
anakconda = ular('anak conda', 'daging', 'hutan', 'bertelur', 'sisik dorsal', 'tidak berbisah')
kelabu =ular("ular kelabu", 'daging', 'hutan', 'bertelur' , 'hijau', 'tidak berbisah')

print('\t\tINI cobra')
cobra.info_ular()
print('\t\tINI python')
anakconda.info_ular()
print('\t\tINI ular kelabu')
kelabu.info_ular()