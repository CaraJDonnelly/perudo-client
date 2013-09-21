#!/usr/bin/env python
import setup
import gamestate
import playround

Env = setup.CEnv()				#setup environment and process argv string
Game = gamestate.Game(Env, Env.ArgvName)	#connect to server and set up game


while 1:					#obey the server
	NextRoundType = Game.GetRoundType(Env)	#The server will tell us if the next round is an obliged round
	if NextRoundType == 0:			#...play normal round
		Game.PlayNormalRound(Env)
	elif NextRoundType == 1:		#...play obliged round
		Game.PlayObligedRound(Env)
	else:					#Game is finished or error code == -1
		break

#test code
print "Leftover data: \n"
print Game.recvBuffer
while 1:
	data = Game.clientSocket.recv(1024)
	if not data: break
	print data
#end test code	
