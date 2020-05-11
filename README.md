# ZkillMonitor
Monitors zkill for killmails and the flashes led when some come in.

This is a simple pice of code that attaches to zkill using a filter flashes a light if kills are made that pass the filter entered. This is used to light up a sweet sculpture.

Targets rasperry pi w zero, this means that for all intents and purposes there is no sound and thus we cannot play a taylor swift song every time. Sorry.

## installing

 

 It requires websockets & asyncio you can install them via pip3.

 Edit the filter.txt file to match the filter you want.  See https://github.com/zKillboard/zKillboard/wiki/Websocket for details

 Edit the service file to use the correct directory. (unless you cloned into the pi user's home directory)

 `chmod +X install.sh`
 `# ./install.sh`


## Running it

If you ran the install script and it did not explode you should have it running in the background as a service. This gets you auto restart when it inevtiably crashes due to zkill disconnecting.

Alternately, if you have screen installed you can use start.sh to run this in the background. That means you could do other stuff with your pi too (if you wanted). 

`./start.sh`

Finally, You can run this as one off.

 `python3 main.py`

