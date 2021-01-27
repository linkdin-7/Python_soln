import datetime  
from datetime import datetime, date, time, timedelta 
import calendar
import ast 

def MissingDates(thisdict):
    keylist = list()
    valuelist=list()

    upkey=list()
    upvalue=list()
  
    for i in thisdict.keys():
        keylist.append(datetime.strptime(i, '%Y-%m-%d'))
      
        valuelist.append(thisdict[i])
    

    for i in range(len(keylist)-1):
        diff=keylist[i+1]-keylist[i];
     
        if (diff.days)>1:
            firstday=keylist[i];
            firstvalue=int(valuelist[i]);
          
            avg=(int(valuelist[i+1])-int(valuelist[i]))/(diff.days);

            for j in range(1,diff.days):
                firstday+=timedelta(days=1)
                upkey.insert(j,str(firstday));
                firstvalue=firstvalue+avg;
                upvalue.insert(j,int(firstvalue));
                
    for key in upkey: 
        for value in upvalue: 
            thisdict[key] = value 
            upvalue.remove(value) 
            break
    for i in sorted (thisdict.keys()):  
        print((i, thisdict[i]), end =" ")  
        

def fun(x):
    dic = {'Mon':0, 'Tue':0, 'Wed':0,'Thu':0, 'Fri':0,'Sat':0, 'Sun':0}
    dic2={}
    for j in x:
        date = j
        year,month,day = (int(i) for i in date.split('-'))
        dayNumber = calendar.weekday(year, month, day) 
        days =['Mon', 'Tue', 'Wed', 'Thu','Fri', 'Sat', 'Sun']
        dic[days[dayNumber]]+=x[j]
        for k,v in dic.items():
            if v==0:
                dic2.update({k:v})
                MissingDates(dic2);

    print(dic)


x = {'2020-01-01':4, 2020-01-02':4,'2020-01-03':6,'2020-01-04':8,'2020-01-05':2,'2020-01-06':-6,'2020-01-07':2,'2020-01-08':-2}
fun(x)
