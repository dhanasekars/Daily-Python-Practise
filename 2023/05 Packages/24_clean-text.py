""" 
Created on : 24/05/23 1:20 pm
@author : ds  
"""

from cleantext import clean

# Sample text
text = """ Zürich, largest city of Switzerland and capital of the canton of 633Zürich. Located in an Al\u017eupine. (https://google.com). Currency is not ₹"""
# Cleaning the "text" with clean text
cleaned_text = clean(text,
      fix_unicode=True,
      to_ascii=True,
      lower=True,
      no_urls=True,
      no_numbers=True,
      no_digits=True,
      no_currency_symbols=True,
      no_punct=True,
      replace_with_punct=" ",
      replace_with_url="",
      replace_with_number="",
      replace_with_digit=" ",
      replace_with_currency_symbol="Rupees")

print(cleaned_text)