The client mode is very similar to the console mode but you can access any OpenAssembler server on any machine

You can start the oas client like this:
```
OpenAssembler -m client
```
or
```
python OpenAssembler.py -m client
```

This will connect you to the localmachine's default port-oas-server.

Or you can connect to any machine by this command: (!!!! This is not working jet !!!!!!!!)

```
OpenAssembler -m client 192.168.0.1:23345
or
OpenAssembler -m client mymachine:23345
or
OpenAssembler -m client 192.168.0.1
or
OpenAssembler -m client 23345
```

then you will get this prompt (this is different a littlebit from the simple console prompt):
```
OpenAssembler:
```

## Client commands ##

You cna use the same commands as for the console. The only difference is that your **answers will be a littlebit different**. This is with the reason to able to parse the ansers simply.

For the commands, please check the [console](console.md) wiki.