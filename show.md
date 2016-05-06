### show 

&lt;what&gt;

 ###
This command will show you several different thihng. You cna use it for the followings:
  1. 

&lt;nodetype&gt;

**get the default settings on a nodetype element
  1.**

&lt;nodename&gt;

**get the settings on a node
  1.**

<connection\_id>

**get the settings on a connection
  1.**endnode**check the endnode
  1.**framerange**check the framerange
  1.**frame**check the current frame
  1.**setup**get the scene settings**

Examples:
for nodetype:
```
show mult
```
and the answer is:
```
Name of the node: mult
This node is a nodetype template node!
Path to the sourcefile: /net/homes/lmates/OpenAssembler/OpenNodes/mult.py
Inputs:
        A = 1
        B = 1
Outputs:
        out = 1
```
so, you get important informations on the nodetype, like the path to the node-description...

If you use this command on a node in the scene, it become someting different a little:
```
show mult_01
```
and the answer:
```
ID of the node: Node260052
Name of the node: mult_01
This node is a scene node!
Inputs:
        A = =oas_current_frame
        B = 2
Outputs:
        out = 1
```
By this command you can get the unique id of the node aswell.

```
show setup
```
will give you back the settings of the scene:
```
endnode = printer_01
startframe = 1
frame = 100
endframe = 15
```
Or for connections:
```
show Connection899775
```
and the answer is:
```
m_01.add --> printer_01.A
```

and so on...