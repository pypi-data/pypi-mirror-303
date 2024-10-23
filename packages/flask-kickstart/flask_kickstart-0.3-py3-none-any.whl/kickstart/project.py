

from kickstart.blueprint import Blueprint
from kickstart.application import Application
from kickstart.hatcher import Hatcher


class Project(Hatcher):
    def __init__(self, project_name, author, description, folder):
        super().__init__( folder + '/' + project_name)
        self.name = project_name
        self.author = author
        self.description = description
        
        self.application = Application( self.folder)
        #self.application.addBlueprint('main')

    def generate(self):
        print('Generating code for ' + self.name )
        folderName = self.folder
      
        self.makeFolder(folderName)
        self.generateFile('readme.tmpl', self.folder, 'README.md', projectName=self.name, description=self.description, author=self.author)
        self.generateFile('run.tmpl', self.folder, 'run.py')
        self.application.generate()
    def setOutputFolder(self, folder):
        self._outputFolder = folder
        
    def addBlueprints(self, blueprints):
        for blueprint in blueprints:
            self.application.addBlueprint(blueprint)