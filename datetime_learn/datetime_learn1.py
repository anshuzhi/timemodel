# -*-encoding:utf-8 -*-
#作者：石振安
#日期：2021/2/18 19:39

import time
import datetime

print(datetime.date.today())
print(datetime.date(2021,1,25))
print(datetime.date.fromtimestamp(time.time()))#通过时间戳生成日期

d=datetime.date.today()
# datetime.date->结构化时间对象
print(d.timetuple())
print(d.replace(2021))
print(d.replace(d.year,8))
print(d.replace(year=2022))
print(d.replace(month=8))
print(d.replace(day=8))
print(d.toordinal())#从0001-01-01到现在的天数
print(d.weekday())#0代表周一，6代表周日
print(d.isoweekday())#1代表周一,0代表周日

# 自定义输出格式
print(d.strftime("%Y-%m-%d"))


print(f"{'datetime':=^50s}")#居中填充
print(f"{'datetime':=<50s}")#右填充
print(f"{'datetime':=>50s}")#左填充

dt=datetime.datetime.now()
print(dt)
# datetime转结构化时间对象
print(dt.timetuple())
# datetime转时间戳
print(dt.timestamp())
# datetime转时间字符串
print(dt.strftime("%Y-%m-%d %H:%M:%S"))
# 时间戳转datetime
print(datetime.datetime.fromtimestamp(time.time()))#通过时间戳生成日期
# 时间字符串转datetime
print(datetime.datetime.strptime('2021-02-18 20:16:40',"%Y-%m-%d %H:%M:%S"))
# 结构化对象转datetime
print(datetime.datetime.fromtimestamp(time.mktime(time.localtime())))


# 日期计算：datetime.timedelta
#生成时间差
# td=datetime.timedelta(days,seconds,mic,mll,huors,weeks)
td=datetime.timedelta(days=10)
print(td)
# 计算目标时间
dt=datetime.datetime.now()
delta1=datetime.timedelta(days=10)
delta2=datetime.timedelta(weeks=1)
target1=dt+delta1
target2=dt+delta2
print(target1.strftime('%Y/%m/%d %H:%M:%S'))
print(target2.strftime('%Y/%m/%d %H:%M:%S'))


# 计算时间差
dt1=datetime.datetime.today()
dt2=datetime.datetime.utcnow()
print(dt1-dt2)


# 这是我新增的