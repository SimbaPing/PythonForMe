import time

ticks = time.time()
print("当前时间：", ticks)

localtime = time.localtime(time.time())
print("本地时间：", localtime)

local_time = time.asctime(time.localtime(time.time()))
print("正确显示：", local_time)

# 格式化日期
print(time.strftime("%Y-%m-%d %H:%M:%S"))  # 喜欢这个样式
print(time.strftime("%a %b %d %H:%M:%S %Y"))

# 将时间变为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))
