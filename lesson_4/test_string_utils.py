import pytest
from string_utils import StringUtils 

b = StringUtils()

a = b.capitilize("skypro")
assert a == "Skypro"

a = b.trim(" skypro")
assert a == "skypro"

a = b.to_list("a,b,c,d")
assert a == ["a", "b", "c", "d"]

a = b.contains("SkyPro", "S")
assert a == True

a = b.delete_symbol("SkyPro", "Pro")
assert a == "Sky" 

a = b.starts_with("SkyPro", "S")
assert a == True

a = b.end_with("SkyPro", "o")
assert a == True

a = b.is_empty(" ")
assert a == True

a = b.list_to_string([1,2,3,4])
assert a == "1, 2, 3, 4"




"""
string_utils = StringUtils()

def capitilize(self, string: str) -> str:
        string_utils = StringUtils()
        res = string.capitalize("skypro")
        assert res == "Skypro"
"""