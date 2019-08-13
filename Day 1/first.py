import time;
print("hello there")
a = b = c = 1, 2, "JD"
print(a, b, c)
list = ['abcd', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print(list)
print(list[0])
print(list[1:4])
print(list[2:])
print(list[:2])
print(list[:-1])
print(tinylist * 2)
print(list + tinylist)

tuple = ("abcd", 1, 2)
print(tuple)

dict = {}
dict["one"] = "this is one"
dict[2] = "this is two"
tinydict = {"name": "JD", "code": 1122, "dept": "Web"}
print(dict["one"])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())
tinydict["code"]=1111;
print(tinydict)
x = y = z = 10
print(len(tuple))
x, y = 1, 2

print("Value of x , y : ", x, y);

def ti():
    localtime = time.asctime( time.localtime(time.time()) )
    print ("Local current time :", localtime)
ti();

def cha(t):
    t=10;
    print(t);
t=20;
cha(t);
print(t);
def printinfo(age,name):
    print("age:", age);
    print("name:", name);
printinfo(name="JD", age=20);

def printnum(args1,*vartuple):
    print(args1);
    for var in vartuple:
        print(var);

printnum(10);
printnum(10,20,30,40,50,60);



def sum(arg1,arg2):
    total=arg1+arg2;
    print(total);
    return total;
sum(40,50);

sums=lambda args3, agrs4: args3 + agrs4;
print(sum(10, 50));