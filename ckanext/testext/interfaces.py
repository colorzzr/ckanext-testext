import ckan.plugins.interfaces as p

class testinterface(p.Interface):
	def test_interface_function(slef):
		print("test_interface_function")
		return "hello, this is test Interface"
		