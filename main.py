#!/usr/bin/env python
import setup
import gamestate
import playround

Env = setup.CEnv()				#setup environment and process argv string
Game = gamestate.Game()				#connect to server and set up game

while 1:					#obey the server
	NextRoundType = Game.GetRoundType()	#The server will tell us if the next round is an obliged round
	if NextRoundType == 0:			#...play normal round
		Game.PlayNormalRound(Env)
	elif NextRoundType == 1:		#...play obliged round
		Game.PlayObligedRound(Env)
	elif NextRoundType == -1:		#Game is finished
		break

