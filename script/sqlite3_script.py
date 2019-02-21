import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect("/Users/ustc-weihua/frontend.db")
    c = conn.cursor()
    for row in c.execute("select service_loc, group_concat(source_uuid) as source_uuid_list from ds_sqlcontentsource group by service_loc"):
        print(row[0])
        print(type(row[1]))
        print(row[1].split(','))
    conn.close()
