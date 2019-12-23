from textify import __version__
from textify import TextCleaner,TextExtractor

def test_version():
    assert __version__ == '0.0.1'


def test_clean_text():
	docx = TextCleaner()
	docx.text = "He was writing to example@gmail.com on the 12th of January. Later on he called him on +380934777555 but he missed $100 dollars#"
	result = docx.clean_text()
	assert result == "he was writing to  on the th of january later on he called him on  but he missed  dollars"

def test_remove_email():
	docx = TextCleaner()
	docx.text = "After calling him  on +080934777555,he told him to mail him at example@gmail.com before January. Later on he wired him $100 dollars#"
	result = docx.remove_emails()
	assert result == "After calling him  on +080934777555,he told him to mail him at  before January. Later on he wired him $100 dollars#"

def test_replace_email():
	docx = TextCleaner()
	docx.text = "After calling him  on +080934777555,he told him to mail him at example@gmail.com before January. Later on he wired him $100 dollars#"
	result = docx.replace_emails()
	assert result == "After calling him  on +080934777555,he told him to mail him at <EMAIL> before January. Later on he wired him $100 dollars#"

def test_extract_email():
	docx = TextExtractor()
	docx.text = "After calling him  on +080934777555,he told him to mail him at example@gmail.com before January. Later on he wired him $100 dollars#"
	result = docx.extract_emails()
	assert result == ['example@gmail.com']

