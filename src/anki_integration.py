import json
import urllib.request

def request(action, params):
    return {'action': action, 'params': params, 'version': 6}

def invoke(action, params):
    requestJson = json.dumps(request(action, params)).encode('utf-8')
    response = json.load(urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:8765', requestJson)))
    if len(response) != 2:
        raise Exception('response has an unexpected number of fields')
    if 'error' not in response:
        raise Exception('response is missing required error field')
    if 'result' not in response:
        raise Exception('response is missing required result field')
    if response['error'] is not None:
        raise Exception(response['error'])
    return response['result']

def fill_note(deckName="default", modelName="Basic", fields=None, tags=None):
    if fields is None:
        fields = {}
    if tags is None:
        tags = []
    return {
            'deckName': deckName,
            'modelName': modelName,
            'fields': fields,
            'tags': tags,
            'options': {
                'allowDuplicate': True
            }
        }

if __name__ == "__main__":
    deckName = "spanish selfmade"
    modelName = "Spanish Sentence"
    tags = ["spanish_vocab"]
    payload = {
        "notes": []
    }
    
    fields_list = 
    for fields in fields_list:
        payload["notes"].append(fill_note(deckName=deckName, modelName=modelName, fields=fields, tags=tags))
    print(payload)
    result = invoke('addNotes', payload)
    print('received the result: {}'.format(result))