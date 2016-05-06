### set <node.input> 

&lt;value&gt;

 ###

You can set a value for a node. If the value is not matchable to ist type (you want to set "shdghbsdf" as a float) than it will be set to the default value. (in this case 0.000)
You can set [expressions](expressions.md) for the values, in that case you need to start your value with "=".

You can check the [expressions](expressions.md) wiki.

Example:
```
set mult_01.A 123
```