import json, random
def dec(n, p=2):
    b = 10**p
    w, f = divmod(n, b)
    fs = str(f).zfill(p).rstrip("0")
    return str(w) + "." + fs if fs else str(w)
def m(n): return f"{n//100}.{str(n%100).zfill(2)}"
def pl(n, one, many): return f"{n}" + (one if n == 1 else many)
def v(n, one, many): return one if n == 1 else many
def sheets(n, b):
    k = -(-n//b)
    return f"The {pl(n,' stamp',' stamps')} at {pl(b,' stamp',' stamps')} a sheet {v(n,'takes','take')} {pl(k,' sheet',' sheets')}, the last sheet holding {pl(n-(k-1)*b,' stamp',' stamps')}."
def weeks(n, w):
    k = n//w
    return f"The {pl(n,' stamp',' stamps')} at {pl(w,' stamp',' stamps')} a week {v(n,'lasts','last')} {pl(k,' full week',' full weeks')} with {pl(n-k*w,' stamp',' stamps')} left for the next week."
def cost(b, pc, n):
    cc = b*pc
    pb = (2*cc + n)//(2*n)
    return f"The {pl(b,' sheet',' sheets')} at ${m(pc)} a sheet {v(b,'comes','come')} to ${m(cc)}, ${m(pb)} a stamp."
def time_(n, pm):
    t = -(-n//pm); h, r = t//60, t%60
    return f"The {pl(n,' stamp',' stamps')} at {pl(pm,' stamp',' stamps')} a minute {v(n,'takes','take')} {pl(t,' minute',' minutes')}, {pl(h,' hour',' hours')} {pl(r,' minute',' minutes')}."
random.seed(782)
R = random.randint
cases = [
 dict(fn="sheets", args=["465","20"], expect=sheets(465,20)),
 dict(fn="weeks", args=["465","60"], expect=weeks(465,60)),
 dict(fn="cost", args=["24","13.20","465"], expect=cost(24,1320,465)),
 dict(fn="time", args=["465","8"], expect=time_(465,8)),
 dict(fn="sheets", args=["1","1"], expect=sheets(1,1)),
 dict(fn="sheets", args=["460","20"], expect=sheets(460,20)),
 dict(fn="sheets", args=["1000000","1000"], expect=sheets(1000000,1000)),
 dict(fn="weeks", args=["1","1"], expect=weeks(1,1)),
 dict(fn="weeks", args=["420","60"], expect=weeks(420,60)),
 dict(fn="weeks", args=["1000000","100000"], expect=weeks(1000000,100000)),
 dict(fn="cost", args=["1","0.01","1"], expect=cost(1,1,1)),
 dict(fn="cost", args=["100000","999.99","1000000"], expect=cost(100000,99999,1000000)),
 dict(fn="time", args=["1","1"], expect=time_(1,1)),
 dict(fn="time", args=["60","1"], expect=time_(60,1)),
 dict(fn="time", args=["1000000","100"], expect=time_(1000000,100)),
]
for _ in range(20):
    n,b=R(1,1000000),R(1,1000); cases.append(dict(fn="sheets", args=[str(n),str(b)], expect=sheets(n,b)))
for _ in range(20):
    n,w=R(1,1000000),R(1,100000); cases.append(dict(fn="weeks", args=[str(n),str(w)], expect=weeks(n,w)))
for _ in range(25):
    b,p,n=R(1,100000),R(1,99999),R(1,1000000); cases.append(dict(fn="cost", args=[str(b),dec(p),str(n)], expect=cost(b,p,n)))
for _ in range(19):
    n,m=R(1,1000000),R(1,100); cases.append(dict(fn="time", args=[str(n),str(m)], expect=time_(n,m)))
errs=[["sheets",["0","20"]],["sheets",["1000001","12"]],["sheets",["2.5","12"]],["sheets",["465","0"]],["sheets",["465","1001"]],
 ["weeks",["0","30"]],["weeks",["465","0"]],["weeks",["465","100001"]],["weeks",["465","1.5"]],["weeks",["1000001","30"]],
 ["cost",["0","13.20","465"]],["cost",["100001","13.20","465"]],["cost",["24","0","465"]],["cost",["24","13.205","465"]],["cost",["24","13.20","0"]],
 ["time",["0","8"]],["time",["465","0"]],["time",["465","101"]],["time",["465","6.5"]],["time",["1000001","5"]]]
json.dump(dict(cases=cases, errors=errs), open("expected.json","w"), indent=1)
print(len(cases),"cases,",len(errs),"errcases")
