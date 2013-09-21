import socket
import virtualplayer
import clientplayer
import sys

class Game:
	#start variable definitions
	I_NumberOfPlayers = 0
	Player = None
	Str_Name = None
	VirtualPlayer = []
	clientSocket = None
	sendBuffer = None
	recvBuffer = None
	
	#end variable definitions
	def __init__(self, Env, argvName):
		Env.Verbose(3, "Initialising gamestate")
		self.Str_Name = argvName
		Env.Verbose(3, "Connecting to server...")
		
		#set up sockets and connect to server
		try:
			self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.clientSocket.connect(("localhost", 1111))
			self.clientSocket.sendall("PERUDO?\n")
			self.recvBuffer=self.clientSocket.recv(1024)
			if(self.recvBuffer != "PERUDO!\n"):
				Env.Verbose(1,"Unknown server type!  Message received: %s", self.recvBuffer)
				self.clientSocket.close()
				sys.exit()
			else:
				Env.Verbose(3, "Connected!  Sending name %s", self.Str_Name)
				self.sendBuffer = self.Str_Name
				self.clientSocket.send(self.sendBuffer)
		except socket.error:
			Env.Verbose(1, "Could not connect!")
			sys.exit()
		#end set up sockets

		self.Player = clientplayer.CPlayerEgo()		#initialise ''real'' player
		for x in xrange(self.I_NumberOfPlayers):		#initialise p ''virtual players''
			self.VirtualPlayer = self.VirtualPlayer + [virtualplayer.CVirtualPlayer()]
	
	#find a codeword in the buffer, return/delete that entry, leave the rest unchanged
	def ExtractChunk(self,Str_Codeword):
		B_FoundYet = 0
		recvBufferBuffer = ""
		for NextChunk in self.recvBuffer.split("\n"):
			if((Str_Codeword in NextChunk) and (B_FoundYet == 0)):
				FoundChunk = NextChunk
				B_FoundYet = 1
			elif len(NextChunk)>0:
				recvBufferBuffer = recvBufferBuffer + NextChunk + "\n"
		self.recvBuffer = recvBufferBuffer
		if B_FoundYet:
			return FoundChunk
		else:
			return ""
		
		
	def GetRoundType(self, Env):	#interrogate server to see what kind of round is next
		try:
			self.recvBuffer = self.recvBuffer + self.clientSocket.recv(1024)
			Env.Verbose(3, "Current buffer: \"%s\"", self.recvBuffer)
			NextChunk = self.ExtractChunk("ROUND!")
			return int(NextChunk.split()[1]);
		except (socket.error, IndexError):
			Env.Verbose(1,"Warning!  Could not get round type!")
			return -1	#return exit code
		

	def PlayNormalRound(self,Env):
		Env.Verbose(2, "Playing normal round...")
		self.GetCup(Env)
		self.GetActivePlayers(Env)

	def PlayObligedRound(self,Env):
		Env.Verbose(2, "Playing obliged round...")
		self.GetCup(Env)
		self.GetActivePlayers(Env)
	
	def GetCup(self, Env):
		Env.Verbose(3, "Getting cup...")
		try:
			self.recvBuffer = self.recvBuffer + self.clientSocket.recv(1024)
			Env.Verbose(3, "Current buffer: \"%s\"", self.recvBuffer)
			NextChunk = self.ExtractChunk("DICE:")
			self.Player.LI_Hand=[]
			for die in NextChunk.split():
				if not(die =="DICE:"):
					self.Player.LI_Hand += [int(die)]
		except (socket.error, IndexError):
			Env.Verbose(1,"Warning!  Could not get cup!")

	def GetActivePlayers(self,Env)
		Env.Verbose(3, "Getting active players...")
		try:
			self.recvBuffer = self.recvBuffer + self.clientSocket.recv(1024)
			Env.Verbose(3, "Current buffer: \"%s\"", self.recvBuffer)
			NextChunk = self.ExtractChunk("PLAYERS:")
			#read in active players
			#end read in active players
		except (socket.error, IndexError):
			Env.Verbose(1,"Warning!  Could not get cup!")
