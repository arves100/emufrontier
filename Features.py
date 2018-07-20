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
from http.data import HTTPData
import Config
import base64
from Crypto.Cipher import AES

def ParsePage(name):
	fp = open(name, 'r')
	lines = fp.readlines()
	fp.close()
	finalstr = ''
	
	for line in lines:
		finalstr = finalstr +  line
		
	return finalstr
	
def SendTerms(client):
	data = HTTPData()
	data.AppendData(ParsePage(Config.GetTermsPage()))
	client.SendHTTPData(data)
	
def Base64Crypt(data):
	return base64.b64encode(data)

def Base64Decrypt(data):
	return base64.b64decode(data)
	
def AESDecrypt(key, data):
	cipher = AES.new(data.ljust(16, '\x00'))
	return cipher.decrypt(data)
	
def AESCrypt(key, data):
	cipher = AES.new(data.ljust(16, '\x00'))
	return cipher.encrypt(data)
	
def PKCS5Pad(data):
	return s + (32 - len(s) % 32) * chr(32 - len(s) % 32)
	
def PKCS5Unpad(data):
	return s[:-ord(s[-1])]
