import importlib
import os

class PluginLoader:

    def __init__(self, path, plugin_blueprint=None):
        if not plugin_blueprint:
            plugin_blueprint = Plugin
        self.plugin_blueprint = plugin_blueprint
        self.path = path
        self.classes = []
        self.modules = []
        self.path_module = {}
        self.load_plugins()

    def __iter__(self):
        for cl in self.classes:
            yield cl

    def find_plugins(self):
        module_paths = []
        for (dirpath, dirs, files) in os.walk(self.path):
            if not len(files) <= 0 and any(f.endswith('.py') for f in files):
                module_paths.append(dirpath.replace('\\', '.'))
        return module_paths

    def load_plugins(self):
        module_paths = self.find_plugins()
        for path in module_paths:
            module = importlib.import_module(path)
            self.modules.append(module)
            self.path_module[path] = module
        self.update_classes()

    def update_classes(self):
        self.classes = self.plugin_blueprint.__subclasses__()

    def get_module(self, cl):
        classes_modules = dict(zip(self.classes, self.modules))
        if cl in classes_modules:
            return classes_modules[cl]
        else:
            raise NameError('Invalid class!')

class Plugin:
    pass