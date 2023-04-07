# Tensor 計算 complex number


記錄一下Tensorflow和Pytorch的complex number用法，以後真的寫code會遇到什麼問題就不清楚了，Debug的階段才會發現。

## Tensorflow

Tensorflows相對而言比較不好用，因爲要建立好session，還有graph邏輯之後，纔可以print結果，要一些時間下去瞭解。

```py
import numpy as np
import tensorflow as tf
A = np.array([[17.+4.j, -3.+2.j],
              [-7.+3.j,  1.+9.j]])

B = np.array([[ 60.+1.j,  -4.+3.j],
              [-12.+2.j,   0.+3.j]])
mmul = A*B # np.mul(A,B)
matmmul = A@B # np.matmul(A,B)
# A+B, A-B, A**2, A**(1/2) 
AA = tf.convert_to_tensor(A,dtype=tf.complex128) # tf.float64
BB = tf.convert_to_tensor(B,dtype=tf.complex128)
mull = AA*BB # tf.multiply(AA,BB)
matmull = AA@BB # tf.matmul(AA,BB)

# 不好用
real = tf.constant([2.25, 3.25])
imag = tf.constant([4.75, 5.75])
comp = tf.complex(real, imag)  # [[2.25 + 4.75j], [3.25 + 5.75j]]

with tf.Session() as sess:
    print('1d complex:\ncomp:\n%s \n[real,imag]:\n%s'%( sess.run(comp), sess.run([real,imag]) ) )
    print('converted:\nAA:\n%s\nBB:\n%s\n' %( sess.run([AA]), sess.run([BB]) )  )
    print('numpy:\n\nmul: \n%s\nmatmul: \n%s\n'%(mmul,matmmul))
    print('tensor:\n\n mul:\n%s\nmatmul:\n%s\n' %( sess.run([mull]), sess.run([matmull]) )  ) # [mull,matmull]
```

result:

```
1d complex:
comp:
[2.25+4.75j 3.25+5.75j]
[real,imag]:
[array([2.25, 3.25], dtype=float32), array([4.75, 5.75], dtype=float32)]
converted:
AA:
[array([[17.+4.j, -3.+2.j],
       [-7.+3.j,  1.+9.j]])]
BB:
[array([[ 60.+1.j,  -4.+3.j],
       [-12.+2.j,   0.+3.j]])]

numpy:

mul:
[[1016.+257.j    6. -17.j]
 [  78. -50.j  -27.  +3.j]]
matmul:
[[1048.+227.j  -86. +26.j]
 [-453. +67.j   -8. -30.j]]

tensor:

 mul:
[array([[1016.+257.j,    6. -17.j],
       [  78. -50.j,  -27.  +3.j]])]
matmul:
[array([[1048.+227.j,  -86. +26.j],
       [-453. +67.j,   -8. -30.j]])]
```

tensorflow 1.x 版本跟 2.x 最大差別應該是session了，如果是用2.3的話可以直接這樣用，和Pytorch幾乎差不多

```py
>>> print(A)
[[17.+4.j -3.+2.j]
 [-7.+3.j  1.+9.j]]
>>> A@BB
<tf.Tensor: shape=(2, 2), dtype=complex128, numpy=
array([[1048.+227.j,  -86. +26.j],
       [-453. +67.j,   -8. -30.j]])>
>>> AA@B
<tf.Tensor: shape=(2, 2), dtype=complex128, numpy=
array([[1048.+227.j,  -86. +26.j],
       [-453. +67.j,   -8. -30.j]])>
```

```py
import numpy as np
import tensorflow as tf

CB = np.zeros((4,4,6),dtype=complex)

# SCMA Codebooks
CB[:,:,0] = [ [ 0,                  0,                  0,                  0 ],
              [ -0.1815-1j*0.1318,  -0.6351-1j*0.4615,   0.6351+1j*0.4615,   0.1815+1j*0.1318 ],
              [ 0,                  0,                  0,                  0 ],
              [ 0.7851,            -0.2243,             0.2243,            -0.7851 ] ]

CB[:,:,1] = [ [ 0.7851,            -0.2243,             0.2243,            -0.7851 ],
              [ 0,                  0,                  0 ,                 0 ],
              [ -0.1815-1j*0.1318,  -0.6351-1j*0.4615,   0.6351+1j*0.4615,   0.1815+1j*0.1318 ],
              [ 0,                  0,                  0,                  0 ] ]

CB[:,:,2] = [ [ -0.6351+1j*0.4615,   0.1815-1j*0.1318,  -0.1815+1j*0.1318,   0.6351-1j*0.4615],
              [ 0.1392-1j*0.1759,   0.4873-1j*0.6156,  -0.4873+1j*0.6156,  -0.1392+1j*0.1759],
              [ 0,                  0,                  0,                  0],
              [ 0,                  0,                  0,                  0 ] ]

CB[:,:,3] = [ [ 0,                  0,                  0,                  0 ],
              [ 0,                  0,                  0,                  0 ],
              [ 0.7851,            -0.2243,             0.2243,            -0.7851 ],
              [ -0.0055-1j*0.2242,  -0.0193-1j*0.7848,   0.0193+1j*0.7848,   0.0055+1j*0.2242 ] ]

CB[:,:,4] = [ [ -0.0055-1j*0.2242,  -0.0193-1j*0.7848,   0.0193+1j*0.7848,   0.0055+1j*0.2242 ],
              [ 0,                  0,                  0,                  0 ],
              [ 0,                  0,                  0,                  0 ],
              [ -0.6351+1j*0.4615,   0.1815-1j*0.1318,  -0.1815+1j*0.1318,   0.6351-1j*0.4615 ] ]

CB[:,:,5] = [ [ 0,                  0,                  0,                  0 ],
              [ 0.7851,            -0.2243,             0.2243,            -0.7851 ],
              [ 0.1392-1j*0.1759,   0.4873-1j*0.6156,  -0.4873+1j*0.6156,  -0.1392+1j*0.1759 ],
              [ 0,                  0,                  0,                  0 ] ]
CBB = tf.convert_to_tensor(CB,dtype=tf.complex128)


with tf.Session() as sess:
    print('CB[:,:,0]:\n%s\n'%CB[:,:,0])
    print('tensor CBB[:,:,0]:\n%s\n'%sess.run([CBB[:,:,0]]))
```

result:

```
CB[:,:,0]:
[[ 0.    +0.j      0.    +0.j      0.    +0.j      0.    +0.j    ]
 [-0.1815-0.1318j -0.6351-0.4615j  0.6351+0.4615j  0.1815+0.1318j]
 [ 0.    +0.j      0.    +0.j      0.    +0.j      0.    +0.j    ]
 [ 0.7851+0.j     -0.2243+0.j      0.2243+0.j     -0.7851+0.j    ]]

tensor CBB[:,:,0]:
[array([[ 0.    +0.j    ,  0.    +0.j    ,  0.    +0.j    ,
         0.    +0.j    ],
       [-0.1815-0.1318j, -0.6351-0.4615j,  0.6351+0.4615j,
         0.1815+0.1318j],
       [ 0.    +0.j    ,  0.    +0.j    ,  0.    +0.j    ,
         0.    +0.j    ],
       [ 0.7851+0.j    , -0.2243+0.j    ,  0.2243+0.j    ,
        -0.7851+0.j    ]])]
```

## Pytorch

Pytorch的Complex要在1.6版本，CUDA 10.2之後的版本做GPU計算。

雖然似乎可以做計算，不過由於還是beta測試版本。比起Tensorflow用起來好了不少，Debug起來容易了很多，不用多寫`print(session.run([var])`

```py
import numpy as np
import torch
>>> x = torch.randn(2,2, dtype=torch.cfloat) # or torch.complex64, torch.complex128
>>> x
tensor([[-0.4621-0.0303j, -0.2438-0.5874j],
     [ 0.7706+0.1421j,  1.2110+0.1918j]])

A = np.array([[17.+4.j, -3.+2.j],
              [-7.+3.j,  1.+9.j]])

B = np.array([[ 60.+1.j,  -4.+3.j],
              [-12.+2.j,   0.+3.j]])

AA = torch.tensor([[17.+4.j, -3.+2.j],
              [-7.+3.j,  1.+9.j]])

BB = torch.tensor([[ 60.+1.j,  -4.+3.j],
              [-12.+2.j,   0.+3.j]])
# A+B, A-B, A**2, A**(1/2) 
mmul = AA*BB # or torch.mul(A,B) 
print('mul: \n%s\n '%mmul)

matmmul = torch.matmul(AA,BB) #這裏似乎 1.6 還沒開發完全
>>> AA@BB # or use torch.matmul(A,B)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: _th_addmm_out not supported on CPUType for ComplexFloat

# 不過可以用numpy代替，相對而言，可能就是不用gpu算，或是計算慢點，不過numpy 還是很快
# torch 可以這樣用，相對還滿和藹的
>>> np.matmul(AA,BB)
tensor([[1048.+227.j,  -86.+26.j],
        [-453.+67.j,   -8.-30.j]])
>>> A@B
array([[1048.+227.j,  -86. +26.j],
       [-453. +67.j,   -8. -30.j]])

# 似乎tensor 放在前面 後面用numpy array會可以用，不過還是輸入numpy fcn比較好
>>> AA@B
tensor([[1048.+227.j,  -86.+26.j],
        [-453.+67.j,   -8.-30.j]], dtype=torch.complex128)
>>> A@BB
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for @: 'numpy.ndarray' and 'Tensor'


AA = torch.tensor(A,dtype=torch.cfloat) # or torch.complex64, torch.complex128
>>> torch.tensor(A,dtype=torch.cfloat)
tensor([[17.+4.j, -3.+2.j],
        [-7.+3.j,  1.+9.j]])
```
