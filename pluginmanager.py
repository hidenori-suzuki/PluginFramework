#!/usr/bin/env python

import sys
import os

class Plugin(object):
    pass

class PluginManager():

    def __init__(self, args={}):
        self.plugin_dir = os.path.dirname(__file__) + '/plugins/'
        self.plugins = {}
        self._loadPlugins()
        self._registerPlugins(**args)

    def _loadPlugins(self):
        sys.path.append(self.plugin_dir)
        plugin_files = [fn for fn in os.listdir(self.plugin_dir) if fn.startswith('plugin_') and fn.endswith('.py')]
        plugin_modules = [m.split('.')[0] for m in plugin_files]
        for module in plugin_modules:
            m = __import__(module)

    def _registerPlugins(self, **kwargs):
        for plugin in Plugin.__subclasses__():
            obj = plugin(**kwargs)
            self.plugins[obj] = obj.pluginId if hasattr(obj, 'pluginId') else []

    def method(self, method, args={}, target=[]):
        for plugin in self.plugins:
            if not target or (set(target) & set(self.plugins[plugin])):
                try:
                    getattr(plugin, method)(**args)
                except:
                    pass

