#!/usr/bin/python3

# WS client to turn Leds on on a raspberry pi If a specific Eve corp, HABIT, gets a kill.
# https://github.com/zKillboard/zKillboard/wiki/Websocket

import websockets
import asyncio
import ssl
import json
from gpiozero import LED
from time import sleep

# assume pi w zero 
# both of there are 1 off  a ground pin so we can test easily



async def monitorZkill(filter):
	zkill = "wss://zkillboard.com:2096"
	subscriptionRequest = "{\"action\":\"sub\",\"channel\":\""+filter+"\"}"
	

	async with websockets.connect(zkill, ssl=True) as socket:
		await socket.send(subscriptionRequest)
		print("waiting for kills..");
		while True:
			try:
				killdata = await socket.recv();
				await processKill(killdata, filter) 
			except Error as e:
				print(e);
			
async def processKill(kill, filter ):
	print(f" {kill}")

	json_kill = json.loads(kill)
	#expect filter to be like Corp:1234 or alliance:1234
	filter_comps = filter.split(":")
	#are we the killer or the killed?
	try:
		led = None
		on_times = 5
		on_duration = 5
		if json_kill[filter_comps[0]+"_id"] == filter_comps[1]:
			# we got killed
			print (":(");
			led = LED(23)
			on_times = 3
			
		else:
			# we killed someone 
			print (":)");
			led = LED(17)
			on_duration = 3
			
		#flash the light
		count =0;
		while count< on_times:
			bad_led.on();
			sleep(on_duration);
			bad_led.off();
	except:
		print("error flashing leds")


	


def generateFilter():
	filter = "corporation:1941177176"

	try:
		with open("filter.txt", 'r') as filterFile:
			filterfile = filterFile.read()
			if len(filterfile) > 10:
				filter = filterfile
			else:
				Print("Filter File Too short using defaults")
			

	except IOError as error:
		print("Can't Read filter.txt");
		print(error)

	print(filter)
	return filter

print("Starting ZKILL monitor");
	
asyncio.run(monitorZkill(generateFilter()))