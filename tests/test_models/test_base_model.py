import unittest
import models
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_creation(self):
        """Test if BaseModel instances are created successfully"""
        base_model = BaseModel()
        self.assertIsInstance(base_model, BaseModel)
        self.assertTrue(hasattr(base_model, 'id'))
        self.assertTrue(hasattr(base_model, 'created_at'))
        self.assertTrue(hasattr(base_model, 'updated_at'))

    def test_id_uniqueness(self):
        """Test if the generated IDs are unique"""
        base_model1 = BaseModel()
        base_model2 = BaseModel()
        self.assertNotEqual(base_model1.id, base_model2.id)

    def test_save_method(self):
        """Test if the save method updates the updated_at attribute"""
        base_model = BaseModel()
        original_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(original_updated_at, base_model.updated_at)

    def test_to_dict_method(self):
        """Test if the to_dict method returns the expected dictionary"""
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()

        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        for key in expected_keys:
            self.assertIn(key, base_model_dict)

        self.assertEqual(base_model_dict['__class__'], 'BaseModel')

    def test_str_method(self):
        """Test if the __str__ method returns the expected string representation"""
        base_model = BaseModel()
        expected_str = f"BaseModel ({base_model.id}) {base_model.__dict__}"
        self.assertEqual(str(base_model), expected_str)

if __name__ == '__main__':
    unittest.main()
