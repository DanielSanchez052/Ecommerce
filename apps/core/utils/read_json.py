import json


def read_json(name=None,path=''): 
    data = {}
    try:        
        if name == None:
            raise Exception
        with open(f'{path}{name}') as f:
            data = json.loads(f.read())
    except Exception as e:
        print(e)
    finally:
        return data    

