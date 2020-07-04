# Boost.python用法



首先安裝一些需要用的庫

# 安裝

在Manjaro上面安裝`boost`, `boost-libs`。

MacOS安裝

```sh
brew install boost
brew install boost-python
brew install boost-python3
```



由於我是使用Anaconda Python3，所以boost的地方是用conda安裝

```sh
conda install -c meznom boost-python 
```



# 執行

 

範例是參考[這裡](https://stackoverflow.com/questions/28571611/boost-python-hello-world-on-mac-os-x)的也就是`boost.python`的官方例子，首先建立兩個檔案`hello_ext.cpp`、`setup.py`

- `hello_ext.cpp`



```cpp
#include <boost/python.hpp>

char const* greet()
{
   return "Greetings!";
}

BOOST_PYTHON_MODULE(hello_ext)
{
    using namespace boost::python;
    def("greet", greet);
}
```



- `setup.py`



```python
from distutils.core import setup
from distutils.extension import Extension

hello_ext = Extension(
    'hello_ext',
    sources=['hello_ext.cpp'],
    libraries=['boost_python-mt'],
)

setup(
    name='hello-world',
    version='0.1',
    ext_modules=[hello_ext])
```



- 編譯



```sh
python setup.py build_ext --inplace -v
running build_ext
building 'hello_ext' extension
gcc -Wno-unused-result -Wsign-compare -Wunreachable-code -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -I/Users/huangshijun/opt/anaconda3/include -arch x86_64 -I/Users/huangshijun/opt/anaconda3/include -arch x86_64 -I/Users/huangshijun/opt/anaconda3/include/python3.7m -c hello_ext.cpp -o build/temp.macosx-10.9-x86_64-3.7/hello_ext.o
g++ -bundle -undefined dynamic_lookup -L/Users/huangshijun/opt/anaconda3/lib -arch x86_64 -L/Users/huangshijun/opt/anaconda3/lib -arch x86_64 -arch x86_64 build/temp.macosx-10.9-x86_64-3.7/hello_ext.o -lboost_python-mt -o /Users/huangshijun/Desktop/hello_ext.cpython-37m-darwin.so
```






