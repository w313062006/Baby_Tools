import os,time;
rh=int(time.strftime("%H",time.localtime()));
rm=int(time.strftime("%M",time.localtime()));
cmd="cmd.exe /k shutdown -s -t 0";

print rh,rm
c1=True;
while c1:
    try:
        h=int(raw_input("Please input the hour:"));
        if h>=0 and h<=23:
            c1=False;
        else:
            continue;
    except:
        continue;
c2=True;
while c2:
    try:
        m=int(raw_input("Please input the minute:"));
        if m>=0 and m<=59:
            c2=False;
        else:
            continue;
    except:
        continue;
if h==rh:
    if m<=rm:
        os.system(cmd);
    else:
        time.sleep((m-rm)*60);
        os.system(cmd);
elif h>rh:
    tem1=(h-rh-1)*3600+(60-rm+m)*60;
    time.sleep(tem1);
    os.system(cmd);
else:
    tem2=(23-rh+h)*3600+(60-rm+m)*60;
    time.sleep(tem2);
    os.system(cmd);