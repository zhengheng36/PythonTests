## ref: https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431937554888869fb52b812243dda6103214cd61d0c2000


## created datetime
from datetime import datetime
# KEY: different from: 'import datetime'
now = datetime.now()
print('Now is:', now)
print('typeof(now) is:', type(now), '\n')

speicifyTime = datetime(2020, 8, 8, 20, 8)
print('specifiyTime: ', speicifyTime)
## change to timestamp(float)
print('specifyTime.timestamp():', speicifyTime.timestamp(), '\n')

## timestamp to datetime
print('speicifyTime.timestamp to datetime:', datetime.fromtimestamp(speicifyTime.timestamp()), '\n')

## str to datetime
TimeFromStr = datetime.strptime('2020-8-8 20:22:22', '%Y-%m-%d %H:%M:%S')
print('TimeFromStr is:', TimeFromStr, '\n')

## datetime to str
print('print now to string:', now.strftime('%a, %b(%m) %d %Y, %H:%M'), '\n')

## datetime in/decrease
from datetime import datetime, timedelta
NextDayFromNow = now + timedelta(days = 1)
print('NextDayFromNow is:', NextDayFromNow)
OneHourBeforeNow = now - timedelta(hours = 1)
print('OneHourBeforeNow:', OneHourBeforeNow, '\n')

## datetime to UTC
from datetime import datetime, timedelta, timezone

utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)