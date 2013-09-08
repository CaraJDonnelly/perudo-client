import sys					#access the system variables

class CEnv:
						#start list of flags
	I_Verbose=0				#verbosity
						#verbose? = 1		Print round results etc.
						#very verbose? = 2	Print bids
						#very very verbose? = 3	Print all function calls
						#end list of flags
						
	I_NumberOfPlayers=None				#number of players
						
							#begin function definitions
	
	def __init__(self):
		
		if "-h" in sys.argv or "?" in sys.argv:
			print "A simple client application for Perudo.  Options: \n\
				-v\tVerbose.  Print round results etc.\n\
				-vv\tVery verbose.  Print round results etc.\n\
				-vvv\tVery very verbose.  Print all function calls\n\
				-h\tPrint this help and exit\n"
			return None

											#Check for verbose level, always take maximum
		if "-v" in sys.argv:
			self.I_Verbose = 1
		if "-vv" in sys.argv:
			self.I_Verbose = 2
		if "-vvv" in sys.argv:
			self.I_Verbose = 3
	
		

	def Verbose(self,I_Verbosity,Str_Print, *PrintfArguments):			#Selective printing based on verbosity
			
		if I_Verbosity <= self.I_Verbose:
			print Str_Print%(PrintfArguments)
			sys.stdout.flush()
	


						#end function definitions
