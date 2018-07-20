#
#    EmulatorFrontier Ptototype Server
#    Copyright (C) 2018 Arves100
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
from data import HTTPData
import Logger
import socket

# This class rappresents a HTTP Client
class HTTPClient:

	# Default constructor with address and socket
	def __init__(self, sock, addr):
		self.sock = sock
		self.addr = addr
	
	# Send an HTTP Data to the socket
	def SendHTTPData(self, data):
		self.Send(data.ToString())

	# Send buffer to the socket
	def Send(self, data):
		Logger.PrintDebug("Sending %s from %s" % (str(data), self.GetAddress()) )
		
		try:
			self.sock.send(data)
		except:
			return
			
	# Get the current address
	def GetAddress(self):
		return self.addr[0]

	# Get the current socket
	def GetSocket(self):
		return self.sock
		
	# Close the socket
	def Close(self):
		self.sock.shutdown(socket.SHUT_RDWR)

