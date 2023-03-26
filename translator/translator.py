from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

apikey = 'bGO1KPq1Kc6SPre0elQjbfHCcIzbwSCHUhcenyxZ7Tpw'
url = 'https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/920e3270-8604-470c-b798-9111066581aa'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(text):
    ftranslation = language_translator.translate(text=text1,model_id='en-fr').get_result()
    return ftranslation['translations'][0].get('translation')

def french_to_english(text):
    etranslation = language_translator.translate(text=text1,model_id='fr-en').get_result()
    return etranslation['translations'][0].get('translation')
