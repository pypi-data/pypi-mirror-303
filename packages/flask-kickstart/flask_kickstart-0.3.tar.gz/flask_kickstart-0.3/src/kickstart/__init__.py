from kickstart.project import Project
import json
import argparse
import os
import importlib.resources

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--settings', help='Settings file')
    args = parser.parse_args()
    

    try:
        if args.settings == None:
            print("Using the default 'settings' file. Use '--settings jsonfile' to change the default configuration")
            file_name = 'kickstart/config/settings.json'
            with importlib.resources.open_text("kickstart.config", "settings.json") as file:
                settings = json.load(file)  
        else:
            file_name = args.settings
        
            with open( file_name ) as user_file:
                file_contents = user_file.read()
            settings = json.loads(file_contents)
    
    except Exception as e:
        print(f"An error occurred: {e}")

    print("Configuration used ->")
    print(settings)

    output_dir = os.path.abspath(settings["outputFolder"])
    proj = Project(settings["project"]["name"],
                    settings["project"]["author"],
                    settings["project"]["description"] ,
                    output_dir)
    
    #proj.setOutputFolder( settings["outputFolder"])
    proj.addBlueprints( settings["project"]["blueprints"] )
    proj.generate()

