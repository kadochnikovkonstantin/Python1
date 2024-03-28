import pytest
from string_utils import StringUtils 

b = StringUtils()

a = b.capitilize("skypro")
assert a == "Skypro"

a = b.capitilize("Skypro")
assert a == "Skypro"

#a = b.capitilize(None)
#assert a == ""

a = b.capitilize(" ")
assert a == " "


a = b.trim(" skypro")
assert a == "skypro"

a = b.to_list("a,b,c,d")
assert a == ["a", "b", "c", "d"]

#a = b.to_list(None)
#assert a == ["a b c d"]

a = b.contains("SkyPro", "S")
assert a == True

a = b.contains("SkyPro", "U")
assert a == False

a = b.delete_symbol("SkyPro", "Pro")
assert a == "Sky" 

a = b.starts_with("SkyPro", "S")
assert a == True

a = b.starts_with("", "")
assert a == True

# a = b.starts_with(" SkyPro", "S")
# assert a == True

a = b.end_with("SkyPro", "o")
assert a == True

a = b.end_with("", "")
assert a == True

a = b.is_empty(" ")
assert a == True

a = b.is_empty("")
assert a == True

a = b.is_empty("рубль")
assert a == False

#a = b.is_empty(None)
#assert a == True

a = b.list_to_string([1,2,3,4])
assert a == "1, 2, 3, 4"

a = b.list_to_string([ ])
assert a == ""


a = b.list_to_string("")
assert a == ""


"""
string_utils = StringUtils()

def capitilize(self, string: str) -> str:
        string_utils = StringUtils()
        res = string.capitalize("skypro")
        assert res == "Skypro"
"""