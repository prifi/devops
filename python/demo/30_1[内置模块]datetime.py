#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@version:
author:fly
@time: 2021/03/09
@file: 30_1[内置模块]datetime.py
@function:
@modify:
"""
### datetime

# 处理日期和时间的标准库
from datetime import datetime

# 获取当前时间（注意是时间类类型）
now = datetime.now()
print(now, type(now))  # 2021-03-09 02:59:58.106648 <class 'datetime.datetime'>

# 格式化输出时间（注意是str类型）
df = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(df, type(df))  # 2021-03-09 03:10:54 <class 'str'>
# str转换为datetime
cday = datetime.strptime(df, '%Y-%m-%d %H:%M:%S')  # 注意是striptime
print(cday, type(cday))

# 获取指定日期和时间
dt = datetime(2015, 4, 19, 12, 20)  # 使用指定日期创建datetime
print(dt)  # 2015-04-19 12:20:00

# datetime转换为timestamp
dtm = dt.timestamp()
print(dtm, type(dtm))  # 1429446000.0 <class 'float'>

# timestamp转为datetime
t = 1429417200.0
print(datetime.fromtimestamp(t))  # 2015-04-19 04:20:00
datetime.utcfromtimestamp(t)  # 转换成UTC时间

# datetime 加减
# 加减可以直接用+和-运算符，把datetime往后或往前计算，得到新的datetime（需要导入timedelta类）
from datetime import datetime, timedelta

now_1 = datetime.now()
print(now_1)
old_time = now_1 - timedelta(minutes=5)
# oldtime = now1 + timedelta(days=2, hours=12)  # 使用timedelta你可以很容易地算出前几天和后几天的时刻。
print(old_time)
# 结果：
# 2021-03-09 03:42:23.071090
# 2021-03-09 03:37:23.071090


# 本地时间转换为UTC时间
# 一个datetime类型有一个时区属性tzinfo，但是默认为None，给datetime加上时区：
from datetime import datetime, timedelta, timezone

tz_utc_8 = timezone(timedelta(hours=8))
now_2 = datetime.now()
print(now_2)
print(now_2.replace(tzinfo=tz_utc_8))
# 结果：
# 2021-03-09 03:50:10.938045
# 2021-03-09 03:50:10.938045+08:00


# 时区转换 UTC时间转换为北京时间 +8:00
# 利用 **带时区** 的datetime，通过astimezone()方法，可以转换到任意时区。
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))  # 转换为北京时间
print(utc_dt, bj_dt)
# 2021-03-09 03:53:01.377522+00:00 2021-03-09 11:53:01.377522+08:00


## 练习：获取了用户输入的日期和时间如2015-1-21 9:01:30，以及一个时区信息如UTC+5:00，均是str，请编写一个函数将其转换为timestamp：
import re
from datetime import datetime, timedelta, timezone


def to_timestamp(dt_str, tz_str):
    try:
        t1 = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    except Exception as e:
        print('time eror')
        raise
    re_time = re.compile(r'.*?([\+\-\d]+).*')
    if not re_time.match(tz_str):
        return
    zone = int(re_time.match(tz_str).group(1))
    t = t1.replace(tzinfo=timezone(timedelta(hours=zone))).timestamp()
    return t
    # 方法2：一行代码搞定
    # return datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S').replace(
    #     tzinfo=timezone(timedelta(hours=int(re.match(r'.*?([\+\-\d]+).*', tz_str).group(1))))).timestamp()


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')
