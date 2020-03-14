import re,sys,unicodedata

# Patterns
EMAIL_REGEX = re.compile(r"[\w\.-]+@[\w\.-]+")
PHONE_REGEX = re.compile(r"[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]")
NUMBERS_REGEX = re.compile(r"\d+")
SPECIAL_CHARACTERS_REGEX = re.compile(r"[^A-Za-z0-9 ]+")
EMOJI_REGEX = re.compile("["
                       u"\U0001F600-\U0001F64F"  # emoticons
                       u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                       u"\U0001F680-\U0001F6FF"  # transport & map symbols
                       u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                       u"\U00002702-\U000027B0"
                       u"\U000024C2-\U0001F251"
                       "]+", flags=re.UNICODE)

CURRENCIES = {
	"$": "USD",
	"zł": "PLN",
	"£": "GBP",
	"¥": "JPY",
	"฿": "THB",
	"₡": "CRC",
	"₦": "NGN",
	"₩": "KRW",
	"₪": "ILS",
	"₫": "VND",
	"€": "EUR",
	"₱": "PHP",
	"₲": "PYG",
	"₴": "UAH",
	"₹": "INR",
}
CURRENCY_REGEX = re.compile(
	"({})+".format("|".join(re.escape(c) for c in CURRENCIES.keys()))
)



class TextCleaner(object):
	"""TextCleaner: Class For Text Cleaning
	usage
	docx = TextCleaner()
	docx.text = "this is example@gmail.com and you can reach me at +380994777888 at 5pm#"

	"""
	def __init__(self, text=None):
		super(TextCleaner, self).__init__()
		self.text = text
		
	def __repr__(self):
		return "TextCleaner(text={})".format(self.text)

	def remove_emails(self):
		result = re.sub(EMAIL_REGEX,"",self.text)
		return result
	
	def remove_phone_numbers(self):
		result = re.sub(PHONE_REGEX,"",self.text)
		return result

	def remove_numbers(self):
		result = re.sub(NUMBERS_REGEX,"",self.text)
		return result

	def remove_special_characters(self):
		result = re.sub(SPECIAL_CHARACTERS_REGEX,"",self.text)
		return result

	def remove_emojis(self):
	   result = re.sub(EMOJI_REGEX,"",self.text)
	   return result

	def replace_emails(self,replace_with="<EMAIL>"):
		result = re.sub(EMAIL_REGEX,replace_with,self.text)
		return result
	
	def replace_phone_numbers(self,replace_with="<PHONENUMBER>"):
		result = re.sub(PHONE_REGEX,replace_with,self.text)
		return result

	def replace_numbers(self,replace_with="<NUMBER>"):
		result = re.sub(NUMBERS_REGEX,replace_with,self.text)
		return result

	def replace_special_characters(self,replace_with="<SPECIAL_CHAR>"):
		result = re.sub(SPECIAL_CHARACTERS_REGEX,replace_with,self.text)
		return result


	def clean_text(self,preserve=False):
		if preserve == False:
			email_result = re.sub(EMAIL_REGEX,"",self.text)
			phone_result = re.sub(PHONE_REGEX,"",email_result)
			number_result = re.sub(NUMBERS_REGEX,"",phone_result)
			emoji_result = re.sub(EMOJI_REGEX,"",number_result)
			special_char_result = re.sub(SPECIAL_CHARACTERS_REGEX,"",emoji_result)
			final_result = special_char_result.lower()
			
		else:
			special_char_result = re.sub(r'[^A-Za-z0-9@ ]+',"",self.text)
			email_result = re.sub(EMAIL_REGEX,"<EMAIL>",special_char_result)
			phone_result = re.sub(PHONE_REGEX,"<PHONENUMBER>",email_result)
			number_result = re.sub(NUMBERS_REGEX,"<NUMBERS>",phone_result)
			final_result = number_result.lower()
			
		return final_result


class TextExtractor(TextCleaner):
	"""TextExtractor - Extract emails,numbers and phone numbers from text"""
	def __init__(self, text=None):
		super(TextExtractor, self).__init__()
		self.text = text

	def __repr__(self):
		return "TextExtractor(text={})".format(self.text)

	def extract_emails(self):
		match = re.findall(EMAIL_REGEX,self.text)
		return match
	
	def extract_phone_numbers(self):
		match = re.findall(PHONE_REGEX,self.text)
		return match

	def extract_numbers(self):
		match = re.findall(NUMBERS_REGEX,self.text)
		return match

	def extract_emojis(self):
	   match = re.findall(EMOJI_REGEX,self.text)
	   return match


