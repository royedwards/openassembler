# Create a node #

It is very easy to create a node for OpenAssembler.

All you need to do is to follow a few rule for the script layout.

Well lets start an example:

You want to create a node to handle all the math functions.

You need to start with an identifier line:
```
###OpenAssembler Node python file###
```

Then you need to tell to the interface about your nodes, your inputs your outputs, and some other stuffs.

You need to indicate the name of the node like this:
```
    name multiMath
```
then you need to tag it:
```
   tags anything:something:more
```
and after you need to specify the connection points: first the side: input/output and the variabletype int/float/string/... and then the name like A.. than the default value and at last any option if you want
If you have any space in your value or in your option, you have tu use ""
So here is an example line:
```
   input int A 1 "min=0 max=100"
```

All you need to do is to put all this important informations into a commentblock, and !!this is very important you need to put it into a define{} like this:

```
###OpenAssembler Node python file###

'''
define
{
	name multiMath
	tags oas:math
	input int A 1
	input int B 1
	output int mult 1
	output int add 1
	output int sub 1
	output int div 1
	output int pow 1

}
'''

```

Do not forget to put all this things inside a ''' blablabla ''' marks. This will thee python that it is not relevant for the function.

Ok, then we are ready with the preparation, the real work is starting now.
You have to create a class named the same as your nodename
and you have to define a function called yournodename\_main. It have to implement self, and then all the input variables with a default value (it is important) and a special one at the end called oas\_output.

than the last ting you need to follow is that you will need to have a return value, depending on the output.
That is all.
Here is a working example for the multimath node:
```

###OpenAssembler Node python file###

'''
define
{
	name multiMath
	tags oas:math
	input int A 1
	input int B 1
	output int mult 1
	output int add 1
	output int sub 1
	output int div 1
	output int pow 1

}
'''


class multiMath:
   def multiMath_main(self,A=1, B=1, out=1,oas_output="mult"):

	if oas_output=="mult":
		try:
			return float(A)*float(B)
		except:
			return 0

	elif oas_output=="add":
		try:
			return float(A)+float(B)
		except:
			return 0
			
	elif oas_output=="sub":
		try:
			return float(A)-float(B)
		except:
			return 0	
			
	elif oas_output=="div":
		try:
			return float(A)/float(B)
		except:
			return 0
			
	if oas_output=="pow":
		try:
			return float(A)**float(B)
		except:
			return 0
			
	else:
		return 0


```

Have fun!!!