import socket
import virtualplayer
import clientplayer

class Game:
	#start variable definitions
	I_NumberOfPlayers = 0
	Player = None
	VirtualPlayer = []
	#end variable definitions
	def __init__(self):
		self.Player = clientplayer.CPlayerEgo()		#initialise ''real'' player
		for x in xrange(self.I_NumberOfPlayers):		#initialise p ''virtual players''
			self.VirtualPlayer = self.VirtualPlayer + [virtualplayer.CVirtualPlayer()]
	
	def GetRoundType(self):	#interrogate server to see what kind of round is next
		return -1	#test code - only run normal rounds for now

	def PlayNormalRound(Env,Game):
		pass

	def PlayObligedRound(Env,Game):
		pass
