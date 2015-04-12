import ConfigParser
import sys, os


DEFAULT_CONFIG_DIR = 'config'

class ConfigManager:

	def __init__(self):
		# Initialize the config parser
	    self.__config = ConfigParser.ConfigParser()
	    # setup config file path
	    scriptPath = os.path.dirname(os.path.realpath(__file__))
	    cfgFile = os.path.join(scriptPath, DEFAULT_CONFIG_DIR, 'config.ini')
	    filesLoaded = self.__config.read(cfgFile)

	def get(self, section, option, isRequired = False, defaultValue = None):
	        try:
	            value = self.__config.get(section,option)
	        except:
	            if (isRequired):
	                raise Exception(option + " is required in the config")
	            else:
	                value = defaultValue

	        return value
		


