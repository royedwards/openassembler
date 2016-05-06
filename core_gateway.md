Functions you can access by importing the Gateway/Gateway.py module:

```
from Gateway.Gateway import oas_gateway
```

  * oas\_list(mode,listtype,searchtag)
  * oas\_show(mode,showtype)
  * oas\_count(mode,counttype)
  * oas\_create(mode,nodetype)
  * oas\_delete(mode,deletetype,target)
  * oas\_rename(mode,old,new)
  * oas\_connect(mode,from\_variable,to\_variable)
  * oas\_new(mode)
  * oas\_end(mode,endnode)
  * oas\_save(mode,filename,filetype)
  * oas\_open(mode,filename,filetype)
  * oas\_run(mode)
  * oas\_set(mode,nodevalue,value)
  * oas\_positions(mode,nodevalue,posx,posy)
  * oas\_framerange(mode,firstframe,endframe)
  * oas\_frame(mode,frame)
  * oas\_Start()
  * oas\_server\_chk(port)
  * oas\_ui\_refresh()


mode can be:
  * normal
  * silent

if the mode is normal it will output to the stdout but will not have return value sometimes, if it is silent, than we will have a returnvalue, but no output for stdout. Silent is used for post and inter-software communication.