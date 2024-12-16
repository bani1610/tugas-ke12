from animal import Animal

class Fish(Animal):
    def __init__(self, name, makan, hidup, berkembang_biak, bernapas, habitat):
        super().__init__(name, makan, hidup, berkembang_biak)
        self.bernapas = bernapas
        self.habitat = habitat
    
    def info_Fish(self):
        super().info_animal()
        print("Bernapas\t\t:", self.bernapas,
              "\nHabitat\t\t\t:", self.habitat)
        
hiu = Fish("hiu", "daging", "laut", "melahirkan", "insang", "air laut")
salmon = Fish('salmon', 'ikan-ikan kecil', 'sungai', 'bertelur', 'insang', 'air tawar')
cupang= Fish('cupang', 'daging', 'air tawar', 'bertelur', 'insang', 'air tawar')
print('\t\tini hiu')
hiu.info_Fish()
print('\t\tini salmon')
salmon.info_Fish()
print('\t\tini cupang')
cupang.info_Fish()