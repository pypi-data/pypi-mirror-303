from lightphe import LightPHE

class HomomorphicEncryption:
    def __init__(self, algorithm_name="Paillier"):
        # สร้างคู่กุญแจส่วนตัว-สาธารณะ
        self.cs = LightPHE(algorithm_name=algorithm_name)
        self.cs.export_keys(target_file="public.txt", public=True)
        self.cs.export_keys(target_file="private.txt", public=False)

    def encrypt(self, message):
        """ฟังก์ชันการเข้ารหัส"""
        return self.cs.encrypt(message)

    def decrypt(self, ciphertext):
        """ฟังก์ชันการถอดรหัส"""
        return self.cs.decrypt(ciphertext)

# ตัวอย่างการใช้งาน
if __name__ == "__main__":
    # สร้างอ็อบเจ็กต์ Homomorphic
    homomorphic_encryption = HomomorphicEncryption()

    # กำหนดข้อความธรรมชาติ
    m1 = 17
    m2 = 23

    # เข้ารหัสข้อความ
    c1 = homomorphic_encryption.encrypt(m1)
    c2 = homomorphic_encryption.encrypt(m2)

    print("Ciphertext 1:", c1.value)  # แสดง ciphertext
    print("Ciphertext 2:", c2.value)  # แสดง ciphertext

    # ถอดรหัสข้อความ
    dec_m1 = homomorphic_encryption.decrypt(c1)
    dec_m2 = homomorphic_encryption.decrypt(c2)

    print("Decrypted message 1:", dec_m1)  # ควรแสดง 17
    print("Decrypted message 2:", dec_m2)  # ควรแสดง 23
