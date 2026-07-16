"""
Bellfre Agent catalog (BAC)
Research & Discovery Console

Milestone 8.5
Version 0.1
"""

import csv
import os
from pathlib import Path

# ----------------------------------------------------
# Configuration
# ----------------------------------------------------

VERSION = "0.1"
MILESTONE = "8.5"

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "catalog"

AGENTS = DATA / "agents.csv"
ORGANIZATIONS = DATA / "organizations.csv"
PROTOCOLS = DATA / "protocols.csv"


# ----------------------------------------------------
# Helpers
# ----------------------------------------------------

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress ENTER to continue...")


def load_csv(filename):
    if not filename.exists():
        return []

    with open(filename, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def print_table(title, rows):

    print("=" * 72)
    print(title)
    print("=" * 72)

    if not rows:
        print("No records found.")
        return

    headers = list(rows[0].keys())

    widths = {}

    for h in headers:
        widths[h] = len(h)

    for row in rows:
        for h in headers:
            widths[h] = max(widths[h], len(str(row[h])))

    header = " | ".join(f"{h:<{widths[h]}}" for h in headers)
    print(header)
    print("-" * len(header))

    for row in rows:
        print(
            " | ".join(
                f"{str(row[h]):<{widths[h]}}" for h in headers
            )
        )

    print("-" * len(header))
    print(f"{len(rows)} record(s)")


# ----------------------------------------------------
# Displays
# ----------------------------------------------------

def display_agents():
    clear()
    print_table(
        "Bellfre Agent catalog",
        load_csv(AGENTS),
    )
    pause()


def display_organizations():
    clear()
    print_table(
        "Bellfre Organizations",
        load_csv(ORGANIZATIONS),
    )
    pause()


def display_protocols():
    clear()
    print_table(
        "Bellfre Protocols",
        load_csv(PROTOCOLS),
    )
    pause()


def display_everything():

    clear()

    print_table(
        "Bellfre Agent catalog",
        load_csv(AGENTS),
    )

    print()

    print_table(
        "Bellfre Organizations",
        load_csv(ORGANIZATIONS),
    )

    print()

    print_table(
        "Bellfre Protocols",
        load_csv(PROTOCOLS),
    )

    pause()


def display_stats():

    clear()

    agents = load_csv(AGENTS)
    orgs = load_csv(ORGANIZATIONS)
    prots = load_csv(PROTOCOLS)

    print("=" * 72)
    print("Bellfre catalog Statistics")
    print("=" * 72)

    print(f"Agents        : {len(agents)}")
    print(f"Organizations : {len(orgs)}")
    print(f"Protocols     : {len(prots)}")

    pause()


# ----------------------------------------------------
# Menu
# ----------------------------------------------------

def header():

    agents = len(load_csv(AGENTS))
    orgs = len(load_csv(ORGANIZATIONS))
    prots = len(load_csv(PROTOCOLS))

    print("=" * 72)
    print(" Bellfre")
    print(" Agent catalog (BAC)")
    print(" Research & Discovery Console")
    print("-" * 72)
    print(f" Version   : {VERSION}")
    print(f" Milestone : {MILESTONE}")
    print(f" Data      : {DATA}")
    print("-" * 72)
    print(f" Agents        : {agents}")
    print(f" Organizations : {orgs}")
    print(f" Protocols     : {prots}")
    print("=" * 72)
    print()


def menu():

    while True:

        clear()

        header()

        print(" 1) Display Agents")
        print(" 2) Display Organizations")
        print(" 3) Display Protocols")
        print()
        print(" 4) Display Everything")
        print()
        print(" 5) catalog Statistics")
        print()
        print(" 6) Verify Agent Cards      (Milestone 9)")
        print(" 7) Import Agents           (Future)")
        print(" 8) Export Data             (Future)")
        print()
        print(" 9) Reload Data")
        print(" X) Exit")
        print()

        choice = input("Selection > ").strip().upper()

        if choice == "1":
            display_agents()

        elif choice == "2":
            display_organizations()

        elif choice == "3":
            display_protocols()

        elif choice == "4":
            display_everything()

        elif choice == "5":
            display_stats()

        elif choice == "6":
            print("\nComing in Milestone 9.")
            pause()

        elif choice == "7":
            print("\nFuture feature.")
            pause()

        elif choice == "8":
            print("\nFuture feature.")
            pause()

        elif choice == "9":
            print("\nData reloaded.")
            pause()

        elif choice == "X":
            break

        else:
            print("\nInvalid selection.")
            pause()


# ----------------------------------------------------
# Main
# ----------------------------------------------------

if __name__ == "__main__":
    menu()