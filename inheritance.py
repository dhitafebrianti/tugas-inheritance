class Mahasiswa(object):
  def __init__(self, t, p, s):
    self.tekom = t
    self.ptik = p
    self.seni = s
    
  def jumlahMahasiswa(self):
     return self.tekom + self.ptik + self.seni
     
  def cetakData(self):
     print("tekom\t:", self.tekom)
     print("ptik\t:", self.ptik)
     print("seni\t:", self.seni)
   
  def cetakJM(self):
     print("total dari semua mahasiswa diatas\t=", self.jumlahMahasiswa())
     
     
class WarnaMahasiswa(Mahasiswa):
  def __init__(self, t, p, s, w):
      self.tekom = t
      self.ptik = p
      self.seni = s
      self.warna = w
  def cetakData(self):
      print("tekom\t:", self.tekom)
      print("ptik\p:", self.ptik)
      print("seni\t:", self.seni)
      print("Warna dari Almamater Mahasiswa tersebut adalah", self.warna)
      
def main ():
     wh1 = WarnaMahasiswa( 155, 200, 150, "orengs")
      
     wh1.cetakData()
     wh1.cetakJM()
     
if __name__ == "__main__":
   main()
