#变量可以指向函数，把函数本身赋给变量

print(abs(-10))

f=abs
print(f(-10))


#既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接受另一个函数作为参数，这种函数称为高阶函数
def add(x,y,f):
    return f(x)+f(y)

print(add(-5,6,abs))
#x==>-5，y==>6，f==>abs，f(x)+f(y)==>abs(-5)+abs(6)


#python中有map()和reduce()函数
#map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个函数，并把结果作为新的list返回
def f(x):
    return x*x

map(f,[1,2,3,4,5,6,7,8,9])
#[1,4,9,16,25,36,49,64,81]
#map也可用循环代替
map(str,[1,2,3,4,5,6,7,8,9])
#['1','2','3','4','5','6','7','8','9']



#reduce把一个函数作用在一个序列上，这个函数必须接受两个参数，reduce把结果继续和序列的下一个函数做累积运算
#reduce(f,[x1,x2,x3,x4])=f(f(f(x1,x2),x3),x4)
def fn(x,y):
    return x*10+y





#filter函数用于过滤序列，也是接受一个函数和一个序列，把传入的函数依次作用于每个函数，然后返回之时true还是false决定保留还是舍弃该函数

def is_odd(n):
   return n%2 == 1

filter(is_odd,[1,2,4,5,6,9,10,15])
#[1,5,9,15]
#用filter()这个高阶函数关键在于正确实现一个“筛选”函数





#sorted函数
#函数可以作为返回值，用于闭包


'''
def lazy_sum(*args):     #*为可变参数，**又是什么？
    def sum():
        ax = 0
        for n in args
        ax = ax + n
    return ax
return sum


f=lazy_sum(1,3,5,7,9)
#f   得不到结果
#f()   才能得到结果
'''




#匿名函数
#装饰器，借助@语法
#模块及其调用，包的定义
#正则表达式re的各种内容、切分字符串、匹配(match?)、分组(group)
#struct