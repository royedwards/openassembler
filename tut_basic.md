## Basic OpenAssembler v2 tutorial ##

I hope the install vas sucesfull, you downloaded the files extract them, edited and copied the ini file to the ~/.OpenAssembler folder. If so, and you have all the requirements than you can run oas.

So,

Lets start oas with the following command (I guess you are in the oas folder)

```
python OpenAssembler.py -m console
```

Fingers crossed XXXX and..

You have to see something similar:
```
OpenAssembler--->
OpenAssembler Server started at 192.168.0.1:23345 !

```

If you see the same, well this is something like positive start.

Press a few enter, to get a clean prompt, like this:
```
OpenAssembler--->
```

Well, first of all, we need to know what type of nodes you have.

For the complete command reference, check the [console](console.md) page.

So,

```
ln
```

You will see something liek this.

```
OpenAssembler--->
OpenAssembler--->
OpenAssembler--->ln

printer
DualColor_Test
TXT_FileOut
TXT_In
multiMath
TXT_Combine
TXT_FileIn
TXT_Replace
mult
OutputCollector

OpenAssembler--->
```

This means you have this nodes installed, so you can start to combine them.

At this exmaple we will use the mult and the multiMath node.

If oyu are not so sure about the structure of this nodes, you can type:
```
show mult
```

And the result is:

```
OpenAssembler--->show mult

Name of the node: mult
This node is a nodetype template node!
Path to the sourcefile: /net/homes/lmates/OpenAssembler/OpenNodes/mult.py
Inputs:
        A = 1
        B = 1
Outputs:
        out = 1

OpenAssembler--->
```
You can see now, that we have just 1 output and 2 input named A and B. The multiMath node looks like this:
```
OpenAssembler--->show multiMath

Name of the node: multiMath
This node is a nodetype template node!
Path to the sourcefile: /net/homes/lmates/OpenAssembler/OpenNodes/multiMath.py
Inputs:
        A = 1
        B = 1
Outputs:
        pow = 1
        add = 1
        div = 1
        sub = 1
        mult = 1

OpenAssembler---> 
```

You can see that there is much more output for this one.

Well lets create a node:
```
cr mult
```

And you will see the node created:

```
OpenAssembler--->cr mult
Node mult695790 created.
OpenAssembler---> 
```
This means you created a node named mult695790 and the type is a mult. (sorry about the long initial names, I will change it later, just It is needed for debugging now)

Just to doublecheck:
```
ls
```

```
OpenAssembler--->ls

mult695790

OpenAssembler---> 
```

Yep, we have this node in the scene.

Now we can rename this node, by the command:

```
rename mult695790 mult_01
```

```
OpenAssembler--->rename mult695790 mult_01
Node mult695790 is known as mult_01 now.
OpenAssembler---> 
```

Lest create a few more node:
```
OpenAssembler--->rename mult695790 mult_01
Node mult695790 is known as mult_01 now.
OpenAssembler--->
OpenAssembler--->
OpenAssembler--->
OpenAssembler--->cr mult
Node mult604765 created.
OpenAssembler--->cr multiMath
Node multiMath500884 created.
OpenAssembler--->rename mult604765 mult_02
Node mult604765 is known as mult_02 now.
OpenAssembler--->rename multiMath500884 multi_01
Node multiMath500884 is known as multi_01 now.
OpenAssembler--->cr printer
Node printer264754 created.
OpenAssembler--->rename printer264754 printer_01
Node printer264754 is known as printer_01 now.
OpenAssembler--->  
```

Now we ahve seweral nodes in the scene:
```
OpenAssembler--->ls

mult_02
multi_01
mult_01
printer_01

OpenAssembler--->
```

Btw, the printer node is a node to print values to the console. :)

If we are ready with this, we can start to connect them.

First connect the 2 mult into the multimath and the multi to the printer.

```
OpenAssembler--->cn mult_01.out multi_01.A
OpenAssembler--->cn mult_02.out multi_01.B
OpenAssembler--->cn multi_01.add printer_01.A
OpenAssembler--->
```

If you type:
```
lc
```

You will get the list of the connections:

```
OpenAssembler--->lc

Connection754333
Connection465509
Connection600641

OpenAssembler--->
```

And you can check a connection if you want, by:

```
OpenAssembler--->show Connection754333

mult_01.out --> multi_01.A

OpenAssembler--->
```

If you vant to run the network later (yeh, thats the aim I guess) than you need to mark a node as an end-node. This is needed to pars to the run, where to start. And it is wise to set the framerange and the current frame as well.

```
OpenAssembler--->end printer_01
Node printer_01 marked as endnode.
OpenAssembler--->framerange 1 10
Frame range are set.
OpenAssembler--->frame 1
Frame range are set.
OpenAssembler--->
```

I just realised, that the set frame comamnd is wrong... :D and showing the same result as the framerange command. (but it is doing what it have to...)

We can check now the settings if we want:
```
OpenAssembler--->show setup

endnode = printer_01
startframe = 1
frame = 1
endframe = 10

OpenAssembler---> 
```

Now we can set some values.
```
OpenAssembler--->set mult_01.A 2
OpenAssembler--->set mult_01.B 4
OpenAssembler--->set mult_02.A 6
OpenAssembler--->set mult_02.B 8
OpenAssembler---> 
```

It is nice, and now my favourite part comes: you can set expressinons as a value, like this, which will take the current frame number as an input:
```
set mult_02.A =oas_current_frame
```

If we check now our nodes now:
```
OpenAssembler--->show mult_01

ID of the node: Node965456
Name of the node: mult_01
This node is a scene node!
Inputs:
        A = =oas_current_frame
        B = 4
Outputs:
        out = 1

OpenAssembler--->show multi_01

ID of the node: Node114687
Name of the node: multi_01
This node is a scene node!
Inputs:
        A = 1   Connected
        B = 1   Connected
Outputs:
        pow = 1
        add = 1
        div = 1
        mult = 1
        sub = 1

OpenAssembler---> 
```

You can see the connections, and the important settings as well.
So the only thing to do is to save the scene:
```
OpenAssembler--->save /home/user/tutorial_example.oas oas
File saved.
OpenAssembler--->
```
and, to run it!!!!!!!!!!!!!!!:

```
OpenAssembler--->run
OpenAssembler--->
52.0
56.0
60.0
64.0
68.0
72.0
76.0
80.0
84.0
88.0

OpenAssembler---> 
```


Very good!!!!!!!!! Yes!!!!!!!!!!!!!!!

Have fun!