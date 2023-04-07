# Pytorch視覺化


{{< typeit code=python >}}
import torch
import torch.nn as nn # Layer
import torch.nn.functional as F # Function
import torchvision
{{< /typeit >}}

Pytorch相對於tensorflow不一樣的地方是不是用tf.variable來分類圖，而是包在Tensor裏面，這就會讓tensorboard相對起來難讀一點，不過要讓可讀性增加還是要從程式下手，另外Autograd也是它特別的地方。

## Tensorboard 生成圖

```py
from torch.utils.tensorboard import SummaryWriter
# from tensorboardX import SummaryWriter # or use this

# Writer will output to ./runs/ directory by default
writer = SummaryWriter()

# Initial the Network model (class)
# writer.add_image('images', grid, 0)
# writer.add_figure("matplotlib/figure", figure)
writer.add_graph(model, images)
writer.close()
```

執行結束後，預設儲存在`./runs/`

```console
tensorboard --logdir="./runs/"
```

## torchvision生成graphviz流程圖

```py
outputs = model(inputs)
from torchviz import make_dot, make_dot_from_trace
for param in model.named_parameters():
    print(param[0])
vis_graph = make_dot(outputs, params=dict(model.named_parameters()))
vis_graph.view()  # "Digraph.gv.pdf"
```

## Save & Load weight


在這個儲存weight、bias的部分，tensorflow v1是相對起來比較簡單的，直接存成`*.meta`還有另外兩個檔案，直接使用`FileLoader`讀取。

Pytorch使用類似Pickle的方式儲存Weight，他們讓model下面多了一個屬性儲存現在的weight，然後還有兩個方法可以把weight重新加載到模型上面。

跟tensorflow v1比起來，就是原本的Model的網路網路（Class）要留着，不能像是tensorflow v1直接使用meta讀取Model Graph，缺點就是不能藏程式吧！


```py
# Save weight
# Print model's state_dict
print("Model's state_dict:")
for param_tensor in model.state_dict():
    print(param_tensor, "\t", model.state_dict()[param_tensor].size())

# Print optimizer's state_dict
print("Optimizer's state_dict:")
for var_name in optimizer.state_dict():
    print(var_name, "\t", optimizer.state_dict()[var_name])

torch.save(model, 'net.pt')
torch.save(model.state_dict(), 'net_params.pt')
torch.save(optimizer, 'optimizer.pt')
torch.save(optimizer.state_dict(), 'optimizer_params.pt')
```

加載

```py
model.load_state_dict(torch.load('net_params.pt'))
model.eval()
```

用法差不多這樣，print出來的結果差不多是這樣，去測試咯

```console
conv1.weight     torch.Size([6, 3, 5, 5])
conv1.bias   torch.Size([6])
conv2.weight     torch.Size([16, 6, 5, 5])
conv2.bias   torch.Size([16])
fc1.weight   torch.Size([120, 400])
fc1.bias     torch.Size([120])
fc2.weight   torch.Size([84, 120])
fc2.bias     torch.Size([84])
fc3.weight   torch.Size([10, 84])
fc3.bias     torch.Size([10])

Optimizer's state_dict:
state    {}
param_groups     [{'lr': 0.001, 'momentum': 0.9, 'dampening': 0, 'weight_decay': 0, 'nesterov': False, 'params': [4675713712, 4675713784, 4675714000, 4675714072, 4675714216, 4675714288, 4675714432, 4675714504, 4675714648, 4675714720]}]
```

如果還要儲存現在的計算過程，分很多次計算的話可以使用checkpoint的方式儲存

```py
torch.save({
            'epoch': epoch+1,
            'model_state_dict': model.state_dict(),
            'optimizer_state_dict': optimizer.state_dict(),
            'loss': loss,
            ...
            }, PATH)
```

加載

```py
model = TheModelClass(*args, **kwargs)
optimizer = TheOptimizerClass(*args, **kwargs)

checkpoint = torch.load(PATH)
model.load_state_dict(checkpoint['model_state_dict'])
optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
epoch = checkpoint['epoch']
loss = checkpoint['loss']

model.eval()
# - or -
model.train()
```

## Torchvision 網路

- AlexNet
- VGG
- ResNet
- SqueezeNet
- DenseNet
- Inception v3
- GoogLeNet
- ShuffleNet v2
- MobileNet v2
- ResNeXt
- Wide ResNet
- MNASNet

```py
import torch
import torch.nn as nn # Layer
import torch.nn.functional as F # Function
import torchvision
model = torchvision.models.alexnet()
```

## Custom Layer

參考GitHub [Sébastien M. P.](https://github.com/wavefrontshaping/complexPyTorch)的程式

在建構子構建我們用到的Layer class，然後在forward定義計算流程

其中ComplexFunction.complex_relu

```py
def complex_relu(input_r,input_i):
    return relu(input_r), relu(input_i)
```

其中 complexLayers.ComplexBatchNorm2d

```py
class ComplexConv2d(Module):

    def __init__(self,in_channels, out_channels, kernel_size=3, stride=1, padding = 0,
                 dilation=1, groups=1, bias=True):
        super(ComplexConv2d, self).__init__()
        self.conv_r = Conv2d(in_channels, out_channels, kernel_size, stride, padding, dilation, groups, bias)
        self.conv_i = Conv2d(in_channels, out_channels, kernel_size, stride, padding, dilation, groups, bias)

    def forward(self,input_r, input_i):
#        assert(input_r.size() == input_i.size())
        return self.conv_r(input_r)-self.conv_i(input_i), \
               self.conv_r(input_i)+self.conv_i(input_r)
```


Class跟Function的差別主要是，Class要做實體化的動作，所以要在建構子的地方做實體化，比如`ComplexConv2d`如果我要使用的話就要在Class的`__init__`做簡單的實體化到記憶體。

Class上面比較細節的就不討論了，class decorator，@staticmethod或是jit之類的不是重點。

```py
# MNIST example
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import datasets, transforms
from complexLayers import ComplexBatchNorm2d, ComplexConv2d, ComplexLinear
from complexFunctions import complex_relu, complex_max_pool2d

batch_size = 64
trans = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (1.0,))])
train_set = datasets.MNIST('../data', train=True, transform=trans, download=True)
test_set = datasets.MNIST('../data', train=False, transform=trans, download=True)

train_loader = torch.utils.data.DataLoader(train_set, batch_size= batch_size, shuffle=True)
test_loader = torch.utils.data.DataLoader(test_set, batch_size= batch_size, shuffle=True)

class ComplexNet(nn.Module):
    
    def __init__(self):
        super(ComplexNet, self).__init__()
        self.conv1 = ComplexConv2d(1, 20, 5, 1)
        self.bn  = ComplexBatchNorm2d(20)
        self.conv2 = ComplexConv2d(20, 50, 5, 1)
        self.fc1 = ComplexLinear(4*4*50, 500)
        self.fc2 = ComplexLinear(500, 10)
             
    def forward(self,x):
        xr = x
        # imaginary part to zero
        xi = torch.zeros(xr.shape, dtype = xr.dtype, device = xr.device)
        xr,xi = self.conv1(xr,xi)
        xr,xi = complex_relu(xr,xi)
        xr,xi = complex_max_pool2d(xr,xi, 2, 2)
        
        
        xr,xi = self.bn(xr,xi)
        xr,xi = self.conv2(xr,xi)
        xr,xi = complex_relu(xr,xi)
        xr,xi = complex_max_pool2d(xr,xi, 2, 2)
        
        xr = xr.view(-1, 4*4*50)
        xi = xi.view(-1, 4*4*50)
        xr,xi = self.fc1(xr,xi)
        xr,xi = complex_relu(xr,xi)
        xr,xi = self.fc2(xr,xi)
        # take the absolute value as output
        x = torch.sqrt(torch.pow(xr,2)+torch.pow(xi,2))
        return F.log_softmax(x, dim=1)

# # Run training on 50 epochs
# for epoch in range(50):
#     train(model, device, train_loader, optimizer, epoch)

device = torch.device("cpu" )
model = ComplexNet().to(device)
optimizer = torch.optim.SGD(model.parameters(), lr=0.01, momentum=0.9)

def train(model, device, train_loader, optimizer, epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = F.nll_loss(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % 1000 == 0:
            print('Train Epoch: {:3} [{:6}/{:6} ({:3.0f}%)]\tLoss: {:.6f}'.format(
                epoch,
                batch_idx * len(data), 
                len(train_loader.dataset),
                100. * batch_idx / len(train_loader), 
                loss.item())
            )


inputs,cla = next(iter(test_loader))
from torch.utils.tensorboard import SummaryWriter
# Writer will output to ./runs/ directory by default
writer = SummaryWriter()
writer.add_graph(model, inputs)
writer.close()

from torchviz import make_dot, make_dot_from_trace
# for param in model.named_parameters():
#     print(param[0])

vis_graph = make_dot(model(inputs), params=dict(model.named_parameters()))
vis_graph.view()  # Digraph.gv.pdf
```

最後放一下產生的圖好了，不然感覺好像只有寫

![](Deepin_selectarea_20200914140238.png "Tensorboard")


{{< gview "make_dot.pdf" >}}

