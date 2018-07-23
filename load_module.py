import imp
import sys ## somehow buggy
from urllib.request import urlopen
    
def load_module_from_helper_lib(name):
    modulesource = 'https://raw.githubusercontent.com/CeadeS/helper_lib/master/'+name+'.py'
    sourcestr = urlopen(modulesource).read()
    source_file = "./ProgressBar.py"
    codeobj = compile(sourcestr, source_file, 'exec')
    newmodule = imp.new_module(name)
    exec(codeobj,newmodule.__dict__)
    return newmodule

ProgressBar = load_module_from_helper_lib('ProgressBar')
