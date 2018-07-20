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
import datetime
import sys

HTTPResponses = {
	100: 'Continue',
	101: 'Switching Protocols',

	200: 'OK',
	201: 'Created',
	202: 'Accepted',
	203: 'Non-Authoritative Information',
	204: 'No Content', 
	205: 'Reset Content',
	206: 'Partial Content',

	300: 'Multiple Choices',
	301: 'Moved Permanently',
	302: 'Found',
	303: 'See Other',
	304: 'Not Modified',
	305: 'Use Proxy',	
	307: 'Temporary Redirect',
	
	400: 'Bad Request',
	401: 'Unauthorized',
	402: 'Payment Required',
	403: 'Forbidden',
	404: 'Not Found',
	405: 'Method Not Allowed',
	406: 'Not Acceptable',
	407: 'Proxy Authentication Required',
	408: 'Request Timeout',
	409: 'Conflict',
	410: 'Gone',
	411: 'Length Required',
	412: 'Precondition Failed',
	413: 'Request Entity Too Large',
	414: 'Request-URI Too Long',
	415: 'Unsupported Media Type',
	416: 'Requested Range Not Satisfiable',
	417: 'Expectation Failed',

	500: 'Internal Server Error',
	501: 'Not Implemented',
	502: 'Bad Gateway',
	503: 'Service Unavailable',
	504: 'Gateway Timeout',
	505: 'HTTP Version Not Supported',
}


# This class provide a rappresentation of HTTP Data
class HTTPData:

	# Default Constructor
	def __init__(self):
		self.Reset()
		
	# Initialize the HTTPData with default values
	def Reset(self):
		self.data = ''
		self.agent = 'EmulatorFrontier/0.1 (Python/%d.%d.%d)' % (sys.version_info[0], sys.version_info[1], sys.version_info[2])
		self.code = 200
		self.type = ''
		self.conn = 'Close'
		self.extra = ''
		self.location = '/'
		self.host = '127.0.0.1'
		self.contenttype = 'text/html'
		self.contentcharset = 'utf-8'
		self.phploc = {}
	
	# Set the request to POST
	def POST(self):
		self.type = 'POST'
		
	# Set the request to GET
	def GET(self):
		self.type = 'GET'
		
	# Get the request (if any)
	def GetRequest(self):
		return self.type

	# Check if the HTTPData have a request (aka Client)
	def HaveRequest(self):
		return self.type != ''
	
	# Append a string to be sended
	def AppendData(self, text):
		self.data = self.data + '\n' + text
	
	# Get Data to be sended into HTTP
	def GetData(self):
		return self.data

	# Clear the Data to be sended
	def ClearData(self):
		self.data = ''
		
	# Set Content Type
	def SetContentType(self, text):
		self.contenttype = text

	# Get Content Type
	def GetContentType(self):
		return self.contenttype
		
	# Set Content Charset
	def SetContentCharset(self, text):
		self.contentcharset = text
		
	# Get Content Charset
	def GetContentCharset(self):
		return self.contentcharset

	# Set the User Agent
	def SetAgent(self, text):
		self.agent = text

	# Get the User Agent
	def GetAgent(self):
		return self.agent
		
	# Get the Server information
	def GetServerInfo(self):
		return self.agent

	# Set the Server information
	def SetServerInfo(self, text):
		self.agent = text

	# Set the connection to Close
	def ConnectionClose(self):
		self.conn = 'Close'
				
	# Set the connection to Keep-Alive
	def ConnectionKeepAlive(self):
		self.conn = 'Keep-Alive'

	# Get the connection type
	def GetConnectionType(self):
		return self.conn

	# Set the error code
	def SetError(self, num):
		self.code = num

	# Append Data to extra
	def AppendExtra(self, text):
		self.extra = self.extra + '\n' + text

	# Set host (Where to reply the data)
	def SetHost(self, text):
		self.host = text
	
	# Get current date
	def CurrentDateTime(self):
		return datetime.datetime.now().strftime('%a, %d %b %Y %H:%M:%S %Z')
		
	# Convert the Error code into a String
	def ConvertErrorToString(self, err):
		try:
			return HTTPResponses[err]
		except:
			return 'Unknown'
			
		return 'Unknown'
		
	# Check if the Connection is Keep-Alive
	def IsConnectionKeepAlive(self):
		return self.conn == 'Keep-Alive'
		
	# Convert a String into HTTPData
	def FromString(self, str):
	
		# This function find and trasform a server request
		def ClientFind(self, str):
			returnindex = 0
			index = str.find(' ')
			if index == -1:
				return 0
				
			self.SetLocation(str[0:index])
		
			index = str.find('\n', index)
			
			if index == -1:
				return 0
				
			str = str[index:]
	
			returnindex = index + 1
			
			index = str.find('Host: ')
			
			if index != -1:
				index = index + 6
				index2 = str.find('\n', index)
				returnindex = index2 + 1
				self.SetHost(str[index:index2])
				
			index = str.find('User-Agent: ')
			
			if index != -1:
				index = index + 12
				index2 = str.find('\n', index)
				returnindex = index2 + 1
				self.SetAgent(str[index:index2])
			
			index = str.find('Connection: ')
			if index != -1:
				index = index + 12
				index2 = str.find('\n', index)
				returnindex = index2 + 1
				self.conn = str[index:index2]
				
			return returnindex
			
		
		# This function find and trasform a server request
		def ServerFind(self, str):
			returnindex = 0
			
			index = str.find(' ')
			if index == -1:
				return 0
			
			self.SetError(int(str[:index]))
			
			index = str.find('\n')
			if index == -1:
				return 0
				
			str = str[index:]
			
			returnindex = index + 1
			
			index = str.find('Date: ')
			if index != -1:
				index = index + 6
				index2 = str.find('\n', index)
				returnindex = index2 + 1
				## TODO: Add handling of date string to date time
			
			index = str.find('Connection: ')
			if index != -1:
				index = index + 12
				index2 = str.find('\n', index)
				returnindex = index2 + 1
				self.conn = str[index:index2]
			
			index = str.find('Content-Type: ')
			if index != -1:
				index = index + 14
				index2 = str.find('\n', index2)
				returnindex = index2 + 1
				
				index3 = str.find('charset=', index)
				if index3 == -1:
					self.SetContentType(str[index:index2])
				else:
					self.SetContentType(str[index:index3-2])
					
					index2 = str.find('\n', index3)
					self.SetContentCharset(str[index3:index2])
					
					returnindex = index2 + 1
					
			index = str.find('Server: ')
			if index != -1:
				index = index + 8
				index2 = str.find('\n', index)
				self.SetServerInfo(str[index:index2])
				returnindex = index2 + 1
				
			return returnindex
			
		index = 0
		
		## Find type
		index = str.find(' ', index)
		self.type = str[:index]	
			
		## Switch to find server request or client request
		if self.type == 'HTTP/1.1':
			self.type = ''
			index = ServerFind(self, str[index+1:])
		else:
			index = ClientFind(self, str[index+1:])
			
		## Find data
		index = str.find('\n', index)
		if index == -1:
			index = index + 2
			self.data = str[index:-1]		
		
	# Set the location to be requesting the file/directory
	def SetLocation(self, text):
		index = text.find('?')
		if index == -1:
			self.location = text
			return
			
		self.location = text[:index]
		index = index + 1
		
		## Split '?' arguments
		working = True
		first_text = ''
		second_text = ''
		index2 = 0
		
		while working:
			index2 = text.find('=', index)
			if index2 == -1:
				working = False
			else:
				first_text = text[index:index2]
				index2 = index2 + 1
				
				index = text.find('&', index2)
				if index == -1:
					second_text = text[index2:]
					working = False
				else:
					second_text = text[index2:index]
					
				index = index + 1
				
				self.phploc.update({first_text:second_text})

	# Get the current location
	def GetLocation(self):
		return self.location
		
	# Get the Arguments (?x=y&z=k)
	def GetArguments(self):
		return self.phploc
		
	# Transform this HTTPData into a String
	def ToString(self):
		buffer = ''
		if self.type == '': ### Server
			buffer = ( '''HTTP/1.1 %d %s
Content-Type: %s;charset=%s
Data-Length: %d
Date: %s
Server: %s
Content-Length: %d
Connection: %s'''  % (self.code, self.ConvertErrorToString(self.code),
						self.contenttype, self.contentcharset,
						len(self.data)-1, self.CurrentDateTime(),
						self.agent, len(self.data)-1, self.conn) )
		else: ### Client
			buffer = ( '''%s %s HTTP/1.1
Host: %s
Accept: */*
Accept-Encoding: None
Accept-Language: en
User-Agent: %s
Content-Length: %s
Connection: %s
Content-Type: %s
Expect: 100-continue''' % (self.type, self.location,
				self.host , self.agent, len(self.data)-1,
				self.conn, self.contenttype) )
				
		if self.extra != '':
			buffer = buffer + '\n' + self.extra
		
		buffer = buffer + '\n' + self.data
			
		return buffer
