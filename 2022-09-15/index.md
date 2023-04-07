# C語言筆記




## Day1

### GCC編譯過程

C語言編譯過程會按照順序經過

- 預處理（define include替換後給編譯器處理），不屬於關鍵字
- gcc -E -o
- 編譯
- gcc -S -o
- 組譯（匯編）
- gcc -c -o
- 鏈接 連接*.o的binary檔案
- gcc -o 產生可執行檔案

```sh
 gcc -v -o build test1.c
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/lib/gcc/x86_64-pc-linux-gnu/11.1.0/lto-wrapper
Target: x86_64-pc-linux-gnu
Configured with: /build/gcc/src/gcc/configure --prefix=/usr --libdir=/usr/lib --libexecdir=/usr/lib --mandir=/usr/share/man --infodir=/usr/share/info --with-bugurl=https://bugs.archlinux.org/ --enable-languages=c,c++,ada,fortran,go,lto,objc,obj-c++,d --with-isl --with-linker-hash-style=gnu --with-system-zlib --enable-__cxa_atexit --enable-cet=auto --enable-checking=release --enable-clocale=gnu --enable-default-pie --enable-default-ssp --enable-gnu-indirect-function --enable-gnu-unique-object --enable-install-libiberty --enable-linker-build-id --enable-lto --enable-multilib --enable-plugin --enable-shared --enable-threads=posix --disable-libssp --disable-libstdcxx-pch --disable-libunwind-exceptions --disable-werror gdc_include_dir=/usr/include/dlang/gdc
Thread model: posix
Supported LTO compression algorithms: zlib zstd
gcc version 11.1.0 (GCC)
COLLECT_GCC_OPTIONS='-v' '-o' 'build' '-mtune=generic' '-march=x86-64' '-dumpdir' 'build-'
 /usr/lib/gcc/x86_64-pc-linux-gnu/11.1.0/cc1 -quiet -v test1.c -quiet -dumpdir build- -dumpbase test1.c -dumpbase-ext .c -mtune=generic -march=x86-64 -version -o /tmp/ccvuBrUn.s
GNU C17 (GCC) version 11.1.0 (x86_64-pc-linux-gnu)
        compiled by GNU C version 11.1.0, GMP version 6.2.1, MPFR version 4.1.0-p13, MPC version 1.2.1, isl version isl-0.24-GMP

GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
ignoring nonexistent directory "/usr/lib/gcc/x86_64-pc-linux-gnu/11.1.0/../../../../x86_64-pc-linux-gnu/include"
#include "..." search starts here:
#include <...> search starts here:
 /usr/lib/gcc/x86_64-pc-linux-gnu/11.1.0/include
 /usr/local/include
 /usr/lib/gcc/x86_64-pc-linux-gnu/11.1.0/include-fixed
 /usr/include
End of search list.
GNU C17 (GCC) version 11.1.0 (x86_64-pc-linux-gnu)
        compiled by GNU C version 11.1.0, GMP version 6.2.1, MPFR version 4.1.0-p13, MPC version 1.2.1, isl version isl-0.24-GMP

GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
Compiler executable checksum: ec1bc319e19ef4dd2d241e66d95d4739
COLLECT_GCC_OPTIONS='-v' '-o' 'build' '-mtune=generic' '-march=x86-64' '-dumpdir' 'build-'
 as -v --64 -o /tmp/ccYy1xpJ.o /tmp/ccvuBrUn.s
GNU assembler version 2.36.1 (x86_64-pc-linux-gnu) using BFD version (GNU Binutils) 2.36.1
COMPILER_PATH=/usr/lib/gcc/x86_64-pc-linux-gnu/11.1.0/:/usr/lib/gcc/x86_64-pc-linux-gnu/11.1.0/:/usr/lib/gcc/x86_64-pc-linux-gnu/:/usr/lib/gcc/x86_64-pc-linux-gnu/11.1.0/:/usr/lib/gcc/x86_64-pc-linux-gnu/
LIBRARY_PATH=/usr/lib/gcc/x86_64-pc-linux-gnu/11.1.0/:/usr/lib/gcc/x86_64-pc-linux-gnu/11.1.0/../../../../lib/:/lib/../lib/:/usr/lib/../lib/:/usr/lib/gcc/x86_64-pc-linux-gnu/11.1.0/../../../:/lib/:/usr/lib/
COLLECT_GCC_OPTIONS='-v' '-o' 'build' '-mtune=generic' '-march=x86-64' '-dumpdir' 'build.'
 /usr/lib/gcc/x86_64-pc-linux-gnu/11.1.0/collect2 -plugin /usr/lib/gcc/x86_64-pc-linux-gnu/11.1.0/liblto_plugin.so -plugin-opt=/usr/lib/gcc/x86_64-pc-linux-gnu/11.1.0/lto-wrapper -plugin-opt=-fresolution=/tmp/cciGeuNv.res -plugin-opt=-pass-through=-lgcc -plugin-opt=-pass-through=-lgcc_s -plugin-opt=-pass-through=-lc -plugin-opt=-pass-through=-lgcc -plugin-opt=-pass-through=-lgcc_s --build-id --eh-frame-hdr --hash-style=gnu -m elf_x86_64 -dynamic-linker /lib64/ld-linux-x86-64.so.2 -pie -o build /usr/lib/gcc/x86_64-pc-linux-gnu/11.1.0/../../../../lib/Scrt1.o /usr/lib/gcc/x86_64-pc-linux-gnu/11.1.0/../../../../lib/crti.o /usr/lib/gcc/x86_64-pc-linux-gnu/11.1.0/crtbeginS.o -L/usr/lib/gcc/x86_64-pc-linux-gnu/11.1.0 -L/usr/lib/gcc/x86_64-pc-linux-gnu/11.1.0/../../../../lib -L/lib/../lib -L/usr/lib/../lib -L/usr/lib/gcc/x86_64-pc-linux-gnu/11.1.0/../../.. /tmp/ccYy1xpJ.o -lgcc --push-state --as-needed -lgcc_s --pop-state -lc -lgcc --push-state --as-needed -lgcc_s --pop-state /usr/lib/gcc/x86_64-pc-linux-gnu/11.1.0/crtendS.o /usr/lib/gcc/x86_64-pc-linux-gnu/11.1.0/../../../../lib/crtn.o
COLLECT_GCC_OPTIONS='-v' '-o' 'build' '-mtune=generic' '-march=x86-64' '-dumpdir' 'build.'
```

在編譯過程中可以看到編譯`cc1`、組譯`as`、鏈接`collect2`的過程

```sh
/usr/lib/gcc/x86_64-pc-linux-gnu/11.1.0/cc1
 as -v --64 -o /tmp/ccYy1xpJ.o /tmp/ccvuBrUn.s
 /usr/lib/gcc/x86_64-pc-linux-gnu/11.1.0/collect2
 ```


### 編譯文件範例

```sh
gcc -S -o a.s test1.c # 編譯 a.s我組合語言檔案

ls
a.s  test1.c
gcc -c -o a.o test1.c # 組譯 a.o爲二進制檔案
ls
a.s  a.o  test1.c
```

`test1.c`檔案如下：

```c
#include <stdio.h>

int main(){
    int a[10];
	for(int i=0;i<10;i++) {a[i]=9-i;}
    for(int i=0; i<10;i++){a[i]=a[a[i]];}
    printf("a[8]: %d",a[8]);
}
```

`a.s`檔案如下：

```assembly
	.file	"test1.c"
	.text
	.section	.rodata
.LC0:
	.string	"a[8]: %d"
	.text
	.globl	main
	.type	main, @function
main:
.LFB0:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$64, %rsp
	movq	%fs:40, %rax
	movq	%rax, -8(%rbp)
	xorl	%eax, %eax
	movl	$0, -56(%rbp)
	jmp	.L2
.L3:
	movl	$9, %eax
	subl	-56(%rbp), %eax
	movl	%eax, %edx
	movl	-56(%rbp), %eax
	cltq
	movl	%edx, -48(%rbp,%rax,4)
	addl	$1, -56(%rbp)
.L2:
	cmpl	$9, -56(%rbp)
	jle	.L3
	movl	$0, -52(%rbp)
	jmp	.L4
.L5:
	movl	-52(%rbp), %eax
	cltq
	movl	-48(%rbp,%rax,4), %eax
	cltq
	movl	-48(%rbp,%rax,4), %edx
	movl	-52(%rbp), %eax
	cltq
	movl	%edx, -48(%rbp,%rax,4)
	addl	$1, -52(%rbp)
.L4:
	cmpl	$9, -52(%rbp)
	jle	.L5
	movl	-16(%rbp), %eax
	movl	%eax, %esi
	leaq	.LC0(%rip), %rax
	movq	%rax, %rdi
	movl	$0, %eax
	call	printf@PLT
	movl	$0, %eax
	movq	-8(%rbp), %rdx
	subq	%fs:40, %rdx
	je	.L7
	call	__stack_chk_fail@PLT
.L7:
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE0:
	.size	main, .-main
	.ident	"GCC: (GNU) 11.1.0"
	.section	.note.GNU-stack,"",@progbits
```

### 表頭預處理錯誤問題 gcc -I

`<>`尋找系統環境變量中的目錄位置的檔案

```c
#include <stdio.h>
#include "stdio.h"
```

若新增一個`abc.h`的檔案在`./inc`目錄之下，
可以使用`gcc -I ./inc -o build test1.c`



### 鏈接錯誤

```c
#include <stdio.h>
void fun(void);
int main(){
	fun();
	return 0;
}
```

```sh
 gcc -o build test1.c
/usr/sbin/ld: /tmp/ccWBLXSg.o: in function `main':
test1.c:(.text+0x5): undefined reference to `fun'
collect2: error: ld returned 1 exit status
```

修改爲

```c
#include <stdio.h>
void fun(void){}
int main(){
	fun();
	return 0;
}
```

### 多檔案編譯

直接生成

```sh
gcc -o build a.c b.c
gcc -I ./inc -o build a.c b.c
```

生成二進制檔案後，重新進行鏈接

```sh
gcc -c -I ./inc -o a.o a.c
gcc -c -I ./inc -o b.o b.c
gcc -o build a.o b.o
```


### 編譯錯誤

語法問題


### 預處理撰寫

預處理主要有`#include`、`#define`、系統預定義宏（__FUNCTION__、__LINE__、__FILE__）、條件預處理（`#ifdef` `#else` `#endif`）

其中`#include`爲標頭檔案文件位置，`<>`表示爲環境變量中的名字，`""`中表示爲當前目錄的位置


`#define`爲預處理器指示詞，可建立類似函式的宏(宏函數)，需要注意，儘量以**大寫字母表示**，安全起見在運算上加入`()`

Ex:在預處理中需記得加入掛號，如下例子中，若無加入掛號ABx5會爲5+3x5並非我們想要的答案

```c
#include <stdio.h>
#define AB 5+3
#define ABC (5+3)
#define ABCD(x) (5+x)

int main(){
	printf("The %d\n",AB*5);
	printf("The %d\n",ABC*5);
	printf("The %d\n",ABCD(5)*5);
	printf("__FUNCTION__:%s\n__LINE__:%d\n__FILE__:%s",__FUNCTION__,__LINE__,__FILE__); //這裏LINE 10
	return 0;
}
```

```sh
gcc -o build test1.c
./build
The 20
The 40
The 50
__FUNCTION__:main
__LINE__:10
__FILE__:test1.c%
```

#### 條件預處理（`#ifdef` `#else` `#endif`） gcc -D

方便程式碼測試管理使用，避免大量修改而使用的功能
使用`gcc -D ABC` === `#define ABC`

```c
#include <stdio.h>
// #define ABC
int main(){
#ifdef ABC
	printf("====%s====:%d\n",__FILE__,__LINE__);
	printf("%s 函數執行\n",__FUNCTION__);
#endif
	printf("hello world!");
	return 0;
}
```

```sh
gcc -o build test1.c && ./build
hello world!

gcc -D ABC -o build test1.c && ./build
====test1.c====:4
main 函數執行
hello world!%

gcc -DABC -o build test1.c && ./build
====test1.c====:4
main 函數執行
hello world!%
```

#### 宏展開

透過宏展開可以簡化名稱定義，使得撰寫更加方便，在Linux Kernel內核編程上也是尤爲常見，通常用來囊括一些相關訊息使用

`#` 字符串化
`##` 連接符號

```c
#include <stdio.h>
#define ABC(x)	#x
#define DAY(x)	myday##x

int main(){
	int myday1 = 10;
	int myday2 = 20;
	printf(ABC(ab\n)); // 字符串化 ABC爲ab 需要\n換行
	printf(ABC(ab));
	printf("the day is %d\n", DAY(1));
	printf("the day2 is %d\n", DAY(2));
	return 0;
}
```


```sh
gcc  -o build test1.c && ./build
ab
abthe day is 10
the day2 is 20
```


Ex：如下程式便是此定義的衍生使用

```c
#define err(formajt, arg...) printk(KERN_ERR "%s: " format, MY_NAME, ## arg)
#define info(formajt, arg...) printk(KERN_INFO "%s: " format, MY_NAME, ## arg)
#define warn(formajt, arg...) printk(KERN_WARNING "%s: " format, MY_NAME, ## arg)
```

```c
#define ADM8211_SRAM(x) (priv->pdev->revision < ADM8211_REV_BA ? \
		ADM8211_SRAM_A_ ## x: ADM8211_SRAM_B_ ## x)

#define ADM8211_SRAM_INDIV_KEY  0x0000

#define ADM8211_SRAM_A_SHARE_KEY  0x0160
#define ADM8211_SRAM_B_SHARE_KEY  0x00c0

#define ADM8211_SRAM_A_SSID  0x0180
#define ADM8211_SRAM_B_SSID  0x00d4
#define ADM8211_SRAM_SSID ADM8211_SRAM(SSID)
```

## Day2



### C語言關鍵字

C語言常見的32個關鍵字有介紹，簡略概括有，資料形別、自定義數據類型（enum枚舉、typedef、struct、union等等）、邏輯流程判斷式、類型修飾符號等等

char、int、long、short、unsigned、signed、float、double、void
stuct、union、enum、typedef
sizeof、return
if、else
switch、case、default
do、while、for
continue、break、go
auto、register、static、const、extern、volatile

### return

函數定義後返回而已

### sizeof

`sizeof()`存在`()`容易被誤認爲函數，但是實際上在編譯過程中爲關鍵字，主要辨識

功能上主要查詢變量記憶體儲存容量的空間大小，沒什麼好說的

```c
#include <stdio.h>
int main(){
	int a;
	printf("int sizeof %lu\n",sizeof a); // %lu無符號的返回詞
	printf("int sizeof %d\n",sizeof(a));
	float b;
	printf("float sizeof %d\n",sizeof(b));
	double c;
	printf("double sizeof %d\n",sizeof(c));
	char d;
	printf("char sizeof %d\n",sizeof(d));
	long e;
	printf("long sizeof %d\n",sizeof(e));
	short f;
	printf("short sizeof %d\n",sizeof(f));

	return 0;
}
```

```sh
int sizeof 4
int sizeof 4
float sizeof 4
double sizeof 8
char sizeof 1
long sizeof 8
short sizeof 2
```

### char

char爲位元操作的的最小單位`sizeof`爲1byte，1byte=8bits=2^8可以記錄256個狀態，在操作上需要注意最大範圍，當Overflow的問題發生的時候，需對溢出位元進行額外處理

char buffer[32];

```c
#include <stdio.h>
int main(){
	char a=0;
	printf("char sizeof %lu\n",sizeof a); // %lu無符號的返回詞
	for (int i =0; i<255; i+=1){
		printf("%c\n",a); // 字串內容查詢ASCII表
		printf("%d\n",a);
        a++;
	}
	return 0;
}
```

```c
#include <stdio.h>
int main(){
	char a=255;
    printf("%c\n",a); // %lu無符號的返回詞
	char a=256; // overflow
	return 0;
}
```

### int

大小：根據編譯器來進行決定

編譯器最優處理大小，定義形別爲系統一個週期，能夠承受的最大處理單位

Ex：Signed value
- 32bit處理器爲 4 Byte大小=(2^31)-1= 2,147,483,647 dec
- 16bit處理器爲 2 Byte大小=(2^15)-1= 32,767 dec

Ex：Unsinged
- 16bit=(2^16)-1=65,535dec.....

#### 整型常量

在進行賦值的時候會根據編譯器一個週期可以處理的單位爲Limit進行賦值，若是2B系統的，`200`的地方最大只能寫到65535，32bit系統2147483647，其餘進制轉換此處不多介紹

```c
char a = 200;
```

### long, short

特殊長度限制，此關鍵字需瞭解編譯器是否支援

### unsigned, signed

- unsigned 用於數據採集
- signed 用於數學意義的數值運算

```c
#include <stdio.h>

int main(){
	char a=-1; //0xff =最大值255 signed value
    printf("%d\n",a);
	for(int i=0; i<=7; i++){ // 右移8次 除2
        a = a>>1;
		printf("%d\n",a);
	}
	unsigned char b=-1; // b = "11111111"
    printf("%d\n",b);
	for(int i=0; i<=7; i++){ // 右移8次 除2
        b=b>>1;
		printf("%d\n",b);
	}
	return 0;
}
```

```sh
-1 
-1 
-1 
-1 
-1 
-1 
-1 
-1 
-1 
255
127
63 
31 
15 
7  
3  
1  
0  
```

### float, double

- 單精度 float 4B=32bit=-2^128~2^128
- 雙精度 double 8B=64bit=-2^1024~2^1024


### void

void（空的）表示不回傳

```c
void main(){}
```


### 自定義數據類型

在嵌入式系統撰寫中，爲了增加程式可讀性、以及未來編修的方便性，假設一個WDT看門狗計數器在系統中有四個暫存器位置的話，便可以使用自定義的方式完成定義並編輯。

Ex： Register Map

| Register | Address     | R/W | Description                            | Reset Value |
|----------|-------------|-----|----------------------------------------|-------------|
| WTCON    | 0xE270_0000 | R/W | Watchdog Timer Control Register        | 0x00008021  |
| WTDAT    | 0xE270_0004 | R/W | Watchdog Timer Data Register           | 0x00008000  |
| WTCNT    | 0xE270_0008 | R/W | Watchdog Timer Count Register          | 0x00008000  |
| WTCLRINT | 0xE270_000C | W   | Watchdog Timer Interupt Clear Register | -           |

#### struct

在`struct`的創建過程中需注意其中元素的，擺放順序，不僅影響其表示意義，且也可能影響最後生成的結構大小

```c
struct abc{
	unsigned int a;
	unsigned int b;
	unsigned int c;
};

struct abc myAbc;
```


#### union

```c
union abc{
	char a;
	unsigned int b;
};

union abc myAbc;
```

#### struct、union差別

stuct在創建過程中會在各個Variable中創建起始位址，而union則所有變量共用起始位址

假設在union創建如下，在修改b的同時a也會改變，屬於比較技巧性的處理手段

```c
union abc{
	char a;
	int b;
}
```


![struct vs union](https://programmerbay.com/wp-content/uploads/2019/11/structure-and-union.jpg "Struct VS Union")


#### enum

枚舉 enumerate，用來取代#define的使用，增加程式可讀性


```c
// #define MON 0
// #define TUE 1
// #define WED 2

enum week{
	Monday=0,Tuesday=1,Wednesday=2, // 在無標識的情況按照順序進行編號
	Thursday,Friday,Saturday,Sunday
};
```

```c
#include <stdio.h>
enum abc{AA,BB=100,CC};
enum {A,B,C}; //可以不需要定義名稱
int main(){
	printf("%d\n",AA);
	printf("%d\n",BB);
	printf("%d\n",CC);
	printf("%d\n",A);
	printf("%d\n",B);
	printf("%d\n",C);
	return 0;
}
```

```sh
0   
100 
101 
0   
100 
101 
```

實際例子大概看起來如下：

```c
/* The top five bits written to EL3_CMD are a command, the lower 11 bits are the parameter, if applicable */
enum c509cmd{
	TotalReset = 0<<11, Select Window = 1<<11, StartCoax=2<<1,
	RxDisable=3<<11, RxEnable=4<<11, RxReset=5<<11,RxDisable=8<<11,
	TxEnable=9<<11
};
enum Window1 {
	TX_FIFO=0x10, RX_FIFO=0x10, RX_Errors=0x14,
	RxStatus=0x18, Timer=0x1A, TxStatus=0x1B,
	TxFree=0x1c, /* Remaining free bytes in Tx buffer. */
};
enum Window0 {
	Wn0EepromCmd=10,  /* Window 0: EEPROM command register. */
	WnEeprom Data = 12,  /* Window 0 : EEPROM results register. */
	IntrStatus=0x0E,  /* Valid in all windows. */
};

```

#### typedef

建立數據類型的別名，可以使得程式碼的可讀性增加

```c
int a =800; // 800m
int b =1500; // 1500m
typdef int a_t; // 建立一個別名形態，其創立的形態別爲int
a_t mydistance; // mydistance爲一個int型別
```


### 邏輯流程判斷式

#### if else

```c
if(cond){

} else{

}
```

#### switch case defaut


```c
float a;
sitch(a){
	case 1.0:
		break;
	case 2.0:
		continue;
	default:
		char b;
}
```

```c
#include <stdio.h>
#include <stdlib.h>
unsigned char c = '-';

int main(){

    switch (c)
    {
    case '-':
    printf("%c",c);
    
    default:
        printf("default");
        break;
    }
}
```

#### do while for

```c
do{

}while(cond){

}

while(cond){

}

for (start;cond;conpute){
	statement;
	
}
```

#### continue break goto

goto: 同個函數中調用

### 類型修飾符

定義並限定記憶體內部的存放位址
auto、register、static、const、extern、volatile

#### auto

預設使用的情況，auto，設定在可讀寫的位置上

```c
auto int a; // 與int a;  相同
auto long b; // 與long b; 相同
```

加入{}表示爲stack space


#### register

定義快速訪問的變量，
會將訪問次數較高的變量設定爲此，
編譯器會儘量安排CPU的Register去存放定義的變量，
如果Register不足的時候，還是會放在，通常沒什麼用
因爲無法使用`&`取址


```c
#include <stdio.h>
int main(){
	register int a;
	a=0x10;
	printf("the a is %d\n",a);
	printf("the addr %d\n",&a);
	return 0;
}
```

```sh
gcc  -o build test1.c && ./build
test1.c: In function ‘main’:
test1.c:6:9: error: address of register variable ‘a’ requested
    6 |         printf("the addr %d\n",&a);
```

#### static

1. Function 內部的變量定義

```c
int fun(){
	int a;
	static int a;
}
```

2. Function外部的變量

```c
static int a;
int a
int fun (){}
```

3. Function

```c
static int fun (){}
```

#### const

定義一個無法修改的變量，不過實際上還是可以透過指針進行修改，
因爲實際位置被安排在可以修改的記憶體區塊的緣故

```c
#include <stdio.h>
int main(){
	const int a=100;
	a=200; // 無法修改
}
```

```sh
test1.c: In function ‘main’:
test1.c:4:10: error: assignment of read-only variable ‘a’
    4 |         a=200; // 無法修改
```

#### extern

外部聲明，在全域Function使用

#### volatile

告知編譯器的編譯方法的編譯器，不優化編譯的組合語言，
修飾變量值的修改，通常是外部硬體數值修改的時候做修飾


```c
#include <stdio.h>
void pprint(){ print("Hello~")}
int main(){
	int a=100;
	while(a==100);
	pprint();
}
```

```asm
f1: LDR R0, [a]
f2: CMP R0, #100
f3: JMPeq f1	---> JMPEQ f2 // 就沒有去取a的真實位址
f4: pprint();
```



### 運算符號

- basic operator ：`+`、`-`、`*`、`/`、`%`
- logic operator： `||`、`&&`、`>`、`>=`、`<`、`<=`、`!`、`?:`
- bitwize: `>>`、`<<`、`&`、`|`、`^`xor、`~`not // 需要考慮是否爲有號數
- 賦值：`=`、`+=`、`-=`、`^=`
- 限制符：`()`、`[]`、`{}`、
- 訪問自定義空間的成員：`->`、`.`
- 指標取址：`&`、`*`，`&*p===p`互消

!a if(!a){}

char a=0x0000;

`~a` 0xffff

## Day3

### 指針

1. 指針變量指針多大？

在32位元編譯器的系統中指針大小爲4 Byte字節大小
64位元則爲8 Byte大小

1GB=2^N
2^10=1K
2^20=1M
2^30=1G
2^32=4Byte
2^64=8Byte

2. 指針分配多大

看定義的數據形態，例如int、char.... etc

```c
#include <stdio.h>
int main(){
	int *p1;
	int arr[5] = {5,10,15,20,0};
	int *p2 = &arr[0];
	char *p3;
	int a = 5;
	int *p = &a;
	int **q= &p; // pointer to pointer
	printf("%d\n%d\n%d\n%d\n%d\n",sizeof p1,sizeof p2, sizeof p3, sizeof p, sizeof q);
}
```

```sh
8
8
8
8
```

3. 讀取方式

```c
#include <stdio.h>
int main(){
	int a = 0x12345;
	int *p1; // 指標變數指向一個char類型變數範圍，定義後p爲地址
	unsigned char *p2; // 錯誤寫法型別不同，有的編譯器可以執行會得到不同範圍，相同起始位置
	p1=&a; // *p1相當於取*&a,*&對消爲a
	p2=&a;
	printf("\n%x\n%x\n%x\n",p1,*p1,a);
    printf("\n%x\n%x\n%x\n",p2,*p2,a);
    printf("\n%x\n%x\n%x\n",p2+1,*(p2+1),a);
}
```

```sh
30a3fd24
12345
12345

30a3fd24
45
12345

30a3fd25
23
12345
```

#### 指針加入 const


```c
char *p;

const char *p;
char const *p;

char * const p;
char *p const;

const char * const p;
```


```c
#include <stdio.h>
int main(){
	// char *p ="hello world!\n";
	const char *p ="hello world!\n"; // 指標變數宣告後，p爲位置
    char buf[] = {"hello world!\n"};
    char *p2 = buf;
	printf("%x\n%c\n",*p,*p);
    *p2 = 'a';
    printf("%s\n",p);
    printf("%s\n",p2);
}
```

```sh
68
h
hello world!

aello world!
```

```c
#include <stdio.h>
int main(){
	// char *p ="hello world!\n";
	const char *p ="hello world!\n"; // 指標變數宣告後，p爲位置
    char buf[] = {"hello world!\n"};
    const char *p2 = buf;
	printf("%x\n%c\n",*p,*p);
    *p2 = 'a';
    printf("%s\n",p);
    printf("%s\n",p2);
}
```

```sh
 gcc  -o build test1.c && ./build
test1.c: In function ‘main’:
test1.c:8:9: error: assignment of read-only location ‘*p2’
    8 |     *p2 = 'a';
      |         ^
```

#### 指針加入 voliatile、typedef

防止指向內存位置的組合語言被簡化，主要硬體訪問資料的時候做修飾

```c
char *p;
volatile char *p;

*p ==0x10

while(*p==0x10);
fun();
```

#### 指針加入 typedef

對複雜的指針加入名稱定義

Ex：

```c
int (*p[10])(int, void (*p)(int));

char *name_t; // name_t 爲一個指針，指向一個char類型的記憶體空間
typedef char *name_t; // name_t爲一個指針類型的名稱，指向一個char 類型的記憶體空間

name_t abc;
```

#### 指標加減

```c
#include <stdio.h>
int main(){
	int a = 0x12345678;
	int b = 0x99991199;

	int *p1 = &b;
	char *p2 = (char *) &b; // 強制轉型 類型不同
	// *(p1+1) 
	printf("The p1+1 is %x,%x\n", *(p1+1),p1[1]);
	printf("The p2+1 is %x,%x\n", *(p2+1),p2[1]);
}
```

```c
#include <stdio.h>
int main(){
	int a = 0x12345678;
	int b = 0x99991199;

	// 兩個pointer 定義相同起始位置
	int *p1 = &b;
	char *p2 = (char *) &b; // 強制轉型 類型不同
	// *(p1+1) 
	printf("addr p1:%x, p2:%x\n",p1,p2);
	printf("The p1 is %x, p1+1 is %x,%x\n",*p1,*(p1+1),p1[1]);
	printf("The p2 is %x, p2+1 is %x,%x\n",*p2,*(p2+1),p2[1]);
}
```

```sh
gcc  -o build test1.c && ./build
addr p1:12881ef0, p2:12881ef0
The p1 is 99991199, p1+1 is 12345678,12345678
The p2 is ffffff99, p2+1 is 11,11
```

#### 多重指針

```c
int *p = &a;
int **q= &p; // pointer to pointer

int *p[5];
int (*p)[5];
```

### 記憶體空間

在下面的程式碼中，可以看出來pubic的變量位址距離function的定義位置較爲接近，由此可知道，記憶體配置的位置不同

```c
#include <stdio.h>

int main(){
	int a; // a at public
	a=0x10;
	printf("%p\n",&a);
	printf("%p\n",main);
}
```

```sh
gcc  -o build test1.c && ./build
0x7fff42996854
0x5568c472c149
```

```c
#include <stdio.h>
int a; // a at public
int main(){
	a=0x10;
	printf("%p\n",&a);
	printf("%p\n",main);
}
```

```sh
gcc  -o build test1.c && ./build
0x561c3455f034
0x561c3455c139
```


記憶體區段主要分爲code space（malloc）、stack space（local variable）、heap space、kernel space（程式不行訪問）

![](https://img-blog.csdnimg.cn/13cc8bf3b9714d15bbd2e451dc767846.png Code Space)
