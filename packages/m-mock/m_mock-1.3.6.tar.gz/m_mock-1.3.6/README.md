# install
pip install m-mock

# mock

一个仿照mock.js生成随机数据的工具包

## Basic

### character 字符

```python
m_mock.mock("@character()"):X
m_mock.mock("@character('lower')"):f
m_mock.mock("@character('upper')"):E
m_mock.mock("@character('number')"):4
m_mock.mock("@character('symbol')"):)
m_mock.mock("@character('aeiou')"):o
```

### integer 整数

```python
m_mock.mock("@integer(2,4)"):3
m_mock.mock("@integer(3)"):4941869747671297
m_mock.mock("@integer()"):-3191979912544874
```

### boolean 布尔值

```python
m_mock.mock("@boolean(2,4)"):False
m_mock.mock("@boolean(3)"):True
m_mock.mock("@boolean()"):False
```

### float 浮点数

```python
m_mock.mock("@float(2,4)"):2.937
m_mock.mock("@float(3)"):229342892631770.44
m_mock.mock("@float()"):872256.00439
```

### string 字符串

```python
m_mock.mock('@string(2)'):W3
m_mock.mock('@string('lower', 3)'):icz
m_mock.mock('@string('upper', 3)'):NBE
m_mock.mock('@string('number', 3)'):108
m_mock.mock('@string('symbol', 3)'):!%=
m_mock.mock('@string('aeiou', 3)'):eia
m_mock.mock('@string('lower', 1, 3)'):fih
m_mock.mock('@string('upper', 1, 3)'):F
m_mock.mock('@string('number', 1, 3)'):102
m_mock.mock('@string('symbol', 1, 3)'):`
m_mock.mock('@string('aeiou', 1, 3)'):aao
m_mock.mock('@string('chinese', 1, 3)'):捎创
m_mock.mock('@string('cn_symbol', 1, 3)'):～
m_mock.mock('@string('cn_string', 3, 9)'):〉·，（鉴或【落【
m_mock.mock('@string('cn_string', 1)'):侄
m_mock.mock('@string('abcd', 2)'):bd
```

## name 中英文姓名

```python
m_mock.mock("@clast()"):折
m_mock.mock("@cfirst()"):丰
m_mock.mock("@cname()"):梁恒蹄
m_mock.mock("@cname(3)"):臧倡荷
m_mock.mock("@last()"):Smith
m_mock.mock("@first()"):Kennet
m_mock.mock("@name()"):Jessica Jackson
m_mock.mock("@name(True)"):Melissa Mark Davis
```

## date 日期

```python
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称

# date
m_mock.mock("@date('%Y-%m-%d %H:%M:%S', '+1d')"):2023-02-21 13:50:02
m_mock.mock("@date('%Y-%m-%d %H:%M:%S', '+24h')"):2023-02-21 13:50:02
m_mock.mock("@date('%Y年-%m月-%d日 %H时:%M分:%S秒', '+2mon')"):2023年-04月-20日 13时:50分:02秒
m_mock.mock("@date('%Y年-%m月-%d日 %H时:%M分:%S秒', '+2min')"):2023年-02月-20日 13时:52分:02秒
# time
m_mock.mock("@time('', '+4sec')"):15:51:46
m_mock.mock("@time"):15:51:42
# 毫秒级时间戳
m_mock.mock('@timestamp'):1715681195311
# now
m_mock.mock("@now('year')"):2023-01-01 00:00:00
m_mock.mock("@now('month')"):2023-02-01 00:00:00
m_mock.mock("@now('week')"):2023-02-26 00:00:00
m_mock.mock("@now('day')"):2023-02-20 00:00:00
m_mock.mock("@now('hour')"):2023-02-20 13:00:00
m_mock.mock("@now('minute')"):2023-02-20 13:42:00
m_mock.mock("@now('second')"):2023-02-20 13:42:44
m_mock.mock("@now()"):2023-02-20 13:42:44
m_mock.mock("@now('year','%Y年-%m月-%d日 %H:%M:%S')"):2023年-01月-01日 00:00:00
m_mock.mock("@now('week','%Y年 %m月 %d日 %H:%M:%S')"):2023年 02月 26日 00:00:00
```

# miscellaneous 杂项
```python
m_mock.mock('@id()'):397425198210051092
m_mock.mock('@increment()'):1
m_mock.mock('@increment(100)'):101
m_mock.mock('@uuid()'):"4f35a282-73d0-4705-9fd5-ddf722e78eea"
```