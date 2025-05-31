import requests
from flask_babel import _

# Translate Method 
def translate(text, source_language, dest_language):
    # Python anywhere free translate API 
    r = requests.get(f'https://ftapi.pythonanywhere.com/translate?sl={source_language}&dl={dest_language}&text={text}')

    if r.status_code != 200:
        return _('Error: the translation service failed.')
    
    return r.json()['destination-text']