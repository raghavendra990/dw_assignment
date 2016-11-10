import requests

class manage:
    def __init__(self , host):
        self.host = host

    def ADD(self , key  , value):
        headers = {
            'Content-Type': 'application/json',
        }
        data = '{"key":"%s", "value":"%s"}'%(key , value)
        r = requests.post('%s/add_key/'%(self.host), headers=headers, data=data)
        return r.text 

    def GET(self , key  ):
        headers = {
            'Content-Type': 'application/json',
        }
        data = '{"key":"%s"}'%(key )
        r = requests.post('%s/get_key/'%(self.host), headers=headers, data=data)
        return r.text

    def DELETE(self , key):
        headers = {
            'Content-Type': 'application/json',
        }
        data = '{"key":"%s"}'%(key )
        r = requests.post('%s/delete_key/'%(self.host), headers=headers, data=data)
        return r.text

