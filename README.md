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

Another Plugin Blueprint
========================

### files/folders:

```
pluginloader.py
main.py
pluginblueprint.py
plugins
       \plugin1
               \__init__.py
       \plugin2
               \__init__.py
```

### main.py:

```python
from pluginloader import PluginLoader
from pluginblueprint import MyPluginBlueprint

plugin_path = 'plugins'
plugin_classes = []
for plugin_class in PluginLoader(plugin_path, MyPluginBlueprint):
    cl = plugin_class()
    plugin_classes.append(cl)
```
