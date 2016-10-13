from flask import Flask
from ucloud_api.Client import *

app = Flask(__name__)

@app.route('/test')
def test():
        ucloud_client = Client(api_type='watch',api_key="",secret="")
        response = ucloud_client.request('listAlarms')
	
        dump_result = json.dumps(response)
        return '%s' %dump_result

def hello():
	return "hello world!"

if __name__ == "__main__":
	app.run(host='0.0.0.0')
