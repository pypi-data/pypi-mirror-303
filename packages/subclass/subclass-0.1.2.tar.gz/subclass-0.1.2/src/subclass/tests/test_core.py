import unittest

from subclass.core import subclass

__all__ = ["TestSubclassDecorator"]


# Unit test class
class TestSubclassDecorator(unittest.TestCase):

    def test_subclass_creates_new_class(self):
        """Test that the subclass decorator creates a new class."""

        # Define a dummy class
        class MyClass:
            pass

        # Apply the decorator
        NewClass = subclass(MyClass)

        # Test that a new class is created
        self.assertTrue(
            isinstance(NewClass, type), "The subclass decorator did not return a class."
        )

    def test_subclass_class_name(self):
        """Test that the new class has the same name as the original."""

        # Define a dummy class
        class MyClass:
            pass

        # Apply the decorator
        NewClass = subclass(MyClass)

        # Test that the new class has the same name
        self.assertEqual(
            NewClass.__name__,
            "MyClass",
            "The new class does not have the correct name.",
        )

    def test_subclass_metaclass(self):
        """Test that the new class has the same metaclass as the original."""

        # Define a dummy class with a specific metaclass
        class Meta(type):
            pass

        class MyClass(metaclass=Meta):
            pass

        # Apply the decorator
        NewClass = subclass(MyClass)

        # Test that the new class is of the same metaclass
        self.assertEqual(
            type(NewClass),
            Meta,
            "The new class does not have the same metaclass as the original.",
        )

    def test_subclass_no_methods_or_attributes(self):
        """Test that the new class does not inherit any methods or attributes from the original."""

        # Define a class with methods and attributes
        class MyClass:
            def my_method(self):
                return "Hello"

            my_attribute = 42

        # Apply the decorator
        NewClass = subclass(MyClass)

        # Test that the new class does not have the method or attribute
        self.assertFalse(
            hasattr(NewClass, "my_method"), "The new class should not inherit methods."
        )
        self.assertFalse(
            hasattr(NewClass, "my_attribute"),
            "The new class should not inherit attributes.",
        )

    def test_subclass_instance(self):
        """Test that an instance of the new class can be created."""

        # Define a dummy class
        class MyClass:
            pass

        # Apply the decorator
        NewClass = subclass(MyClass)

        # Test that we can create an instance of the new class
        instance = NewClass()
        self.assertIsInstance(
            instance, NewClass, "The instance is not of the new class type."
        )

    def test_subclass_does_not_inherit_base(self):
        """Test that the new class does not inherit from the original class."""

        # Define a dummy class
        class MyClass:
            pass

        # Apply the decorator
        NewClass = subclass(MyClass)

        # Test that the new class is not a subclass of the original class
        self.assertFalse(
            issubclass(NewClass, MyClass),
            "The new class should not inherit from the original class.",
        )


# Run the tests
if __name__ == "__main__":
    unittest.main()
