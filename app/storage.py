import os
import json

DATA_DIR = "data"
VAULT_FILE = os.path.join(DATA_DIR, "vault.json")
META_FILE = "data/meta.json"

def ensure_data_dir():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def load_vault(fernet):
    ensure_data_dir()
    if not os.path.exists(VAULT_FILE):
        return {}

    with open(VAULT_FILE, "rb") as f:
        encrypted = f.read()
        if not encrypted:
            return {}

        try:
            decrypted = fernet.decrypt(encrypted)
            return json.loads(decrypted)
        except Exception:
            print("❌ Wrong master password or corrupted vault.")
            exit()

def save_vault(data, fernet):
    ensure_data_dir()
    encrypted = fernet.encrypt(json.dumps(data).encode())
    with open(VAULT_FILE, "wb") as f:
        f.write(encrypted)
def save_meta(data):
    os.makedirs("data", exist_ok=True)
    with open(META_FILE, "w") as f:
        json.dump(data, f)

def load_meta():
    if not os.path.exists(META_FILE):
        return {}
    with open(META_FILE, "r") as f:
        return json.load(f)