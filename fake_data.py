from sqlite3.dbapi2 import Connection
from faker import Faker
from tqdm import tqdm

import sqlite3


fake = Faker()
Faker.seed(0)

connection = sqlite3.connect("db.sqlite3")
cursor = connection.cursor()

# Create tables
cursor.execute(
    """CREATE TABLE IF NOT EXISTS hosts
               (host_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, name TEXT, domain TEXT, ip_address TEXT, mac_address TEXT, created_at TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime')))"""
)

cursor.execute(
    """CREATE TABLE IF NOT EXISTS people
               (person_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, first_name TEXT, last_name TEXT, email TEXT, address TEXT, job TEXT, created_at TEXT NOT NULL DEFAULT (DATETIME('now', 'localtime')))"""
)


# Create hosts
sql = "INSERT INTO hosts(name, domain, ip_address, mac_address) VALUES (?, ?, ?, ?)"
for _ in tqdm(range(10_000)):
    cursor.execute(
        sql, (fake.hostname(0), fake.domain_name(2), fake.ipv4(), fake.mac_address())
    )
# Save (commit) the changes
connection.commit()

# create people
sql = (
    "INSERT INTO people(first_name, last_name, email, address, job) VALUES (?,?,?,?,?)"
)
for _ in tqdm(range(10_000)):
    cursor.execute(
        sql,
        (
            fake.first_name(),
            fake.last_name(),
            fake.ascii_email(),
            fake.address(),
            fake.job(),
        ),
    )
# Save (commit) the changes
connection.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
connection.close()
