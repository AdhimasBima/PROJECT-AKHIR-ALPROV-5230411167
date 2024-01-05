import sqlite3
koneksi = sqlite3.connect('database_fauna.db')

kursor = koneksi.cursor()

kursor.execute("SELECT SUM(jml_skrng) FROM FAUNA")

jml_total = kursor.fetchone()[0]

print(f"Total populasi = {jml_total}")

koneksi.close()