# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 16:39:00 2022

@author: xuewu
"""


# 4.1.1.2 Generators and closures

class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("__iter__")
        return self

    def __next__(self):
        print("__next__")				
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


for i in Fib(10):
    print(i)


# 4.1.1.3 Generators and closures
class Fib:
    def __init__(self, nn):
        self.__n = nn
        self.__i = 0
        self.__p1 = self.__p2 = 1

    def __iter__(self):
        print("Fib iter")
        return self

    def __next__(self):
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret

class Class:
    def __init__(self, n):
        self.__iter = Fib(n)

    def __iter__(self):
        print("Class iter")
        return self.__iter;
object = Class(8)
for i in object:
    print(i)

# 4.1.1.4 Generators and closures

def fun(n):
    for i in range(n):
        yield i

for v in fun(5):
    print(v)

# 4.1.1.5 Generators and closures
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2


for v in powers_of_2(8):
    print(v)

#----------
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
t = [x for x in powers_of_2(5)]
print(t)

#------
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2

t = list(powers_of_2(3))
print(t)

#----
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2

for i in range(20):
    if i in powers_of_2(4):
        print(i)

#----------
def fibonacci(n):
    p = pp = 1
    for i in range(n):
        if i in [0, 1]:
            yield 1
        else:
            n = p + pp
            pp, p = p, n
            yield n

fibs = list(fibonacci(10))
print(fibs)


# 4.1.1.7 Generators and closures

the_list = []

for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0)

print(the_list)

# 4.1.1.8 Generators and closures

the_list = [1 if x % 2 == 0 else 0 for x in range(10)]

print(the_list)

# ---
the_list = [1 if x % 2 == 0 else 0 for x in range(10)]
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))

for v in the_list:
    print(v, end=" ")
print()

for v in the_generator:
    print(v, end=" ")
print()

len(the_list)
len(the_generator)


for v in [1 if x % 2 == 0 else 0 for x in range(10)]:
    print(v, end=" ")
print()

for v in (1 if x % 2 == 0 else 0 for x in range(10)):
    print(v, end=" ")
print()

# 4.1.1.9 Generators and closures
two = lambda: 3
sqr = lambda x: x * x
pwr = lambda x, y: x ** y

for a in range(-2, 3):
    print(sqr(a), end=" ")
    print(pwr(a, two()))


# 4.1.1.10 Generators and closures
def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')

def poly(x):
    return 2 * x**2 - 4 * x + 2

print_function([x for x in range(-2, 3)], poly)


#--- using lambda function
def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')

print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2)

# 4.1.1.11 Generators and closures
list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()

# 4.1.1.12 Generators and closures
from random import seed, randint

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

print(data)
print(filtered)


# 4.1.1.13 Generators and closures
def outer(par):
    loc = par

    def inner():
        return loc
    return inner
var = 1
fun = outer(var)
print(fun())

# 4.1.1.14 Generators and closures
def make_closure(par):
    loc = par

    def power(p):
        return p ** loc
    return power

fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(5):
    print(i, fsqr(i), fcub(i))

for x in (el * 2 for el in range(5)):
    print(x)

# 4.1.1.15 Generators and closures
short_list = [1, "Python", -1, "Monty"]
new_list = list(filter(lambda s: isinstance(s, str), short_list))
print(new_list)  # outputs ['Python', 'Monty'].

def tag(tg):
    tg2 = tg
    tg2 = tg[0] + '/' + tg[1:]
    def inner(str):
        return tg + str + tg2
    return inner
b_tag = tag('<b>')
print(b_tag('Monty Python')) # outputs <b>Monty Python</b>



# Ex1
class Vowels:
    def __init__(self):
        self.vow = "aeiouy "  # Yes, we know that y is not always considered a vowel.
        self.pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos == len(self.vow):
            raise StopIteration
        self.pos += 1
        return self.vow[self.pos - 1]

vowels = Vowels()
for v in vowels:
    print(v, end=' ')

# ex2
any_list = [1, 2, 3, 4]
even_list = list(map(lambda x: x | 1, any_list)) # | is bitwise OR
print(even_list)

# Ex3
def replace_spaces(replacement='*'):
    def new_replacement(text):
        return text.replace(' ', replacement)
    return new_replacement


stars = replace_spaces()
print(stars("And Now for Something Completely Different"))

# 4.3.1.1 Working with real files
stream = open("text.txt", "rt", encoding = "utf-8")
print(stream.read()) # printing the content of the file



# 4.3.1.2 Working with real files

from os import strerror

try:
    cnt = 0
    s = open("text.txt", "rt")
    #"D:\\myfiles\welcome.txt"
    #s = open('d:/data/text.txt', "rt")
    ch = s.read(1)
    while ch != '':
        print(ch, end='')
        cnt += 1
        ch = s.read(1)
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))


import os
print(os.path.expanduser('~'))

# # 4.3.1.3 Working with real files
from os import strerror

try:
    cnt = 0
    s = open('text.txt', "rt")
    content = s.read()
    for ch in content:
        print(ch, end='')
        cnt += 1
    s.close()
    print("\n\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))


# 4.3.1.4 Working with real files

from os import strerror

try:
	ccnt = lcnt = 0
	for line in open('text.txt', 'rt'):
		lcnt += 1
		for ch in line:
			print(ch, end='')
			ccnt += 1
	print("\n\nCharacters in file:", ccnt)
	print("Lines in file:     ", lcnt)
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))

# 4.3.1.5 Working with real files
s = open("text.txt")
print(s.readlines(20))
print(s.readlines(20))
print(s.readlines(20))
print(s.readlines(20))
s.close()

#---------------
from os import strerror

try:
    ccnt = lcnt = 0
    s = open('text.txt', 'rt')
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


# 4.3.1.6 Working with real files
from os import strerror
try:
	ccnt = lcnt = 0
	for line in open('text.txt', 'rt'):
		lcnt += 1
		for ch in line:
			print(ch, end='')
			ccnt += 1
	print("\n\nCharacters in file:", ccnt)
	print("Lines in file:     ", lcnt)
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))


# 4.3.1.7 Working with real files

from os import strerror

try:
	fo = open('newtext.txt', 'wt') # A new file (newtext.txt) is created.
	for i in range(10):
		s = "line: #" + str(i+1) + "\n"
		for ch in s:
			fo.write(ch)
	fo.close()
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))


# 4.3.1.8 Working with real files
from os import strerror

try:
    fo = open('newtext8.txt', 'wt')
    for i in range(10):
        fo.write("line #" + str(i+1) + "\n")
    fo.close()
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

import sys
sys.stderr.write("Error message")


# 4.3.1.9 Working with real files
data = bytearray(10)
data

# 4.3.1.10 Working with real files

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 - i

for b in data:
    print(hex(b))

# 4.3.1.11 Working with real files
from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file2.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# Your code that reads bytes from the stream should go here.



from os import strerror

data = bytearray(10)

try:
    bf = open('file2.bin', 'rb')
    bf.readinto(data)
    bf.close()

    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


# 4.3.1.12 Working with real files
from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# Your code that reads bytes from the stream should go here.

from os import strerror

try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read())
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# 4.3.1.13 Working with real files
from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# Your code that reads bytes from the stream should go here.
try:
    bf = open('file.bin', 'rb')
    data = bytearray(bf.read(5))
    bf.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# 4.3.1.14 Working with real files

from os import strerror

srcname = input("Enter the source file name: ")
try:
    src = open(srcname, 'rb')
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno)	

dstname = input("Enter the destination file name: ")
try:
    dst = open(dstname, 'wb')
except Exception as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    src.close()
    exit(e.errno)	

buffer = bytearray(65536)
total  = 0
try:
    readin = src.readinto(buffer)
    while readin > 0:
        written = dst.write(buffer[:readin])
        total += written
        readin = src.readinto(buffer)
except IOError as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    exit(e.errno)	
    
print(total,'byte(s) succesfully written')
src.close()
dst.close()

# 4.4.1.2 The os module
import os
print(os.uname()) # work in UNIX

import platform
print(platform.uname()) # work in Windows


# 4.4.1.3 The os module
import os

os.mkdir("my_first_directory2")
print(os.listdir())


# # 4.4.1.4 The os module
import os

os.makedirs("my_first_directory3/my_second_directory4")
os.chdir("my_first_directory2")
print(os.listdir())


# # # 4.4.1.5 The os module
import os

os.makedirs("my_first_directory/my_second_directory")
os.chdir("my_first_directory")
print(os.getcwd())
os.chdir("my_second_directory")
print(os.getcwd())

# # # 4.4.1.6 The os module
import os

os.mkdir("my_first_directory")
print(os.listdir())
os.rmdir("my_first_directory")
print(os.listdir())


# 4.4.1.7 The os module
import os

returned_value = os.system("mkdir my_first_directory")
print(returned_value)


import os
os.makedirs("my_first_directory/my_second_directory")
os.removedirs("my_first_directory/my_second_directory")
print(os.listdir())



# 4.4.1.8 The os module: LAB

import os

# 4.5.1.2 The datetime module

from datetime import date

today = date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)


from datetime import date

my_date = date(2019, 11, 4)
print(my_date)

# 4.5.1.3 The datetime module
from datetime import date
import time

timestamp = time.time()
print("Timestamp:", timestamp)

d = date.fromtimestamp(timestamp)
print("Date:", d)


# 4.5.1.4 The datetime module
from datetime import date

d = date.fromisoformat('2019-11-04')
print(d)

# 4.5.1.5 The datetime module
from datetime import date
d = date(1991, 2, 5)
print(d)
d = d.replace(year=1992, month=1, day=16)
print(d)

# 4.5.1.6 The datetime module
from datetime import date

d = date(2019, 11, 4)
print(d.weekday())


from datetime import date

d = date(2019, 11, 4)
print(d.isoweekday())


# 4.5.1.7 The datetime module
from datetime import time
t = time(14, 53, 20, 1)
print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)


# 4.5.1.8 The datetime module
import time

class Student:
    def take_nap(self, seconds):
        print("I'm very tired. I have to take a nap. See you later.")
        time.sleep(seconds)
        print("I slept well! I feel great!")

student = Student()
student.take_nap(5)

# 4.5.1.9 The datetime module
import time

timestamp = 1572879180
print(time.ctime(timestamp))


import time
print(time.ctime())

# 4.5.1.10 The datetime module
import time

timestamp = 1572879180
print(time.gmtime(timestamp))
print(time.localtime(timestamp))


# 4.5.1.11 The datetime module
import time

timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.asctime(st))
print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))

# 4.5.1.12 The datetime module
from datetime import datetime

dt = datetime(2019, 11, 4, 14, 53)

print("Datetime:", dt)
print("Date:", dt.date())
print("Time:", dt.time())

# 4.5.1.13 The datetime module
from datetime import datetime

print("today:", datetime.today())
print("now:", datetime.now())
print("utcnow:", datetime.utcnow())


# 4.5.1.14 The datetime and time modules (continued)

from datetime import datetime
dt = datetime(2020, 10, 4, 14, 55)
print("Timestamp:", dt.timestamp())

# 4.5.1.15 The datetime and time modules (continued)
from datetime import date

d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))

# 4.5.1.16 The datetime and time modules (continued)
from datetime import time
from datetime import datetime

t = time(14, 53)
print(t.strftime("%H:%M:%S"))

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%y/%B/%d %H:%M:%S"))

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%Y/%B/%d %H:%M:%S"))

# 4.5.1.17 The datetime and time modules (continued)
import time

timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.strftime("%Y/%m/%d %H:%M:%S", st))
print(time.strftime("%Y/%m/%d %H:%M:%S"))

# 4.5.1.18 The datetime and time modules (continued)
from datetime import datetime
print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))

import time
print(time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))


# 4.5.1.19 The datetime and time modules (continued)
from datetime import date
from datetime import datetime

d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)
print(d1 - d2)

dt1 = datetime(2020, 11, 4, 0, 0, 0)
dt2 = datetime(2019, 11, 4, 14, 53, 0)
print(dt1 - dt2)

# 4.5.1.20 The datetime and time modules (continued)
from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=3)
print(delta)



from datetime import timedelta

delta = timedelta(weeks=2, days=2, hours=1)
print("Days:", delta.days)
print("Seconds:", delta.seconds)
print("Microseconds:", delta.microseconds)

# 4.5.1.21 The datetime and time modules (continued)

from datetime import timedelta
from datetime import date
from datetime import datetime

delta = timedelta(weeks=2, days=2, hours=2)
print(delta)

delta2 = delta * 2
print(delta2)

d = date(2019, 10, 4) + delta2
print(d)

dt = datetime(2019, 10, 4, 14, 53) + delta2
print(dt)


#4.5.1.22 The datetime and time modules: LAB
dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%y/%m/%d %H:%M:%S"))
print(dt.strftime("%y/%B/%d %H:%M:%S"))



#4.5.1.23 
from datetime import date

my_date = date(2020, 9, 29)
print("Year:", my_date.year) # Year: 2020
print("Month:", my_date.month) # Month: 9
print("Day:", my_date.day) # Day: 29


from datetime import date
print("Today:", date.today()) # Displays: Today: 2020-09-29

from datetime import date
import time
timestamp = time.time()
d = date.fromtimestamp(timestamp)


from datetime import date

d = date(2020, 9, 29)
print(d.strftime('%Y/%m/%d')) # Displays: 2020/09/29


from datetime import date

d1 = date(2020, 11, 4)
d2 = date(2019, 11, 4)

d = d1 - d2
print(d) # Displays: 366 days, 0:00:00.
print(d * 2) # Displays: 732 days, 0:00:00.

from datetime import time

t = time(14, 39)
print(t.strftime("%H:%M:%S"))


# 4.6.1.2 The calendar module

import calendar
print(calendar.calendar(2022))


import calendar
calendar.prcal(2020)


# 4.6.1.2 The calendar module
import calendar
print(calendar.month(2020, 11))


# 4.6.1.4 The calendar module
import calendar
calendar.setfirstweekday(calendar.SUNDAY)
calendar.prmonth(2020, 12)

# 4.6.1.5 The calendar module
import calendar
print(calendar.weekday(2020, 12, 24))
print(calendar.weekday(2022, 1, 22))

# 4.6.1.6 The calendar module
import calendar
print(calendar.weekheader(3))

# 4.6.1.7 The calendar module
import calendar

print(calendar.isleap(2020))
print(calendar.leapdays(2010, 2021))  # Up to but not including 2021.

# 4.6.1.9 The calendar module
import calendar  

c = calendar.Calendar(calendar.SUNDAY)

for weekday in c.iterweekdays():
    print(weekday, end=" ")


# 4.6.1.10 The calendar module
import calendar  

c = calendar.Calendar()

for date1 in c.itermonthdates(2019, 11):
    print(date1, end=" ")

# 4.6.1.11 The calendar module
import calendar  

c = calendar.Calendar()

for iter in c.itermonthdays(2019, 11):
    print(iter, end=" ")

for iter in c.itermonthdays2(2019, 11):
    print(iter, end=" ")

for iter in c.itermonthdays3(2019, 11):
    print(iter, end=" ")    
    
for iter in c.itermonthdays4(2019, 11):
    print(iter, end=" ")    
    
# 4.6.1.12 The calendar module  
import calendar  

c = calendar.Calendar()

for data in c.monthdays2calendar(2020, 12):
    print(data)


import calendar
print(calendar.month(2020, 9))


