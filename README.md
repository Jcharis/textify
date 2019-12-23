# textify
A Simple Text Cleaning and Normalization Package For NLP


#### Installation
```bash
pip install textify
```

### Usage
#### Clean Text
+ Clean text by removing emails,numbers,etc
```python
>>> from textify import TextCleaner
>>> docx = TextCleaner()
>>> docx.text = "your text goes here"
>>> docx.clean_text()
```

#### Remove Emails,Numbers,Phone Numbers 
```python
>>> docx.remove_emails()
>>> docx.remove_numbers()
>>> docx.remove_phone_numbers()
```


#### Remove Special Characters
```python
>>> docx.remove_special_characters()
```

#### Replace Emails,Numbers,Phone Numbers
```python
>>> docx.replace_emails()
>>> docx.replace_numbers()
>>> docx.replace_phone_numbers()
```

### Using TextExtractor
+ To Extract emails,phone numbers,numbers from text
```python
>>> from textify import TextExtractor
>>> docx = TextExtractor()
>>> docx.text = "your text with example@gmail.com goes here"
>>> docx.extract_emails()
```

#### By 
+ Jesse E.Agbe(JCharis)
+ Jesus Saves @JCharisTech


#### NB
+ Contributions Are Welcomed
+ Notice a bug, please let us know.
+ Thanks A lot
