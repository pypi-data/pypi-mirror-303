import json, os, requests
from apps_support.others_modules.os_ver import os_version
OS_VERSION = f'{os_version.major()}.{os_version.minor()}.{os_version.mini()}'
apps = []

class commands:
    def install(self, path_to_file:str=None) -> str:
        global config_file_data, filecontent, execfile
        if path_to_file is None:
            raise FileNotFoundError
        # exit(-1)
        with open(path_to_file, 'r') as file:
            config_file_data = json.load(file)

        filecontent = requests.get(config_file_data['download_link'], params=None)
        execfile = config_file_data['exec_name']
        if filecontent.status_code == 200:
            with open(execfile, '+ab') as file:
                file.write(filecontent)
        else:
            raise ConnectionError
            # exit(-1)
        
        appname, nonetype = other_commands.varsplit(execfile)
        apps.append(appname)
        return execfile

    def remove(self=None, app_name:str=None):
        if app_name is None:
            raise ValueError
        if app_name not in apps:
            raise LookupError
        removing_app_exec = f'{app_name}.exe'
        os.remove(f'apps/{removing_app_exec}')
        apps.remove(app_name)
    def list_return(self):
        return apps
    def delete_all(self):
        for count in apps:
            commands.remove(count)
    def printlist(self):
        for count in commands.list_return():
            print(count)

class others:
    def inputwithreturnyes(promt:any):
        yes = input(promt)
        return yes
    def varsplit(var:str, separator:str='.'):
        return var.split(separator, 1)


app_commands = commands()
other_commands = others()
