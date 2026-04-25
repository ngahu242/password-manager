import argparse
from getpass import getpass
from app.crypto import generate_key
from app.manager import add_entry, get_entry, list_entries, delete_entry
from app.utils import generate_password

def run():
    parser = argparse.ArgumentParser(description="🔐 Password Manager")
    subparsers = parser.add_subparsers(dest="command")

    add = subparsers.add_parser("add")
    add.add_argument("site")
    add.add_argument("username")
    add.add_argument("--generate", action="store_true")

    get = subparsers.add_parser("get")
    get.add_argument("site")

    delete = subparsers.add_parser("delete")
    delete.add_argument("site")

    subparsers.add_parser("list")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    master = getpass("Master password: ")
    fernet = generate_key(master)

    if args.command == "add":
        password = generate_password() if args.generate else getpass("Password: ")
        add_entry(fernet, args.site, args.username, password)

    elif args.command == "get":
        get_entry(fernet, args.site)

    elif args.command == "list":
        list_entries(fernet)

    elif args.command == "delete":
        delete_entry(fernet, args.site)