import pytest
from string_utils import StringUtils

# 1. Тест для capitalize_text (позитивный)
def test_capitalize_text_positive():
    assert StringUtils.capitalize_text("hello") == "Hello"
    assert StringUtils.capitalize_text("Hello") == "Hello"
    assert StringUtils.capitalize_text("h") == "H"

# 2. Тест для capitalize_text (негативный)
def test_capitalize_text_empty():
    assert StringUtils.capitalize_text("") == ""

# 3. Тест для add_period (позитивный)
def test_add_period_without_period():
    assert StringUtils.add_period("Hello") == "Hello."
    
def test_add_period_with_period():
    assert StringUtils.add_period("Hello.") == "Hello."

# 4. Тест для add_period (негативный)
def test_add_period_empty():
    assert StringUtils.add_period("") == "."

# 5. Тест для replace_spaces
def test_replace_spaces():
    assert StringUtils.replace_spaces("hello world") == "hello_world"
    assert StringUtils.replace_spaces(" multiple  spaces ") == "_multiple__spaces_"
    assert StringUtils.replace_spaces("") == ""

# Более сложные сценарии (например, с другими символами)
def test_replace_spaces_custom_char():
    assert StringUtils.replace_spaces("hello world", "-") == "hello-world"