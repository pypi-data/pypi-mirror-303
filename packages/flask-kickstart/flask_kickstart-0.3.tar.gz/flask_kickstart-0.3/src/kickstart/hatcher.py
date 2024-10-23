import os
import errno
from jinja2 import FileSystemLoader, Environment, PackageLoader, select_autoescape

#templateLoader = FileSystemLoader(searchpath="./kickstart/templates")
templateLoader = PackageLoader("kickstart")
ENV = Environment(
    loader= templateLoader,
    autoescape=select_autoescape()
)


class Hatcher:
    def __init__(self, folder):
        #self.projectName = project_name
        self.folder = folder
        print (self.folder)
    
    def createFolder_old(self, folderName, mode=755):
        try:
            os.makedirs(folderName, mode, True)
        except OSError as e:
            if e.errno != errno.EEXIST or not os.path.isdir(folderName):
                raise

    def _buildPath(self, path):
        fullpath = path
        return os.sep.join (fullpath.split('/'))
    
    def makeFolder(self, folder, mode=755):
        path = self._buildPath(folder)
        try:
            os.makedirs(path, mode, True)
        except OSError as e:
            if e.errno!= errno.EEXIST or not os.path.isdir(path):
                raise

    def createPackage(self, create_init: True):
        
        self.makeFolder(self.folder)
        if (create_init is True):
            with open(self._buildPath(self.folder + '/__init__.py'), 'a') as f:
                f.write("")

        
    def generateFile(self, template_jnj, output_folder, output_file, **variables):
        file_path = self._buildPath(output_folder + '/' +output_file)
        template = ENV.get_template(template_jnj)
        output   = template.render(variables)
        with open(file_path, 'w') as f:
            f.write(output)