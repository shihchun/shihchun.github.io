# ns3 day 1




ns3 is build with the waf-tools whitch is based on python, so we need to learn how to configure and build the modules with it.

First，copy the links.

![Screenshot_20200704_144302](/media/Screenshot_20200704_144302.png)

switch to terminal and download

```sh
wget url
tar -jxvf file
# make alias or not
```

<script id="asciicast-Z4Yip8Uut840XQu3JbD29sw4p" src="https://asciinema.org/a/Z4Yip8Uut840XQu3JbD29sw4p.js" async></script>

# Bassic useage

{{< mind >}}
- waf
    - configure
        - "--enable-tests"
        - "--enable-examples"
        - "--build-profile=debug"
        - "--with-python=python2"
        - "--disable-python"
        - "--enable-modules"
    - build
    - run
{{< /mind >}}

## Full build

```sh
./waf confiugre --enable-tests --enable-examples
./waf
or
./waf build
or
./waf -vvv
```

<script id="asciicast-50aIrGsOOeg3M3DEum1pAm1Zy" src="https://asciinema.org/a/50aIrGsOOeg3M3DEum1pAm1Zy.js" async></script>

## Build core module only

```sh
./waf confiugre --enable-tests --enable-examples --enable-modules=core
```

<script id="asciicast-EKKZp60dxkwn6txIBxn1oqvPt" src="https://asciinema.org/a/EKKZp60dxkwn6txIBxn1oqvPt.js" async></script>

building log is at build/config.log

```sh
cat build/config.log
```

# Running Program

```sh
./waf --run sample-simulator
./waf --run src/core/examples/sample-simulator # file.cc
## configure add --with-python=python2 need pybindgen
./waf --pyrun src/core/examples/sample-simulator.py
```

# Build variations

{{< mind >}}
- waf
    - debuging code enable
        - "./waf -d debug configure"
    - optimized
        - "./waf -d optimized configure"
    - static libraries
        - "./waf --enable-static configure"
{{< /mind >}}

# Add modules and check dependency

cat the file of wscript in the src/module_name

```python
cat src/propagation/wscript | more
## -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

def build(bld):
    module = bld.create_ns3_module('propagation', ['network', 'mobility'])
    module.includes = '.'
    module.source = [
        'model/propagation-delay-model.cc',
        'model/propagation-loss-model.cc',
        'model/jakes-propagation-loss-model.cc',
        'model/jakes-process.cc',
        'model/cost231-propagation-loss-model.cc',
        'model/okumura-hata-propagation-loss-model.cc',
        'model/itu-r-1411-los-propagation-loss-model.cc',
        'model/itu-r-1411-nlos-over-rooftop-propagation-loss-model.cc',
        'model/kun-2600-mhz-propagation-loss-model.cc',
        'model/channel-condition-model.cc',
--更多--
```

In this script we know the propagation module need the network and mobility modules, and build the source file (modulename/model/*) to ns3/model_name.

and call with, more you can see the example of core module `sample-simulator.cc` and `sample-simulator.py`

```cpp
#include "ns3/jakes-propagation-loss-model.h"
```

```python
import ns.propagation
```


```python
module_test.source = [
        'test/propagation-loss-model-test-suite.cc',
        'test/okumura-hata-test-suite.cc',
        'test/itu-r-1411-los-test-suite.cc',
        'test/kun-2600-mhz-test-suite.cc',
        'test/itu-r-1411-nlos-over-rooftop-test-suite.cc',
        'test/channel-condition-model-test-suite.cc',
        'test/three-gpp-propagation-loss-model-test-suite.cc',
        ]
    # Tests encapsulating example programs should be listed here
    if (bld.env['ENABLE_EXAMPLES']):
        module_test.source.extend([
        #   'test/propagation-examples-test-suite.cc',
            ])
```

You can try if you build propagation module, if you `--enable-tests`, `--enable-examples`, it can recognize the file without full path.

```sh
./waf configure --enable-tests --enable-examples --enable-module=core 
./waf # build
```

```python
    headers = bld(features='ns3header')
    headers.module = 'propagation'
    headers.source = [
        'model/propagation-delay-model.h',
        'model/propagation-loss-model.h',
        'model/jakes-propagation-loss-model.h',
        'model/jakes-process.h',
        'model/propagation-cache.h',
        'model/cost231-propagation-loss-model.h',
        'model/propagation-environment.h',
        'model/okumura-hata-propagation-loss-model.h',
        'model/itu-r-1411-los-propagation-loss-model.h',
        'model/itu-r-1411-nlos-over-rooftop-propagation-loss-model.h',
        'model/kun-2600-mhz-propagation-loss-model.h',
        'model/channel-condition-model.h',
        'model/three-gpp-propagation-loss-model.h',
        ]

    if (bld.env['ENABLE_EXAMPLES']):
        bld.recurse('examples')

    bld.ns3_python_bindings()
```

It is the API headers of the module, should be the public API, but some of them may private.

# Running code

```
./waf --run scratch-simulator
./waf --run scratch/scratch-simulator
cp scratch/scratch-simulator.cc scratch/wss.cc
./waf
./waf wss
```

<script id="asciicast-n2L9eVwqq4LjYJf4GfcK2gycv" src="https://asciinema.org/a/n2L9eVwqq4LjYJf4GfcK2gycv.js" async></script>

## Add subdir

You can build more complicated example with this functionality.

```
cd scratch/
tree
.
├── scratch-simulator.cc
└── subdir
    └── scratch-simulator-subdir.cc
cd ..
./waf --run scratch/subdir/scratch-simulator-subdir # failed
./waf --run scratch/subdir # failed
./waf --run subdir # correct
```

<script id="asciicast-AC67jPbIW5CbIIqV8t4HH4c6h" src="https://asciinema.org/a/AC67jPbIW5CbIIqV8t4HH4c6h.js" async></script>



# Other configure parameters

```sh
(base) ➜  ns-3.31 ls -alh utils | grep ".ns3rc"
-rwxrwxrwx 1 geek geek  405  7月  4 14:55 .ns3rc
cat utils/.ns3rc
#! /usr/bin/env python

# A list of the modules that will be enabled when ns-3 is run.
# Modules that depend on the listed modules will be enabled also.
#
# All modules can be enabled by choosing 'all_modules'.
modules_enabled = ['all_modules']

# Set this equal to true if you want examples to be run.
examples_enabled = False

# Set this equal to true if you want tests to be run.
tests_enabled = False
```

In this file you can set something for waf configure.


```sh
cp utils/.ns3rc .
vi utils/.ns3rc
./waf configure --enable-modules='core','network','mobility','propagation' --with-python=python2
./waf
```

<script id="asciicast-I4yWyDxBxKGLVP01mK7xECvx4" src="https://asciinema.org/a/I4yWyDxBxKGLVP01mK7xECvx4.js" async></script>


# GCC compile parameters

`ns3/build/c4che/_c4che.py` have the very detial settings of the gcc compiler. If you familier with gcc, you can change your compiler flags when it need.

for example you can remove all the `-Werror` in the file, you can look at [doc](https://gcc.gnu.org/onlinedocs/gcc/Warning-Options.html) and [-Werror is Not Your Friend](https://embeddedartistry.com/blog/2017/05/22/werror-is-not-your-friend/) for more info.

That flag means `cc1plus: all warnings being treated as error`, I disable this flag.


# To run test and example file

if I configure with `--enable-modules='core','network','mobility','propagation'`

```
./waf configure --enable-modules='core','network','mobility','propagation'  --enable-tests --enable-examples
cp src/propagation/examples/jakes-propagation-model-example.cc scratch
./waf # build success
./waf --run jakes-propagation-model-example # ok
```

# Debug the program

Debug the program by using waf-tool, the debuger based on gdb.

{{< mind >}}
- gdb
    - Print
        - PrintHelp (or just --help)
        - PrintGlobals
        - PrintTypeIds
{{< /mind >}}

- PrintHelp

```sh
(base) ➜  ns-3.31 ./waf --run  "sample-simulator --help"
sample-simulator [General Arguments]

General Arguments:
    --PrintGlobals:              Print the list of globals.
    --PrintGroups:               Print the list of groups.
    --PrintGroup=[group]:        Print all TypeIds of group.
    --PrintTypeIds:              Print all TypeIds.
    --PrintAttributes=[typeid]:  Print all attributes of typeid.
    --PrintHelp:                 Print this help message.
```

- PrintGlobals

```sh
(base) ➜  ns-3.31 ./waf --run  "sample-simulator --PrintGlobals"
Global values:
    --RngRun=[1]
        The substream index used for all streams
    --RngSeed=[1]
        The global seed of all rng streams
    --SchedulerType=[ns3::MapScheduler]
        The object class to use as the scheduler implementation
    --SimulatorImplementationType=[ns3::DefaultSimulatorImpl]
        The object class to use as the simulator implementation
```

- PrintTypeIds

```sh
(base) ➜  ns-3.31 ./waf --run  "sample-simulator --PrintTypeIds"
Registered TypeIds:
    ns3::CalendarScheduler
    ns3::ConstantRandomVariable
    ns3::DefaultSimulatorImpl
    ns3::DeterministicRandomVariable
    ns3::EmpiricalRandomVariable
    ns3::ErlangRandomVariable
    ns3::ExponentialRandomVariable
    ns3::GammaRandomVariable
    ns3::HeapScheduler
    ns3::ListScheduler
    ns3::LogNormalRandomVariable
    ns3::MapScheduler
    ns3::NormalRandomVariable
    ns3::Object
    ns3::ObjectBase
    ns3::ParetoRandomVariable
    ns3::PriorityQueueScheduler
    ns3::RandomVariableStream
    ns3::RealtimeSimulatorImpl
    ns3::Scheduler
    ns3::SequentialRandomVariable
    ns3::SimulatorImpl
    ns3::Synchronizer
    ns3::TriangularRandomVariable
    ns3::UniformRandomVariable
    ns3::WallClockSynchronizer
    ns3::WeibullRandomVariable
    ns3::ZetaRandomVariable
    ns3::ZipfRandomVariable
```

# Ref

Ref the ns3 2015 traning videos and ppts:

<!-- {{< vimeo 133503055 >}} -->
{{< rawhtml >}}
<br>
<iframe src='https://view.officeapps.live.com/op/embed.aspx?src=http://www.nsnam.org/tutorials/consortium15/ns-3-training-part1.pptx' width='98%' height='500px' frameborder='0'>
</iframe>
<br>
<br>
<iframe src='https://view.officeapps.live.com/op/embed.aspx?src=http://www.nsnam.org/tutorials/consortium15/ns-3-training-part2.pptx' width='98%' height='500px' frameborder='0'>
</iframe>
<br>
<!--
<iframe src='https://docs.google.com/viewer?url=http://www.nsnam.org/tutorials/consortium15/ns-3-training-part1.pdf&embedded=true' width='98%' height='700px' frameborder='0'>
</iframe> -->
<br>
{{< /rawhtml >}}

