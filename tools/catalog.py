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
DATA = ROOT / "data" / "catalog""""
Bellfre Agent Catalog (BAC)
Research & Discovery Console

Milestone 8.5

Purpose:
    Provides a local interface for viewing and managing
    Bellfre catalog records.

Future:
    - Agent discovery imports
    - Agent Card validation
    - SQL generation
    - BUI assignment
    - BAT generation
"""

import json
import os
from pathlib import Path


# ----------------------------------------------------
# Configuration
# ----------------------------------------------------

VERSION = "0.2"
MILESTONE = "8.5"

ROOT = Path(__file__).resolve().parent.parent

DATA = ROOT / "data" / "catalog"

AGENTS = DATA / "agents.json"
ORGANIZATIONS = DATA / "organizations.json"
PROTOCOLS = DATA / "protocols.json"


# ----------------------------------------------------
# Helpers
# ----------------------------------------------------

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress ENTER to continue...")


def load_json(filename):

    if not filename.exists():
        return []

    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def save_json(filename, data):

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=4,
            ensure_ascii=False
        )


def print_table(title, rows):

    print("=" * 80)
    print(title)
    print("=" * 80)

    if not rows:
        print("No records found.")
        return

    # Flatten simple nested objects
    display_rows = []

    for row in rows:

        flattened = {}

        for key, value in row.items():

            if isinstance(value, dict):
                flattened[key] = ", ".join(
                    f"{k}: {v}"
                    for k, v in value.items()
                )

            elif isinstance(value, list):
                flattened[key] = ", ".join(
                    str(x)
                    for x in value
                )

            else:
                flattened[key] = value

        display_rows.append(flattened)


    headers = list(display_rows[0].keys())

    widths = {}

    for h in headers:
        widths[h] = len(h)

    for row in display_rows:
        for h in headers:
            widths[h] = max(
                widths[h],
                len(str(row[h]))
            )


    header = " | ".join(
        f"{h:<{widths[h]}}"
        for h in headers
    )

    print(header)
    print("-" * len(header))


    for row in display_rows:

        print(
            " | ".join(
                f"{str(row[h]):<{widths[h]}}"
                for h in headers
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
        "Bellfre Agent Catalog",
        load_json(AGENTS)
    )

    pause()


def display_organizations():

    clear()

    print_table(
        "Bellfre Organizations",
        load_json(ORGANIZATIONS)
    )

    pause()


def display_protocols():

    clear()

    print_table(
        "Bellfre Protocols",
        load_json(PROTOCOLS)
    )

    pause()


def display_all():

    clear()

    print_table(
        "AGENTS",
        load_json(AGENTS)
    )

    print()

    print_table(
        "ORGANIZATIONS",
        load_json(ORGANIZATIONS)
    )

    print()

    print_table(
        "PROTOCOLS",
        load_json(PROTOCOLS)
    )

    pause()


def statistics():

    clear()

    print("=" * 80)
    print("Bellfre Catalog Statistics")
    print("=" * 80)

    print(
        f"Agents        : {len(load_json(AGENTS))}"
    )

    print(
        f"Organizations : {len(load_json(ORGANIZATIONS))}"
    )

    print(
        f"Protocols     : {len(load_json(PROTOCOLS))}"
    )

    pause()


# ----------------------------------------------------
# Future Functions
# ----------------------------------------------------

def import_record():

    clear()

    print("=" * 80)
    print("Import Catalog Record")
    print("=" * 80)

    print("""
Future workflow:

1. Receive agent metadata
2. Validate structure
3. Assign catalog ID
4. Add source information
5. Save JSON record

Possible inputs:
- Agent Card URL
- Repository
- API response
- Manual entry
- Discovery crawler
""")

    pause()



def generate_sql():

    clear()

    print("=" * 80)
    print("SQL Generator")
    print("=" * 80)

    print("""
Future workflow:

JSON Catalog
      |
      v
Catalog Parser
      |
      v
Clearinghouse SQL Tables


Will generate:
- organizations table
- agents table
- protocols table
- relationships
- verification records
""")

    pause()


# ----------------------------------------------------
# Header / Menu
# ----------------------------------------------------

def header():

    print("=" * 80)
    print(" Bellfre")
    print(" Agent Catalog (BAC)")
    print(" Research & Discovery Console")
    print("-" * 80)
    print(f" Version   : {VERSION}")
    print(f" Milestone : {MILESTONE}")
    print(f" Data      : {DATA}")
    print("=" * 80)
    print()



def menu():

    while True:

        clear()

        header()

        print("1) Display Agents")
        print("2) Display Organizations")
        print("3) Display Protocols")
        print()
        print("4) Display Everything")
        print()
        print("5) Catalog Statistics")
        print()
        print("6) Import Catalog Record")
        print("7) Generate SQL (Future)")
        print()
        print("X) Exit")
        print()

        choice = input("Selection > ").strip().upper()


        if choice == "1":
            display_agents()

        elif choice == "2":
            display_organizations()

        elif choice == "3":
            display_protocols()

        elif choice == "4":
            display_all()

        elif choice == "5":
            statistics()

        elif choice == "6":
            import_record()

        elif choice == "7":
            generate_sql()

        elif choice == "X":
            break

        else:
            print("Invalid selection.")
            pause()



if __name__ == "__main__":
    menu()

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