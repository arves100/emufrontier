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
import asyncore
import socket
import Logger
from client import HTTPClient
from data import HTTPData
import sys

# This class rappresents an HTTP Handler that will requested
#  each time an HTTP Connection has been made
class HTTPHandler(asyncore.dispatcher_with_send):
	# Default constructor with additional addr
	def __init__(self, sock=None, map=None, addr=None):
		asyncore.dispatcher_with_send.__init__(self, sock, map)
		if sock == None or addr == None:
			return # Ignore if the required arguments are None
			
		self.buffer_len = 8192
		self.client = HTTPClient(sock, addr) # Create the client instance
		
	def StopServer(self):
		raise asyncore.ExitNow('')

	# Called when a read has been attempted
	def handle_read(self):
		data = None
		try:
			data = self.recv(self.buffer_len) # Receive data
		except:
			Logger.PrintDebug('Closed connection from %s' % self.client.GetAddress())
			return
			
		if data is None:
			return # Ignore if the data is None
					
		self.internal_read(data)
		
	# Internal read function called when a packet is readed
	def internal_read(self, read):
		if len(read) < 1: 
			return # Ignore EOF/Null packets
		
		Logger.PrintDebug('Received %s from %s' % (str(read), self.client.GetAddress()) )

		# Create data instance
		httpdata = HTTPData()
		httpdata.FromString(read)
		
		if not httpdata.HaveRequest():
			return # Ignore if this is a Server request
			
		# Call the implementable function
		self.OnHTTPRead(httpdata)
		
		# Close the connection if the client is not requesting Keep-Alive
		if not httpdata.IsConnectionKeepAlive():
			self.client.Close()
		
	# This OVERWRITABLE function is called each time an HTTP request has been performed
	def OnHTTPRead(self, data):
		if (data.GetRequest() == 'GET') and (data.GetLocation() == '/'):
			returndata = HTTPData()
			returndata.AppendData('<h1 style="color:red">It Works!</h1>')
			self.client.SendHTTPData(returndata)
		elif (data.GetRequest() == 'GET') and (data.GetLocation() == '/stop_server'):
			returndata = HTTPData()
			returndata.AppendData('<h1>Bye bye!</h1')
			self.client.SendHTTPData(returndata)
			self.StopServer()
		else:
			returndata = HTTPData()
			returndata.SetError(404)
			returndata.AppendData('<h1>ERROR 404: NOT FOUND</h1>')
			self.client.SendHTTPData(returndata)
		
		

# This class rappresents an HTTP Server
class HTTPServer(asyncore.dispatcher):
	# Default constructor
	def __init__(self):
		self.handler = HTTPHandler
		
		# Initialize base class
		asyncore.dispatcher.__init__(self)
		
	# Set a custom handler that will be used to process HTTP data
	def SetHandler(self, handler):
		self.handler = handler

	# Bind to server to the specified host and port
	def Bind(self, host, port):
		try:
			# Create the socket
			self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
			self.set_reuse_addr()
		
			# Bind the socket
			self.bind((host, port))
		
			# Listen the socket
			self.listen(5)
		except:
			Logger.PrintError('Error while binding: %s' % sys.exc_info()[0])
			return False
			
		Logger.PrintInfo('Started EmulatorFrontier Server at %s:%d' % (host, port))
		return True
	
	# Loop the asyncore server
	def Loop(self):
		try:
			asyncore.loop()
		except asyncore.ExitNow:
			Logger.PrintInfo('Shutting down...')
		except:
			Logger.PrintError('Fatal error on loop: %s' % sys.exc_info()[0])
		
	# Handle when a client attemps to connect into the Server
	def handle_accept(self):
		# Trying to accept a Client
		pair = self.accept()
		if pair is None:
			return
			
		sock, addr = pair
		Logger.PrintInfo('Incoming connection from %s' % addr[0])
		
		# Send the request to the handler
		self.handler(sock, None, addr)