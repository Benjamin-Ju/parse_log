import psycopg2
import psycopg2.extras
import datetime as dt
import pandas as pd

expense_log = {
    
}

if __name__ == '__main__':
    conn = psycopg2.connect(host="localhost", database="benjamin-ju", user="postgres", password="chicken!1")

    cur = conn.cursor()

    basic_query = "INSERT INTO expenses (date, expense, value, category) VALUES "

    for date in expense_log:
        for entry in expense_log[date]:
            loc = entry.find('-')
            value = entry[1:loc]
            activity = entry[loc+2:]
            if 'Groceries' in activity or 'Protein Powder' in activity:
                category = 'groceries'
            elif 'Gym' in activity:
                category = 'gym'
            elif 'Bus' in activity:
                category = 'transit'
            elif 'Lunch' in activity or 'MeetFresh' in activity or 'Lazeez' in activity or 'iPotato' in activity or 'Tim Horton' in activity or 'DQ' in activity or 'Milkshake' in activity or 'Dinner' in activity:
                category = 'eating out'
            else:
                category = 'other'
            new_entry = "('" + date + "', '" + activity + "', '" + value + "', '" + category + "'), "
            basic_query += new_entry
            pass
    cur.execute(basic_query[:-2])
    conn.commit()

print "test"
