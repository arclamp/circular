import os
from girder.api.rest import Resource
from girder.utility.plugin_utilities import registerPluginWebroot


class Circular(Resource):
    _cp_config = {'tools.staticdir.on': True,
                  'tools.staticdir.index': 'index.html'}

    def __init__(self, info):
        super(Circular, self).__init__()

        self.resourceName = 'circular'
        self.info = info


def load(info):
    print info
    Circular._cp_config['tools.staticdir.dir'] = os.path.join(info['pluginRootDir'], 'web_client')
    registerPluginWebroot(Circular(info), info['name'])
