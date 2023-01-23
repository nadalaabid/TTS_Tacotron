'''
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run
through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details.
'''
from text import cmudict

_pad        = '_'
_eos        = '~'
_characters = { u"\u0621", # hamza-on-the-line
             u"\u0622", # madda
             u"\u0623", # hamza-on-'alif
             u"\u0624", # hamza-on-waaw
             u"\u0625", # hamza-under-'alif
             u"\u0626", # hamza-on-yaa'
             u"\u0627", # bare 'alif
             u"\u0628", # baa'
             u"\u0629", # taa' marbuuTa
             u"\u062A", # taa'
             u"\u062B", # thaa'
             u"\u062C", # jiim
             u"\u062D", # Haa'
             u"\u062E", # khaa'
             u"\u062F", # daal
             u"\u0630", # dhaal
             u"\u0631", # raa'
             u"\u0632", # zaay
             u"\u0633", # siin
             u"\u0634", # shiin
             u"\u0635", # Saad
             u"\u0636", # Daad
             u"\u0637", # Taa'
             u"\u0638", # Zaa' (DHaa')
             u"\u0639", # cayn
             u"\u063A", # ghayn
             u"\u0640", # taTwiil
             u"\u0641", # faa'
             u"\u0642", # qaaf
             u"\u0643", # kaaf
             u"\u0644", # laam
             u"\u0645", # miim
             u"\u0646", # nuun
             u"\u0647", # haa'
             u"\u0648", # waaw
             u"\u0649", # 'alif maqSuura
             u"\u064A", # yaa'
             u"\u064B", # fatHatayn
             u"\u064C", # Dammatayn
             u"\u064D", # kasratayn
             u"\u064E", # fatHa
             u"\u064F", # Damma
             u"\u0650", # kasra
             u"\u0651", # shaddah
             u"\u0652", # sukuun
             u"\u0670", # dagger 'alif
             u"\u0671", # waSla
            "!","/" , "'" , "(" , ")" , "," , "-" , "." , ":" , ";" , "?" }
# Prepend "@" to ARPAbet symbols to ensure uniqueness (some are the same as uppercase letters):
_arpabet = ['@' + s for s in cmudict.valid_symbols]

# Export all symbols:
symbols = [_pad, _eos] + list(_characters) + _arpabet
