from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = 'bGO1KPq1Kc6SPre0elQjbfHCcIzbwSCHUhcenyxZ7Tpw'
url = 'https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/920e3270-8604-470c-b798-9111066581aa'

authenticator = IAMAuthenticator(apikey)
lt = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

lt.set_service_url(url)

def english_to_french(text):
    translation = lt.translate(text=text, source='en', target='fr').get_result()
    return translation['translations'][0]['translation']

def french_to_english(text):
    translation = lt.translate(text=text, source='fr', target='en').get_result()
    return translation['translations'][0]['translation']
