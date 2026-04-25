from getpass import getpass

from app.crypto import generate_key, generate_recovery_key
from app.manager import add_entry, get_entry, list_entries, delete_entry
from app.utils import generate_password
from app.storage import load_meta, save_meta

def run_ui():
    print("\n🔐 PASSWORD MANAGER")

    # ✅ 1. RUN FIRST-TIME SETUP HERE (IMPORTANT)
    meta = load_meta()

    if not meta.get("setup_done"):
        print("\n🔐 FIRST TIME SETUP")

        hint = input("Set password hint: ")
        recovery_key = generate_recovery_key()

        print("\n⚠️ IMPORTANT: SAVE THIS RECOVERY KEY")
        print(recovery_key)
        print("If you lose your master password, this is your only recovery option.\n")

        meta = {
            "setup_done": True,
            "hint": hint,
            "recovery_key": recovery_key
        }

        save_meta(meta)

    # ✅ 2. THEN ASK MASTER PASSWORD
    master = getpass("Enter master password: ")
    fernet = generate_key(master)

    # ✅ 3. THEN START MENU LOOP
    while True:
        print("\n📌 MENU")
        print("1. Add password")
        print("2. Get password")
        print("3. List sites")
        print("4. Delete password")
        print("5. Generate password")
        print("6. Exit")
        print("7. Forgot master password")  # ✅ ADD THIS LINE

        choice = input("Select option: ")

        if choice == "1":
            add_entry(...)

        elif choice == "2":
            get_entry(...)

        elif choice == "3":
            list_entries(...)

        elif choice == "4":
            delete_entry(...)

        elif choice == "5":
            print(generate_password())

        elif choice == "6":
            print("👋 Goodbye!")
            break

        # 🔐 HERE IS WHERE YOU ADD IT
        elif choice == "7":
            meta = load_meta()

            print("\n🔐 RECOVERY MODE")
            print("Hint:", meta.get("hint", "No hint set"))

            key = input("Enter recovery key: ")

            if key == meta.get("recovery_key"):
                print("\n⚠️ VERIFIED")
                print("You must reset the vault (old data will be lost).")

                confirm = input("Reset vault? (yes/no): ")

                if confirm == "yes":
                    open("data/vault.json", "w").write("")
                    print("✅ Vault reset complete. Set new master password on restart.")
            else:
                print("❌ Invalid recovery key")

        else:
            print("❌ Invalid option")