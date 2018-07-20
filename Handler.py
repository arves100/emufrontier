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
from http.server import HTTPHandler
from http.data import HTTPData
import Logger
import Features
import Config

class BraveHandler(HTTPHandler):

	def Send404(self):
		http = HTTPData()
		http.AppendData('<h1>404: Not found</h1>')
		http.SetError(404)
		self.client.SendHTTPData(http)
		self.client.Close()
		
	def OnHTTPRead(self, data):
		if data.GetRequest() == 'GET':
			self.DoGET(data)
		elif data.GetRequest() == 'POST':
			self.DoPOST(data)
		else:
			Logger.PrintError('Unknown request %s from %s' % (data.GetRequest(), self.client.GetAddress()))
			self.client.Close()
			
	def DoGET(self, data):
		if data.GetLocation() == '/bf/web/terms.htm':
			Features.SendTerms(self.client)
		elif data.GetLocation() == '/bf/gme/action/Dynamic_background.php':
			http = HTTPData()
			http.AppendData(Features.Base64Crypt(Config.GetWallpaper()))
			http.SetContentType('application/json')
			self.client.SendHTTPData(http)
		
		elif data.GetLocation() == '/shutdown_server':
			if self.client.GetAddress() == '127.0.0.1':
				http = HTTPData()
				http.AppendData('Shutting down...')
				self.client.SendHTTPData(http)
				self.client.Close()
				self.StopServer()
			else:
				self.Send404()
		else:
			Logger.PrintError('Unknown location %s from %s' % (data.GetLocation(), self.client.GetAddress()))
			self.Send404()
		
	def DoPOST(self, data):
		if data.GetLocation() == '/bf/gme/action/Dynamic_background.php':
			http = HTTPData()
			http.AppendData(Features.Base64Crypt(Config.GetWallpaper()))
			http.SetContentType('application/json')
			self.client.SendHTTPData(http)
		else:
			Logger.PrintError('Unknown location %s from %s' % (data.GetLocation(), self.client.GetAddress()))
			self.Send404()
