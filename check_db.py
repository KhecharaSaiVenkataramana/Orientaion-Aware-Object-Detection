import pymysql

DB_CONFIG = {
    "host":     "bg0mwot4am56wljm4ims-mysql.services.clever-cloud.com",
    "port":     3306,
    "user":     "uky8zedsjiowpw7m",
    "password": "wjLZKLUHi5GseDFcv7mL",
    "database": "bg0mwot4am56wljm4ims",
    "connect_timeout": 10,
    "cursorclass": pymysql.cursors.DictCursor
}

conn = pymysql.connect(**DB_CONFIG)
try:
    with conn.cursor() as cur:
        # Show all tables
        cur.execute("SHOW TABLES")
        tables = cur.fetchall()
        print("=== TABLES IN CLOUD DB ===")
        for t in tables:
            print(" ", list(t.values())[0])

        # Show users table structure
        cur.execute("DESCRIBE users")
        cols = cur.fetchall()
        print("\n=== USERS TABLE COLUMNS ===")
        for c in cols:
            print(f"  {c['Field']:20} {c['Type']}")

        # Show registered users (no passwords)
        cur.execute("SELECT id, username, email, joined_at FROM users")
        users = cur.fetchall()
        print(f"\n=== REGISTERED USERS ({len(users)}) ===")
        for u in users:
            print(f"  [{u['id']}] {u['username']} | {u['email']} | joined {u['joined_at']}")

finally:
    conn.close()