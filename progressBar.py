import numpy as np
import time

def start_prog():
    tmp = time.time()
    return "                         ",0,tmp,tmp

def print_prog(i,N,bar,prog,start_time,pre_time):
    now = time.time()
    percent = int(i/N*100)
    print("\r",str(percent).rjust(3),"%|",sep="",end="")
    if (prog+1)*4==percent:
        bar = bar[:prog] + '-' + bar[prog+1:]
        prog += 1
    print(bar,"|",str(i).rjust(len(str(N))),"/",N," now: ",'{:.1f}'.format(1/(now-pre_time)),"/s average: ",'{:.1f}'.format(i/(now-start_time)),"/s",sep="",end="")#時間追加
    return bar,prog,now

def end_prog(N,start_time):
    all_time = time.time() - start_time
    print("\r100%|-------------------------|",N,"/",N," average:",' {:.1f}'.format(i/(all_time)),"/s total elapsed time: ",'{:.1f}'.format(all_time),"s",sep="") #累計速度,経過時間


N = int(1e5)
#prepare
bar,prog,start_time,pre_time = start_prog()
#
for i in range(N):

    #処理=========
    #np.pi*np.pi
    #処理=========

    bar,prog,pre_time = print_prog(i+1,N,bar,prog,start_time,pre_time)

#end

end_prog(N,start_time)
del bar,prog,start_time,pre_time
#
'''
USAGE:

bar,prog,start_time,pre_time = start_prog()

for i in range([ループ回数]):
    ---------
    処理
    ---------
    bar,prog,pre_time = print_prog(i+1,N,bar,prog,start_time,pre_time)

end_prog(N,start_time)
del bar,prog,start_time,pre_time
'''