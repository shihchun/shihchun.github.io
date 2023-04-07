# Ns3 day 2


## Main program

First we look at the main porgram

```cpp
#include <iostream>
#include "ns3/simulator.h"
#include "ns3/nstime.h"
#include "ns3/command-line.h"
#include "ns3/double.h"
#include "ns3/random-variable-stream.h"
/*
.......
*/
int main (int argc, char *argv[])
{
  CommandLine cmd (__FILE__);
  cmd.Parse (argc, argv);

  MyModel model;
  Ptr<UniformRandomVariable> v = CreateObject<UniformRandomVariable> ();
  v->SetAttribute ("Min", DoubleValue (10));
  v->SetAttribute ("Max", DoubleValue (20));

  Simulator::Schedule (Seconds (10.0), &ExampleFunction, &model);

  Simulator::Schedule (Seconds (v->GetValue ()), &RandomFunction);

  EventId id = Simulator::Schedule (Seconds (30.0), &CancelledEvent);
  Simulator::Cancel (id);

  Simulator::Run ();

  Simulator::Destroy ();
}
```

## Command line tools

In the program command line is for the gdb debug of the command line tools.


```cpp
CommandLine cmd (__FILE__);
cmd.Parse (argc, argv);
```

## Constructor

My model is a class defined constructor

```cpp
MyModel model;
```

We can see the class MyModel which is defined in namespace

```cpp
/** Simple model object to illustrate event handling. */
class MyModel
{
public:
  /** Start model execution by scheduling a HandleEvent. */
  void Start (void);

private:
  /**
   *  Simple event handler.
   *
   * \param [in] eventValue Event argument.
   */
  void HandleEvent (double eventValue);
};

void
MyModel::Start (void)
{
  Simulator::Schedule (Seconds (10.0),
                       &MyModel::HandleEvent,
                       this, Simulator::Now ().GetSeconds ());
}
void
MyModel::HandleEvent (double value)
{
  std::cout << "Member method received event at "
            << Simulator::Now ().GetSeconds ()
            << "s started at " << value << "s" << std::endl;
}
```

## Initial Object

The model is defined by using smart pointer, the code below will initial the model as a object.

```cpp
Ptr<UniformRandomVariable> v = CreateObject<UniformRandomVariable> ();
```

How can we use this object ? we can check it from the gdb debug tool, remember we use can use the tool to trace down the header we included, attribute is there.

```sh
(base) ➜  ns-3.31 ./waf --run  "sample-simulator --PrintTypeIds"
Registered TypeIds:
.....
    ns3::UniformRandomVariable
....
```

This functionality is not working for only gdb, it works only if you use commandline in your program, only works in ns3.

Here is the example I run with some code, it will print nothing, gdb is a debug tool

```sh
cmake CMakeList.txt
gdb Heap
(gdb) r --help
Starting program: /run/media/geek/04-Heap/Heap/Heap --help
Heap Sort Using Max Heap : 0.35696 s
Heap Sort Using Index Max Heap : 0.752176 s
Heap Sort Using Min Heap : 0.367752 s
Heap Sort Using Index Min Heap : 0.699219 s
[Inferior 1 (process 96271) exited normally]
```

## Pass value to object

We can simply check it by this way, then you know the data type is attributes (random number generator).

```sh
# --PrintAttributes=[typeid] # check (gdb) r --help
./waf --run  "sample-simulator --PrintAttributes=ns3::UniformRandomVariable"
Attributes for TypeId ns3::UniformRandomVariable
    --ns3::UniformRandomVariable::Max=[1]
        The upper bound on the values returned by this RNG stream.
    --ns3::UniformRandomVariable::Min=[0]
        The lower bound on the values returned by this RNG stream.
```

Pass the value to `Min` and `Max`.

```cpp
  v->SetAttribute ("Min", DoubleValue (10));
  v->SetAttribute ("Max", DoubleValue (20));
```

## Start Simulation

The Simulator can be Scheduled, and the Event can be create and cancelled by the Id.

- `Simulator`, `SimulatorImpl`, `Scheduler` class at `Simulator.h`
- at `nstime.h`
    - (int), `Seconds()`, `Minutes()`
    - (double), `MiliSeconds()`, `MicroSeconds()`, `PicoSeconds()`
    - Double time = t.GetSeconds() // set to double
- `EventImpl.EventId` is class defined constructor
- `UniformRandomVariable::GetValue()`

```cpp
  Simulator::Schedule (Seconds (10.0), &ExampleFunction, &model);

  Simulator::Schedule (Seconds (v->GetValue ()), &RandomFunction);

  EventId id = Simulator::Schedule (Seconds (30.0), &CancelledEvent);
  Simulator::Cancel (id);

  Simulator::Run ();

  Simulator::Destroy ();
```

## for more distribution

In the powerpoint page 11, we know it’s not only uniform distribution, we can plot from matplotlib

```sh
pip2 install numpy pandas plotly matplotlib cufflinks
./waf configure --enable-modules='core','network','mobility','propagation' --with-python=python2
./waf
```

`sample-rng-plot`,the random number generator of the ns3

```py
# -*- Mode:Python; -*-
# /*
#  * This program is free software; you can redistribute it and/or modify
#  * it under the terms of the GNU General Public License version 2 as
#  * published by the Free Software Foundation
#  *
#  * This program is distributed in the hope that it will be useful,
#  * but WITHOUT ANY WARRANTY; without even the implied warranty of
#  * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  * GNU General Public License for more details.
#  *
#  * You should have received a copy of the GNU General Public License
#  * along with this program; if not, write to the Free Software
#  * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#  */

## @file
#  @ingroup core-examples
#  @ingroup randomvariable
#  Demonstrate use of ns-3 as a random number generator integrated with
#  plotting tools.
#  
#  This is adapted from Gustavo Carneiro's ns-3 tutorial


import numpy as np
import matplotlib.pyplot as plt
import ns.core

# mu, var = 100, 225
rng = ns.core.NormalRandomVariable()
rng.SetAttribute("Mean", ns.core.DoubleValue(100.0))
rng.SetAttribute("Variance", ns.core.DoubleValue(225.0))
x = [rng.GetValue() for t in range(10000)]

# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)

plt.title('ns-3 histogram')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
```

{{< plotly normal >}}

other example is uniform below

{{< plotly uniform >}}

```py
# mu, var = 100, 225
rng = ns.core.UniformRandomVariable()
rng.SetAttribute("Min", ns.core.DoubleValue(0.0))
rng.SetAttribute("Max", ns.core.DoubleValue(225.0))
x = [rng.GetValue() for t in range(10000)]
```

## add to plotly

```py
import matplotlib.pyplot as plt
fig = plt.figure
#plot things
from plotly.offline.offline import plot_mpl
# plot_mpl(fig, filename='temp-plot.html', auto_open=False) 
# df.plot.get_figure() when use pandas
# setting other property
from plotly.tools import mpl_to_plotly
plotly_fig = mpl_to_plotly(fig)
plotly_fig.update_layout(template="none")
plotly_fig.write_html("temp-plot3.html")
```

Ref
The ns3 2015 training videos and ppts, the videos is available at their official website. [video](https://vimeo.com/showcase/3480129)


{{< officelink "http://www.nsnam.org/tutorials/consortium15/ns-3-training-part2.pptx" >}}

### For more gdb skills

{{< youtube PorfLSr3DDI  >}}
