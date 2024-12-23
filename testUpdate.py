import unittest
from docx import Document
import os
from main import updateStatus
FILENAME = "demo.docx"
class TestFoodOrder(unittest.TestCase):
    def testUpdateStatus(self):
        # Daftar nama yang akan diuji
        namesArr = [f"Person_{i}" for i in range(1, 101)]  # Person_1 hingga Person_100

        # Memanggil updateStatus untuk setiap nama berdasarkan genap/ganjil
        for name in namesArr:
            if int(name.split('_')[1]) % 2 == 0:  # Nama genap
                updateStatus(name,"Selesai")
            else:  # Nama ganjil
                updateStatus(name, "Batal")

        # Membaca ulang dokumen untuk validasi
        doc = Document(FILENAME)
        for paragraph in doc.paragraphs:
            if "Nama" in paragraph.text:
                for name in namesArr:
                    if name in paragraph.text:
                        nameId = int(name.split('_')[1])
                        if nameId % 2 == 0:
                            self.assertIn("Status : Selesai", paragraph.text)
                            print(f"{name} status berhasil diperbarui menjadi Selesai")
                        else: 
                            self.assertIn("Status : Batal", paragraph.text)
                            print(f"{name} status berhasil diperbarui menjadi Batal")
                        break
                else:
                    print("Not Found:", paragraph.text)

if __name__ == "__main__":
    unittest.main()
