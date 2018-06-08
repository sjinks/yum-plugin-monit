import os

import yum
from yum.plugins import TYPE_CORE

requires_api_version = '2.1'
plugin_type = (TYPE_CORE,)

def pretrans_hook(conduit):
    conduit.info(2, 'Stopping monit')
    command = '/usr/bin/systemctl stop monit.service'
    os.system(command)

def posttrans_hook(conduit):
    conduit.info(2, 'Starting monit')
    command = '/usr/bin/systemctl start monit.service'
    os.system(command)
