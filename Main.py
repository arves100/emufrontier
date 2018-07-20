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
from http.server import HTTPServer
from Handler import BraveHandler
import Config
import Logger
# Application Entry point
def app_main():
	Logger.PrintInfo('Starting EmulatorFrontier...')
	
	# Create a Server instance and bind it
	server = HTTPServer()
	server.SetHandler(BraveHandler)
	if server.Bind(Config.GetBindIP(), Config.GetBindPort()) == False:
		return # Exit is we cannot bind the server
	
	# Loop the server
	server.Loop()
		
# Execute this code if we are launching the application
if __name__ == "__main__":
	app_main()

	