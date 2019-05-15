import os

# print(os.getcwd())

# print(os.listdir())

# for dirpath, dirname, filenames in os.walk(os.getcwd()):
#     print(dirpath)
#     print(dirname)
#     print(filenames)
#     print()

# print(os.environ.get("HOME"))
# file_path = os.path.join(os.environ.get("HOME"), "test.txt")
# print(file_path)

# os.path.exists('/tmp/ss.txt')


import datetime
import pytz

# d = datetime.date(2019, 5, 15)
# print(d)
# d = datetime.date.today()
# print(d)
# print(d.weekday())
# print(d.isoweekday())
# tdelta = datetime.timedelta(days=9)
# print(d + tdelta)

# t = datetime.time(15, 30, 33, 10000)
# print(t)

# dt_today = datetime.datetime.today()
# dt_now = datetime.datetime.now()
# dt_utcnow = datetime.datetime.utcnow()

# print(dt_today)
# print(dt_now)
# print(dt_utcnow)

# dt = datetime.datetime(2019, 5, 15, 15, 58, 32, tzinfo=pytz.UTC)
# print(dt)

# dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)

# dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# print(dt_utcnow)

# dt_beijing = dt_utcnow.astimezone(pytz.timezone("Hongkong"))
# dt_beijing = dt_utcnow.astimezone(pytz.timezone("Asia/Shanghai"))
# print(dt_beijing)

dt_beijing = datetime.datetime.now(tz=pytz.timezone("Hongkong"))
print(dt_beijing.strftime("%B %d, %Y"))

dt_str = "May 15, 2019"
dt = datetime.datetime.strptime(dt_str, "%B %d, %Y")
print(dt)
