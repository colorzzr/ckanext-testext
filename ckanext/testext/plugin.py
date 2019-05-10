import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckanext.testext.interfaces import testinterface
# from ckanext.testext.controller import TestController
from ckan.controllers.package import PackageController
from ckan.lib.base import BaseController
import ckan.model as model

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
	# All the attribute in model
	# ['rating', 'ResourceRevision', 'OrderedDict', 'SQLAlchemySession', 'revision_table', 'group_extra', 
	# 'engine_is_pg', 'engine_is_sqlite', 'system_info_revision_table', 'MemberRevision', 'Revision', 'package_tag_table', 
	# 'group', 'package_revision_table', 'system_info', 'PackageExtra', 'PackageTag', 'MAX_TAG_LENGTH', 'activity_detail_table', 
	# 'GroupExtraRevision', 'misc', 'TaskStatus', 'repo', 'package_relationship', 'SystemInfoRevision', 'datetime', 'Rating', 
	# 'resource', 'DictProxy', 'member_revision_table', 'Tag', 'DomainObject', 'activity', 'VOCABULARY_NAME_MIN_LENGTH', 'PackageRelationship', 
	# 'vdm', 'is_id', 'PACKAGE_NAME_MAX_LENGTH', 'System', 'State', 'meta', 'MIN_TAG_LENGTH', 'group_table', 'PACKAGE_NAME_MIN_LENGTH', 
	# 'warnings', 'package_table', 're', 'dashboard', 'core', 'MAX_RATING', 'init_model', 'package_relationship_revision_table', 
	# 'DomainObjectOperation', 'get_system_info', 'logging', 'Repository', 'license', 'package', 'delete_system_info', 'TrackingSummary', 
	# 'set_system_info', 'extra_revision_table', 'Session', 'task_status', 'MIN_RATING', 'Group', 'version_table', 'Member', 'follower', 
	# 'PACKAGE_VERSION_MAX_LENGTH', 'VOCABULARY_NAME_MAX_LENGTH', 'GroupRevision', 'task_status_table', 'ckan', 'log', 'Vocabulary', 
	# 'resource_view', 'UserFollowingGroup', 'User', 'package_extra', 'revision_as_dict', 'text_type', 'domain_object', 'user_table', 
	# 'Dashboard', 'tracking_summary_table', 'resource_view_table', 'extension', 'package_extra_table', 'UserFollowingUser', 'term_translation_table', 
	# 'ResourceView', 'PackageTagRevision', 'group_revision_table', 'group_extra_table', 'SystemInfo', 'PackageExtraRevision', 
	# 'package_relationship_table', 'tag', 'tracking_raw_table', 'resource_revision_table', 'modification', 'sqav', 'ActivityDetail', 
	# 'MetaData', 'Resource', 'vocabulary', 'Package', 'term_translation', 'member_table', 'package_tag_revision_table', 'user', 'Activity', 
	# 'PackageRevision', 'types', 'activity_table', 'system_info_table', 'tracking', 'tag_table', 'GroupExtra', 'resource_table', 'Table', 
	# 'UserFollowingDataset']
    def read(self, id):
    	test = [x for x in model.user.datetime.time.__dict__.keys() if not x.startswith('_')]
    	# print([x for x in model.user.datetime.__dict__.keys() if not x.startswith('_')])
    	print(model.user.datetime.time)
    	print(test)
        return 'foobar'