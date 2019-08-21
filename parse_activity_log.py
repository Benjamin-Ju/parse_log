import psycopg2
import psycopg2.extras
import datetime as dt
import pandas as pd

activity_log = {

}

if __name__ == '__main__':
    conn = psycopg2.connect(host="localhost", database="benjamin-ju", user="postgres", password="chicken!1")

    cur = conn.cursor()

    basic_query = "INSERT INTO activity_log (date, start_time, end_time, length, activity, category) VALUES "

    for date in activity_log:
        for entry in activity_log[date]:
            if 'WASTE DAY' in entry:
                continue
            length = (dt.datetime.strptime(entry[10:17], "%I:%M%p") - dt.datetime.strptime(entry[:7], "%I:%M%p")).seconds/60
            if (dt.datetime.strptime(entry[10:17], "%I:%M%p") < dt.datetime.strptime(entry[:7], "%I:%M%p")):
                length = 0
            activity = entry[18:]
            if 'Social' in activity or 'with' in activity or 'Call Home' in activity:
                category = 'social'
            elif 'Transit' in activity or 'Bike' in activity or 'Groceries' in activity:
                category = 'transit'
            elif 'Leisure' in activity:
                category = 'leisure'
            elif 'Cook' in activity or 'Eat' in activity or 'Dishes' in activity:
                category = 'kitchen'
            elif 'Chores' in activity or 'Laundry' in activity or 'Misc' in activity:
                category = 'misc'
            elif 'Reading' in activity:
                category = 'read'
            elif 'Gym' in activity:
                category = 'gym'
            elif 'Shower' in activity:
                category = 'washroom'
            elif 'Work' in activity:
                category = 'job'
            elif 'Grind' in activity:
                category = 'grind'
            elif 'Meditation' in activity:
                category = 'meditation'
            elif 'Nap' in activity:
                category = 'sleep'
            else:
                category = 'not recorded'
            new_entry = "('" + date + "', '" + entry[:7] + "', '" + entry[10:17] + "', " \
                        + str(length) + ", '" + activity + "', '" + category + "'), "
            if (dt.datetime.strptime(entry[10:17], "%I:%M%p") < dt.datetime.strptime(entry[:7], "%I:%M%p")):
                print "Change length for the following: "
                print new_entry
            basic_query += new_entry
            pass
    cur.execute(basic_query[:-2])
    conn.commit()


print "test"
