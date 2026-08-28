# COMPLETE 70 SUBSCRIBERS PLEASE 🥺 

import requests
import binascii
import jwt
from flask import Flask, render_template, request, jsonify
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# Suppress SSL warnings
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)


_sym_db = _symbol_database.Default()

# GameData protobuf
GAMEDATA_DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x08my.proto\"\xae\t\n\x08GameData\x12\x11\n\ttimestamp\x18\x03 \x01(\t\x12\x11\n\tgame_name\x18\x04 \x01(\t\x12\x14\n\x0cgame_version\x18\x05 \x01(\x05\x12\x14\n\x0cversion_code\x18\x07 \x01(\t\x12\x0f\n\x07os_info\x18\x08 \x01(\t\x12\x13\n\x0b\x64\x65vice_type\x18\t \x01(\t\x12\x18\n\x10network_provider\x18\n \x01(\t\x12\x17\n\x0f\x63onnection_type\x18\x0b \x01(\t\x12\x14\n\x0cscreen_width\x18\x0c \x01(\x05\x12\x15\n\rscreen_height\x18\r \x01(\x05\x12\x0b\n\x03\x64pi\x18\x0e \x01(\t\x12\x10\n\x08\x63pu_info\x18\x0f \x01(\t\x12\x11\n\ttotal_ram\x18\x10 \x01(\x05\x12\x10\n\x08gpu_name\x18\x11 \x01(\t\x12\x13\n\x0bgpu_version\x18\x12 \x01(\t\x12\x0f\n\x07user_id\x18\x13 \x01(\t\x12\x12\n\nip_address\x18\x14 \x01(\t\x12\x10\n\x08language\x18\x15 \x01(\t\x12\x0f\n\x07open_id\x18\x16 \x01(\t\x12\x15\n\rplatform_type\x18\x17 \x01(\x05\x12\x1a\n\x12\x64\x65vice_form_factor\x18\x18 \x01(\t\x12\x14\n\x0c\x64\x65vice_model\x18\x19 \x01(\t\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x1d \x01(\t\x12\x18\n\x10unknown_field_30\x18\x1e \x01(\x05\x12\"\n\x1asecondary_network_provider\x18) \x01(\t\x12!\n\x19secondary_connection_type\x18* \x01(\t\x12\x11\n\tunique_id\x18\x39 \x01(\t\x12\x10\n\x08\x66ield_60\x18< \x01(\x05\x12\x10\n\x08\x66ield_61\x18= \x01(\x05\x12\x10\n\x08\x66ield_62\x18> \x01(\x05\x12\x10\n\x08\x66ield_63\x18? \x01(\x05\x12\x10\n\x08\x66ield_64\x18@ \x01(\x05\x12\x10\n\x08\x66ield_65\x18\x41 \x01(\x05\x12\x10\n\x08\x66ield_66\x18\x42 \x01(\x05\x12\x10\n\x08\x66ield_67\x18\x43 \x01(\x05\x12\x10\n\x08\x66ield_70\x18\x46 \x01(\x05\x12\x10\n\x08\x66ield_73\x18I \x01(\x05\x12\x14\n\x0clibrary_path\x18J \x01(\t\x12\x10\n\x08\x66ield_76\x18L \x01(\x05\x12\x10\n\x08\x61pk_info\x18M \x01(\t\x12\x10\n\x08\x66ield_78\x18N \x01(\x05\x12\x10\n\x08\x66ield_79\x18O \x01(\x05\x12\x17\n\x0fos_architecture\x18Q \x01(\t\x12\x14\n\x0c\x62uild_number\x18S \x01(\t\x12\x10\n\x08\x66ield_85\x18U \x01(\x05\x12\x18\n\x10graphics_backend\x18V \x01(\t\x12\x19\n\x11max_texture_units\x18W \x01(\x05\x12\x15\n\rrendering_api\x18X \x01(\x05\x12\x18\n\x10\x65ncoded_field_89\x18Y \x01(\t\x12\x10\n\x08\x66ield_92\x18\\ \x01(\x05\x12\x13\n\x0bmarketplace\x18] \x01(\t\x12\x16\n\x0e\x65ncryption_key\x18^ \x01(\t\x12\x15\n\rtotal_storage\x18_ \x01(\x05\x12\x10\n\x08\x66ield_97\x18\x61 \x01(\x05\x12\x10\n\x08\x66ield_98\x18\x62 \x01(\x05\x12\x10\n\x08\x66ield_99\x18\x63 \x01(\t\x12\x11\n\tfield_100\x18\x64 \x01(\tb\x06proto3'
)
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(GAMEDATA_DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(GAMEDATA_DESCRIPTOR, 'my_pb2', _globals)
GameData = _sym_db.GetSymbol('GameData')

# Garena_420 protobuf
GARENA420_DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x13jwt_generator.proto\"\xd2\x02\n\nGarena_420\x12\x12\n\naccount_id\x18\x01 \x01(\x03\x12\x0e\n\x06region\x18\x02 \x01(\t\x12\r\n\x05place\x18\x03 \x01(\t\x12\x10\n\x08location\x18\x04 \x01(\t\x12\x0e\n\x06status\x18\x05 \x01(\t\x12\r\n\x05token\x18\x08 \x01(\t\x12\n\n\x02id\x18\t \x01(\x05\x12\x0b\n\x03\x61pi\x18\n \x01(\t\x12\x0e\n\x06number\x18\x0c \x01(\x05\x12\x1e\n\tGarena420\x18\x0f \x01(\x0b\x32\x0b.Garena_420\x12\x0c\n\x04\x61rea\x18\x10 \x01(\t\x12\x11\n\tmain_area\x18\x12 \x01(\t\x12\x0c\n\x04\x63ity\x18\x13 \x01(\t\x12\x0c\n\x04name\x18\x14 \x01(\t\x12\x11\n\ttimestamp\x18\x15 \x01(\x03\x12\x0e\n\x06\x62inary\x18\x16 \x01(\x0c\x12\x13\n\x0b\x62inary_data\x18\x17 \x01(\x0c\x1a\"\n\x12\x44\x65\x63rypted_Payloads\x12\x0c\n\x04type\x18\x01 \x01(\x05b\x06proto3'
)
_builder.BuildMessageAndEnumDescriptors(GARENA420_DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(GARENA420_DESCRIPTOR, 'output_pb2', _globals)
Garena_420 = _sym_db.GetSymbol('Garena_420')

# BioData protobuf
BIODATA_DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\ndata.proto\"\xbb\x01\n\x04\x44\x61ta\x12\x0f\n\x07\x66ield_2\x18\x02 \x01(\x05\x12\x1e\n\x07\x66ield_5\x18\x05 \x01(\x0b\x32\r.EmptyMessage\x12\x1e\n\x07\x66ield_6\x18\x06 \x01(\x0b\x32\r.EmptyMessage\x12\x0f\n\x07\x66ield_8\x18\x08 \x01(\t\x12\x0f\n\x07\x66ield_9\x18\t \x01(\x05\x12\x1f\n\x08\x66ield_11\x18\x0b \x01(\x0b\x32\r.EmptyMessage\x12\x1f\n\x08\x66ield_12\x18\x0c \x01(\x0b\x32\r.EmptyMessage\"\x0e\n\x0c\x45mptyMessageb\x06proto3'
)
_builder.BuildMessageAndEnumDescriptors(BIODATA_DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(BIODATA_DESCRIPTOR, 'data_pb2', _globals)
BioData = _sym_db.GetSymbol('Data')
EmptyMessage = _sym_db.GetSymbol('EmptyMessage')

# ==================== CONSTANTS ====================
MAJOR_LOGIN_URL = "https://loginbp.ggblueshark.com/MajorLogin"
OAUTH_URL = "https://100067.connect.garena.com/oauth/guest/token/grant"
INSPECT_URL = "https://100067.connect.garena.com/oauth/token/inspect"
FREEFIRE_VERSION = "OB54"

UPDATE_URLS = [
    "https://client.ind.freefiremobile.com/UpdateSocialBasicInfo",
    "https://clientbp.ggblueshark.com/UpdateSocialBasicInfo",
    "https://client.us.freefiremobile.com/UpdateSocialBasicInfo",
    "https://clientbp.common.ggbluefox.com/UpdateSocialBasicInfo",
]

KEY = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
IV  = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])

BIO_HEADERS = {
    "Expect": "100-continue",
    "X-Unity-Version": "2018.4.11f1",
    "X-GA": "v1 1",
    "ReleaseVersion": FREEFIRE_VERSION,
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 11; SM-A305F Build/RP1A.200720.012)",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
}

LOGIN_HEADERS = {
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; ASUS_Z01QD Build/PI)",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "Content-Type": "application/octet-stream",
    "Expect": "100-continue",
    "X-Unity-Version": "2018.4.11f1",
    "X-GA": "v1 1",
    "ReleaseVersion": FREEFIRE_VERSION,
}

# ==================== CRYPTO ====================
def encrypt_data(data_bytes):
    cipher = AES.new(KEY, AES.MODE_CBC, IV)
    padded = pad(data_bytes, AES.block_size)
    return cipher.encrypt(padded)

# ==================== JWT HELPERS ====================
def decode_jwt(token):
    try:
        decoded = jwt.decode(token, options={"verify_signature": False})
        return str(decoded.get("account_id")), decoded.get("nickname"), decoded.get("lock_region")
    except:
        return None, None, None

def get_openid_from_inspect(access_token):
    url = f"{INSPECT_URL}?token={access_token}"
    headers = {"User-Agent": "GarenaMSDK/4.0.30", "Accept": "application/json"}
    try:
        resp = requests.get(url, headers=headers, timeout=10, verify=False)
        if resp.status_code == 200:
            data = resp.json()
            return data.get("open_id")
    except:
        pass
    return None

def guest_login(uid, password):
    payload = {
        'uid': uid, 'password': password, 'response_type': "token",
        'client_type': "2", 'client_secret': "2ee44819e9b4598845141067b281621874d0d5d7af9d8f7e00c1e54715b7d1e3",
        'client_id': "100067"
    }
    headers = {'User-Agent': "GarenaMSDK/4.0.19P9(SM-M526B ;Android 13;pt;BR;)"}
    try:
        resp = requests.post(OAUTH_URL, data=payload, headers=headers, timeout=10, verify=False)
        data = resp.json()
        if 'access_token' in data:
            return data['access_token'], data.get('open_id')
    except:
        pass
    return None, None

def major_login(access_token, open_id):
    platforms = [8, 3, 4, 6]
    for pt in platforms:
        try:
            game = GameData()
            game.timestamp = "2024-12-05 18:15:32"
            game.game_name = "free fire"
            game.game_version = 1
            game.version_code = "2.124.1"
            game.os_info = "Android OS 9 / API-28 (PI/rel.cjw.20220518.114133)"
            game.device_type = "Handheld"
            game.network_provider = "Verizon Wireless"
            game.connection_type = "WIFI"
            game.screen_width = 1280
            game.screen_height = 960
            game.dpi = "240"
            game.cpu_info = "ARMv7 VFPv3 NEON VMH | 2400 | 4"
            game.total_ram = 5951
            game.gpu_name = "Adreno (TM) 640"
            game.gpu_version = "OpenGL ES 3.0"
            game.user_id = "Google|74b585a9-0268-4ad3-8f36-ef41d2e53610"
            game.ip_address = "172.190.111.97"
            game.language = "en"
            game.open_id = open_id
            game.access_token = access_token
            game.platform_type = pt
            game.field_99 = str(pt)
            game.field_100 = str(pt)

            ser = game.SerializeToString()
            enc = encrypt_data(ser)
            edata = bytes.fromhex(binascii.hexlify(enc).decode('utf-8'))
            resp = requests.post(MAJOR_LOGIN_URL, data=edata, headers=LOGIN_HEADERS, verify=False, timeout=10)
            if resp.status_code == 200:
                msg = Garena_420()
                msg.ParseFromString(resp.content)
                if msg.token:
                    return msg.token
        except:
            continue
    return None

def update_bio(jwt_token, bio_text):
    """Update bio using JWT. Returns (success, message, endpoint_used)."""
    data = BioData()
    data.field_2 = 17
    data.field_5.CopyFrom(EmptyMessage())
    data.field_6.CopyFrom(EmptyMessage())
    data.field_8 = bio_text
    data.field_9 = 1
    data.field_11.CopyFrom(EmptyMessage())
    data.field_12.CopyFrom(EmptyMessage())
    data_bytes = data.SerializeToString()
    encrypted = encrypt_data(data_bytes)
    headers = BIO_HEADERS.copy()
    headers["Authorization"] = f"Bearer {jwt_token}"

    for url in UPDATE_URLS:
        try:
            resp = requests.post(url, headers=headers, data=encrypted, timeout=15, verify=False)
            if resp.status_code == 200:
                return True, "Bio updated successfully.", url
            else:
                # continue to next endpoint
                continue
        except Exception as e:
            print(f"Endpoint {url} failed: {e}")
            continue
    return False, "All update endpoints failed.", None

# ==================== FLASK ROUTES ====================
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_guest', methods=['POST'])
def generate_guest():
    uid = request.json.get('uid')
    password = request.json.get('password')
    if not uid or not password:
        return jsonify({'error': 'UID and password required'}), 400
    # Step 1: guest login
    acc_token, open_id = guest_login(uid, password)
    if not acc_token:
        return jsonify({'error': 'Guest login failed. Invalid credentials.'}), 400
    # Step 2: major login to get JWT
    jwt_token = major_login(acc_token, open_id)
    if not jwt_token:
        return jsonify({'error': 'Failed to obtain JWT from MajorLogin.'}), 500
    # Decode JWT
    account_id, nickname, region = decode_jwt(jwt_token)
    return jsonify({
        'success': True,
        'jwt': jwt_token,
        'account_id': account_id,
        'nickname': nickname,
        'region': region
    })

@app.route('/generate_token', methods=['POST'])
def generate_token():
    access_token = request.json.get('access_token')
    if not access_token:
        return jsonify({'error': 'Access token required'}), 400

    open_id = get_openid_from_inspect(access_token)
    if not open_id:
        return jsonify({'error': 'Invalid access token or could not fetch open_id.'}), 400
    # Major login
    jwt_token = major_login(access_token, open_id)
    if not jwt_token:
        return jsonify({'error': 'Failed to obtain JWT from MajorLogin.'}), 500
    account_id, nickname, region = decode_jwt(jwt_token)
    return jsonify({
        'success': True,
        'jwt': jwt_token,
        'account_id': account_id,
        'nickname': nickname,
        'region': region
    })

@app.route('/update_bio', methods=['POST'])
def update_bio_route():
    data = request.json
    jwt_token = data.get('jwt')
    bio_text = data.get('bio')
    if not jwt_token or not bio_text:
        return jsonify({'error': 'JWT and bio text required'}), 400
    success, message, endpoint = update_bio(jwt_token, bio_text)
    return jsonify({'success': success, 'message': message, 'endpoint': endpoint})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)