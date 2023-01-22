import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
translator = LanguageTranslatorV3(
    version='2023-01-21',
    authenticator=authenticator
)


def french_to_english(french_text):
    try:
        translate = translator.translate(text=french_text, model_id='fr-en').get_result()
        french_text = translate['translations'][0]['translation']
        return french_text

    except Exception as error:
        return error


def english_to_french(english_text):
    try:
        translate = translator.translate(text=english_text, model_id='en-fr').get_result()
        english_text = translate['translations'][0]['translation']
        return english_text

    except Exception as error:
        return error
