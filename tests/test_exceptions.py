# Tests for SecretStorage
# Author: Dmitry Shachnev, 2013
# License: BSD

# Various exception tests

import unittest
import secretstorage
from secretstorage.exceptions import ItemNotFoundException

class ExceptionsTest(unittest.TestCase):
	"""A test case that ensures that all SecretStorage exceptions
	are raised correctly."""

	def setUp(self):
		self.bus = secretstorage.dbus_init(main_loop=False)
		self.collection = secretstorage.Collection(self.bus)

	def test_double_deleting(self):
		item = self.collection.create_item('MyItem',
			{'application': 'secretstorage-test'}, b'pa$$word')
		item.delete()
		self.assertRaises(ItemNotFoundException, item.delete)

	def test_non_existing_item(self):
		self.assertRaises(ItemNotFoundException, secretstorage.Item,
			self.bus, '/not/existing/path')

if __name__ == '__main__':
	unittest.main()