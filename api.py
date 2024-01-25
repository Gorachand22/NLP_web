# !pip install paralleldots

import paralleldots
 
class API:
    def __init__(self, text):
        if len(text) == 43:
            paralleldots.set_api_key(text)
        else:
                raise ValueError('Invalid API Key')

    def sentiment_analysis(self, text):    
            response = paralleldots.sentiment(text)
            return response
    
    # --------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------
    def ner_analysis(self, text):    
            response = paralleldots.ner(text)
            return response
    
    # --------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------
    def emp_analysis(self, text):  
        try:
            response = paralleldots.batch_emotion(text)
            if response['emotion']:
                for i in response['emotion'][0]:
                    if response['emotion'][0][i] == max(response['emotion'][0].values()):
                        return i
            else:
                # No emotion detected
                return 'No emotion detected'
        except:
            raise ValueError('No Response Found')
    
    # --------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------
    def sarcasm_analysis(self, text):  
        try:
            response = paralleldots.batch_sarcasm(text)
            if response[0]:
                for i in response[0]:
                    if response[0][i] == max(response[0].values()):
                        return i
            else:
                # No emotion detected
                return 'No sarcasm detected'
        except:
            raise ValueError('No Response Found')
    

    # --------------------------------------------------------------------------------------------------------
    # --------------------------------------------------------------------------------------------------------
    def abuse_analysis(self, text):  
        try:
            response = paralleldots.batch_abuse(text)
            if response['abuse']:
                for i in response['abuse'][0]:
                    if response['abuse'][0][i] == max(response['abuse'][0].values()):
                        return i
            else:
                return 'No Abuse word is detected'
        except Exception as e:
            raise ValueError('No Response Found')

# ----------------------------------------------END OF CLASS API----------------------------------------------------------