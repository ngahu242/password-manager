from app.storage import load_vault, save_vault

def add_entry(fernet, site, username, password):
    vault = load_vault(fernet)
    vault[site] = {"username": username, "password": password}
    save_vault(vault, fernet)
    print("✅ Entry added.")

def get_entry(fernet, site):
    vault = load_vault(fernet)
    if site in vault:
        print(f"Username: {vault[site]['username']}")
        print(f"Password: {vault[site]['password']}")
    else:
        print("❌ Entry not found.")

def list_entries(fernet):
    vault = load_vault(fernet)
    if not vault:
        print("No entries found.")
    else:
        for site in vault:
            print(f"- {site}")

def delete_entry(fernet, site):
    vault = load_vault(fernet)
    if site in vault:
        del vault[site]
        save_vault(vault, fernet)
        print("🗑️ Entry deleted.")
    else:
        print("❌ Entry not found.")