OpenAssembler have a server mode combined with the most basic console.
I suggest to start with this one, and than later you can open up everything else.

You can start the oas server and console like this:
```
OpenAssembler -m server
```
or
```
python OpenAssembler.py -m server
```

Or you can start it by loading up a file:

```
OpenAssembler -m console -f ~/test.oas
```

then you will get this prompt:
```
OpenAssembler--->
```

After some time (quite soon) you will get a message from the server, like this one:
```
OpenAssembler Server started at 192.168.0.1:23345 !
```


For the commands:
[Normal console](normal.md)