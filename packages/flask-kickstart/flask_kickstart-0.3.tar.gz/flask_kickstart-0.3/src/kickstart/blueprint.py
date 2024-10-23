

from kickstart.hatcher import Hatcher


class Blueprint(Hatcher):
    
    def __init__(self, folder: str, name: str):
        super().__init__(folder + '/' + name)
        self.name = name
      

    def generate(self):
        self.createPackage(create_init=False)
        self.generateFile('bp_init.tmpl', self.folder, '__init__.py', bp_name=self.name)
        self.generateFile('routes.tmpl', self.folder, 'routes.py', bp_name=self.name)