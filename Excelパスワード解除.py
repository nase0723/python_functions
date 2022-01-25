import msoffcrypto
import glob
import os

# パスワード
PASSWORD = ""

excel_files = glob.glob('*.xlsx')

def password_unlock(encrypted_file_name):
    for file in encrypted_file_name:
        # 暗号化されたファイル
        encrypted_file_name = file
        no_extension = encrypted_file_name.split(".")
        # 復号化して保存するファイル
        decrypted_file_name = no_extension[0] + "パスワード解除.xlsx"
        try:
            # 暗号化ファイルを開く
            f = open(encrypted_file_name, "rb")
            encrypted_file = msoffcrypto.OfficeFile(f)
            # 復号化のパスワードを設定する
            encrypted_file.load_key(password=PASSWORD)
            # 復号化したファイルを別のファイルに保存する
            with open(decrypted_file_name, "wb") as decrypted_file:
                encrypted_file.decrypt(decrypted_file)
        except:
            os.remove(decrypted_file_name)
        f.close()