import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckanext.testext.interfaces import testinterface
# from ckanext.testext.controller import TestController
from ckan.controllers.package import PackageController
from ckan.lib.base import BaseController


class TestextPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IRoutes, inherit=True)
    
    # IConfigurer

    def update_config(self, config_):
    	print("update_config")
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'testext')


    ## IRoutes
    def before_map(self, map):
    	print("-------TestextPlugin.before_map------")
    	map.connect('test_controller_function', '/test_controller_function',
    		controller='ckanext.testext.controller:TestController',
    		action='test_controller_function')
    	# Our new custom mapping.
        map.connect('/dataset/{id}',
                controller='ckanext.testext.plugin:TestPackageController',
                action='read',
                )

    	return map

    def color_hello(self):
    	
    	print(testinterface().test_interface_function())
    	# print(TestController().test_controller_function())

    	# print("test")

    	return "Hello World I am color"



class TestPackageController(BaseController):

    def read(self, id):
    	print("test")
        return 'foobar'