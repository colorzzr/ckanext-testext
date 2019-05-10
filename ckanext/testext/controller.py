import ckan.plugins as p

class TestController(p.toolkit.BaseController):
	def test_controller_function(self):
		print("test_controller_function says hey")
		return "test_controller_function says hey"
