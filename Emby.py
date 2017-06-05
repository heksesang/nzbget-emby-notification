#!/usr/bin/env python
#
# Copyright (C) 2017 Gunnar Lilleaasen
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

##############################################################################
### NZBGET POST-PROCESSING SCRIPT                                          ###

# Updates an Emby movie library.
# 
# This is a script for notifying an Emby media server to update the
# movie library with any newly added movies.
#
# NOTE: The script should run after sorting scripts such as VideoSort.

##############################################################################
### OPTIONS                                                                ###

# Host address of the Emby server.
#
#Host=localhost:8096

# API key for Emby.
#
#ApiKey=

### NZBGET POST-PROCESSING SCRIPT                                          ###
##############################################################################

import urllib, urllib2

import sys
import os

# Exit codes used by NZBGet
POSTPROCESS_SUCCESS=93
POSTPROCESS_NONE=95
POSTPROCESS_ERROR=94

host = os.environ['NZBPO_HOST']
apikey = os.environ['NZBPO_APIKEY']

url = 'http://{0}/emby/Library/Movies/Updated'.format(host)

values = {}
data = urllib.urlencode(values)

try:
    req = urllib2.Request(url, data)

    if apikey:
        req.add_header('X-MediaBrowser-Token', apikey)

    response = urllib2.urlopen(req)
    result = response.read()
    response.close()

    print('[INFO] HTTP response: {0}'.format(result.replace('\n', '')))
    sys.exit(POSTPROCESS_SUCCESS)

except (urllib2.URLError, IOError) as e:
    print('[ERROR] Couldn\'t reach Emby at {0}: {1}'.format(url, e))
    sys.exit(POSTPROCESS_ERROR)