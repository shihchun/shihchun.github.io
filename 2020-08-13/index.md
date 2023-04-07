# Python 多進程


Python提高計算效率的方法不外乎有多線程和多進程，多線程是使用Threading的庫來完成，主要可以處理IO操作，而由於Global Intepreter Lock的關係，所以使用CPU密集操作的時候則要使用Multiprocessing來做多進程。

今天來用這個庫來跑一個模擬。

原始碼在[這裏](https://github.com/XassassinXsaberX/communication-simulation/blob/master/MIMO/channel%20capacity/ergodic_capacity.py)

在我的電腦上面計算，沒有多進程的時候執行時間約爲`19.356636 sec`。

```py
import numpy as np
import matplotlib.pyplot as plt
import time
tStart = time.time()#計時開始

snr_db = [0]*12
snr = [0]*12
capacity = [0]*12
N = 5000 #執行N次來找channel capacity
for i in range(len(snr)):
    snr_db[i] = 2*i
    snr[i] = np.power(10,snr_db[i]/10)

for k in range(5):
    for i in range(len(snr_db)):
        cap = 0
        if k == 0:
            Nt = 1
            Nr = 1
        elif k == 1:
            Nt = 1
            Nr = 2
        elif k == 2:
            Nt = 2
            Nr = 1
        elif k == 3:
            Nt = 2
            Nr = 2
        elif k == 4:
            Nt = 4
            Nr = 4

        H = [[0j]*Nt for m in range(Nr)]
        H = np.matrix(H)

        for j in range(N):
            # 先決定MIMO的通道矩陣
            for m in range(Nr):
                for n in range(Nt):
                    H[m, n] = 1 / np.sqrt(2) * np.random.randn() + 1j / np.sqrt(2) * np.random.randn()

            #累積所有目前channel matrix的通道容量
            cap += np.log2( np.linalg.det(np.identity(Nr) + snr[i]/Nt * H * H.getH()).real ) #因為det後的值為複數，所以我們取其實部

        capacity[i] = cap / N

    plt.plot(snr_db,capacity,marker='o',label='Nt = {0} , Nr = {1}'.format(Nt,Nr))

plt.title('ergodic channel capacity (unknown CSI)')
plt.xlabel('Eb/No , dB')
plt.ylabel('bps/Hz')
plt.legend()
plt.grid(True)
tEnd = time.time()#計時結束
print ("It cost %f sec" % (tEnd - tStart))#會自動做近位
plt.show()
```

參考這裏的方法進行改寫，`partial`、`multiprocessing.Pool(cpus)`、`multiprocessing.map`(partial_fcn, fcn_test_list)



```py
cpus = os.cpu_count()
p1 = multiprocessing.Pool(cpus)

def job(k,N,snr,capacity,snr_db):
    (...some code...)
    pass

partial_function = partial( job,N=N,snr=snr,capacity=capacity,snr_db=snr_db )
res = p1.map( partial_function, range(5)) # 將range(5) list元素的內容，帶入最前面定義的k多進程迭代
```

經過上面方法修改，`7.121585 sec`，差不多快三倍快的速度，如果計算量過大的模擬，也可以試着從計算量比較大的迴圈著手，改成多進程，可以加快很多計算速度。

```py
#coding=utf-8
import multiprocessing as mp
from functools import partial
import os
import time

import numpy as np
import matplotlib.pyplot as plt

def job(k,N,snr,capacity,snr_db):
    # for k in range(5):
    for i in range(len(snr_db)):
        if k == 0:
            Nt = 1
            Nr = 1
        elif k == 1:
            Nt = 1
            Nr = 2
        elif k == 2:
            Nt = 2
            Nr = 1
        elif k == 3:
            Nt = 2
            Nr = 2
        elif k == 4:
            Nt = 4
            Nr = 4
        H = [[0j]*Nt for m in range(Nr)]
        H = np.matrix(H)
        cap = 0
        for j in range(N):
            # 先決定MIMO的通道矩陣
            for m in range(Nr):
                for n in range(Nt):
                    H[m, n] = 1 / np.sqrt(2) * np.random.randn() + 1j / np.sqrt(2) * np.random.randn()
            #累積所有目前channel matrix的通道容量
            cap += np.log2( np.linalg.det(np.identity(Nr) + snr[i]/Nt * H * H.getH()).real ) #因為det後的值為複數，所以我們取其實部
        capacity[i] = cap / N
    print('\n\nPrint Test Result:\n capacity:%s\n Nt %s\n Nr %s' %(capacity,Nt,Nr) )
    return {'capacity':capacity,'Nt':Nt,'Nr':Nr}
    pass

def main():
    snr_db = [0]*12
    snr = [0]*12
    capacity = [0]*12
    N = 5000 #執行N次來找channel capacity
    for i in range(len(snr)):
        snr_db[i] = 2*i
        snr[i] = np.power(10,snr_db[i]/10)
        pass
    # for k in range(5): # 這裏寫成job() 再用 partial function 調用
    #     for i in range(len(snr_db)):
    #         if k == 0:
    #             Nt = 1
    #             Nr = 1
    #         elif k == 1:
    #             Nt = 1
    #             Nr = 2
    #         elif k == 2:
    #             Nt = 2
    #             Nr = 1
    #         elif k == 3:
    #             Nt = 2
    #             Nr = 2
    #         elif k == 4:
    #             Nt = 4
    #             Nr = 4
    #         H = [[0j]*Nt for m in range(Nr)]
    #         H = np.matrix(H)
    #         cap = 0
    #         for j in range(N):
    #             # 先決定MIMO的通道矩陣
    #             for m in range(Nr):
    #                 for n in range(Nt):
    #                     H[m, n] = 1 / np.sqrt(2) * np.random.randn() + 1j / np.sqrt(2) * np.random.randn()
    #             #累積所有目前channel matrix的通道容量
    #             cap += np.log2( np.linalg.det(np.identity(Nr) + snr[i]/Nt * H * H.getH()).real ) #因為det後的值為複數，所以我們取其實部
    #         capacity[i] = cap / N
    #     # partial_function = partial(job, k=k,N=N,snr=snr,capacity=capacity,snr_db=snr_db)
    #     # res=p1.map( partial_function, range(len(snr_db)) )
    #     print('\n\nPrint Test Result:\n capacity:%s\n Nt %s\n Nr %s' %(capacity,Nt,Nr) )
    #     plt.plot(snr_db,capacity,marker='o',label='Nt = {0} , Nr = {1}'.format(Nt,Nr))
    partial_function = partial( job,N=N,snr=snr,capacity=capacity,snr_db=snr_db )
    res = p1.map( partial_function, range(5))
    print(res)
    for i in range(len(res)):
        capacity = res[i]['capacity']
        Nt = res[i]['Nt']
        Nr = res[i]['Nr']
        plt.plot(snr_db,capacity,marker='o',label='Nt = {0} , Nr = {1}'.format(Nt,Nr))
    plt.title('ergodic channel capacity (unknown CSI)')
    plt.xlabel('Eb/No , dB')
    plt.ylabel('bps/Hz')
    plt.legend()
    plt.grid(True)

if __name__=='__main__':
    plt.figure()
    cpus = os.cpu_count() 
    print('You have %s CPUs \n' %cpus)
    p1 = mp.Pool(cpus)
    tStart = time.time() # 計時開始
    main()
    tEnd = time.time() # 計時結束
    print("It cost %f sec" % (tEnd - tStart)) # 會自動做近位
    plt.show()
```

除了多進程、多線程，現在還有[parfor](https://pypi.org/project/parfor/)，可以使用

不過如果要真的改到最高速度的話，可能還是摒棄掉numpy，numbda的量子計算方式可能可以提高更多效率，計算CPU效能就知道其實沒有提高太多速度。

