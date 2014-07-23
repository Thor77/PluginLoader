PluginLoader
============

A simple plugin loader

Usage
=====

### files/folders:

```
pluginloader.py
main.py
plugins
       \plugin1
               \__init__.py
       \plugin2
               \__init__.py
```

### main.py:

```python
from pluginloader import PluginLoader

plugin_path = 'plugins'
plugin_classes = []
for plugin_class in PluginLoader(plugin_path):
    cl = plugin_class()
    plugin_classes.append(cl)
```
