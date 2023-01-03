from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

#For making Requests i.e. GET, POST, PUT, DELETE
class HelloWorld(Resource):
    def get(self):
        return {"data":"Hello Flask its Wainaina"}

# http://127.0.0.1:5000/helloworld
api.add_resource(HelloWorld, "/helloworld") 

if __name__ == '__main__':
    app.run(debug=True) #for debuggin in test environnt