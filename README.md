PluginLoader
============

A simple plugin loader

Usage
=====

`
from pluginloader import PluginLoader

plugin_path = 'plugins'
plugin_classes = []
for plugin_class in PluginLoader(plugin_path):
    cl = plugin_class()
    plugin_classes.append(cl)
`
