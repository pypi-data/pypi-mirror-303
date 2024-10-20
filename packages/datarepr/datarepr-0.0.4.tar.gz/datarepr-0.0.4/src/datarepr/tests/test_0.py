import unittest

from datarepr.core import datarepr


class TestDatareprFunction(unittest.TestCase):

    def test_empty_args_kwargs(self):
        """Test when only the name is provided and no args or kwargs."""
        result = datarepr("test_function")
        self.assertEqual(result, "test_function()")

    def test_positional_args_only(self):
        """Test with positional arguments only."""
        result = datarepr("test_function", 1, 2, 3)
        self.assertEqual(result, "test_function(1, 2, 3)")

        result = datarepr("test_function", "a", "b", "c")
        self.assertEqual(result, "test_function('a', 'b', 'c')")

    def test_keyword_args_only(self):
        """Test with keyword arguments only."""
        result = datarepr("test_function", a=1, b=2, c=3)
        self.assertEqual(result, "test_function(a = 1, b = 2, c = 3)")

        result = datarepr("test_function", x="x", y="y")
        self.assertEqual(result, "test_function(x = 'x', y = 'y')")

    def test_mixed_args(self):
        """Test with both positional and keyword arguments."""
        result = datarepr("test_function", 1, 2, a=3, b=4)
        self.assertEqual(result, "test_function(1, 2, a = 3, b = 4)")

        result = datarepr("test_function", "x", "y", z=5)
        self.assertEqual(result, "test_function('x', 'y', z = 5)")

    def test_various_types(self):
        """Test with various types of arguments."""
        result = datarepr("test_function", 1, 2.0, True, None)
        self.assertEqual(result, "test_function(1, 2.0, True, None)")

        result = datarepr("test_function", [1, 2], {3, 4}, {"key": "value"})
        self.assertEqual(result, "test_function([1, 2], {3, 4}, {'key': 'value'})")

    def test_name_as_non_string(self):
        """Test with the 'name' parameter as a non-string type."""
        result = datarepr(123, "arg1")
        self.assertEqual(result, "123('arg1')")

        result = datarepr(None, "arg1")
        self.assertEqual(result, "None('arg1')")

    def test_empty_name(self):
        """Test with an empty name."""
        result = datarepr("", 1, 2, a=3)
        self.assertEqual(result, "(1, 2, a = 3)")

    def test_special_characters(self):
        """Test with special characters in arguments."""
        result = datarepr("test_function", "a\nb", "\t", key="val\nue")
        self.assertEqual(result, "test_function('a\\nb', '\\t', key = 'val\\nue')")

    def test_large_number_of_args(self):
        """Test with a large number of arguments."""
        args = range(100)
        result = datarepr("test_function", *args)
        expected = "test_function(" + ", ".join(map(str, args)) + ")"
        self.assertEqual(result, expected)

    def test_duplicate_keys(self):
        """Test what happens when duplicate keys are provided in kwargs."""
        with self.assertRaises(TypeError):
            # In Python, duplicate keys in **kwargs should raise an error.
            datarepr("test_function", 1, 2, a=3, a=4)

    def test_combination_of_all(self):
        """Test with a complex combination of different types and structures."""
        result = datarepr(
            "complex_function", [1, 2], {3: 4}, a=5, b=[6, 7], c={"key": "value"}
        )
        self.assertEqual(
            result,
            "complex_function([1, 2], {3: 4}, a = 5, b = [6, 7], c = {'key': 'value'})",
        )

    def test_no_args_at_all(self):
        """Test with no arguments, not even the name."""
        with self.assertRaises(TypeError):
            datarepr()  # Should raise a TypeError due to missing required 'name' argument.


if __name__ == "__main__":
    unittest.main()
