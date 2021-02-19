import time
# 时间戳
print(time.time())

# 结构化时间对象
# localtime(时间戳)
st=time.localtime()
print(st)
# st本质上是一个元组，所以，如下：
print('今天是{}-{}-{}'.format(st[0],st[1],st[2]))
print('今天是{}-{:02d}-{}'.format(st[0],st[1],st[2]))#2位数，不足两位的左填充0
print('今天是{}-{:.2f}-{}'.format(st[0],st[1],st[2]))#保留小数点两位
print('今天是星期{}'.format(st.tm_wday+1))


# 格式化的时间字符串：Thu Feb 18 18:31:49 2021
print(time.ctime())

# strftime(时间格式，结构化时间对象)"%Y-%m-%d %H:%M:%S"
print(time.strftime("%Y-%m-%d %H:%M:%S"))
print(time.strftime("%Y-%m-%d %H:%M:%S"))
print(time.strftime("%Y-%m-%d %H:%M:%S %a"))#星期缩写
print(time.strftime("%Y-%m-%d %H:%M:%S %A"))#星期全拼
print(time.strftime("%Y-%m-%d %H:%M:%S %b"))#月份缩写
print(time.strftime("%Y-%m-%d %H:%M:%S %B"))#月份全拼
print(time.strftime("%Y-%m-%d %H:%M:%S %w"))#在当前星期是第几天
print(time.strftime("%Y-%m-%d %H:%M:%S %W"))#今天所在的周是整年的第几周
print(time.strftime("%Y-%m-%d %I:%M:%S %p"))#%I十二小时制


# 三种时间格式之间的转换
# 时间戳-》结构化对象
# UTC时间
print(time.gmtime())#gmtime()默认的参数是time.time()  当前的时间戳
print(time.gmtime(3600))
# 北京时间
print(time.localtime(3600))

# 结构化时间对象->时间戳
# mktime(结构化对象)
print(time.mktime(time.localtime()))
print(time.time())
# 结构化时间对象->时间字符串
# strftime(format,结构化时间对象)
print(time.strftime("%Y-%m-%d %H:%M:%S ",time.localtime()))
print(time.strftime("%Y-%m-%d %H:%M:%S ",time.localtime(3600)))
print(time.strftime("%Y-%m-%d %H:%M:%S ",time.gmtime()))
print(time.strftime("%Y-%m-%d %H:%M:%S ",time.gmtime(3600)))

#时间字符串->结构化时间对象
# strptime(str,format)
strtime='2021-2-18 19:05:28'
print(time.strptime(strtime,"%Y-%m-%d %H:%M:%S"))
# 更改
# 更改
# 更改