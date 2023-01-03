from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    views = db.Column(db.Integer, nullable=False) 
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name={name}, views={views}, likes={likes})"

################################################################
# NB: AFTER RUNNING THE CODE, COMMENT THIS LINE SO AS TO PREVENT RE-INITIALIZATION OF THE DATA
db.create_all() #initialize database
################################################################

#PUT ie create a new video
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Error: Name of video is required", required = True)
video_put_args.add_argument("views", type=int, help="Error: Views of video is required", required = True)
video_put_args.add_argument("likes", type=int, help="Error: Likes on video is required", required = True)

#PATCH ie update a video
video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Error: Name of video is required")
video_update_args.add_argument("views", type=int, help="Error: Views of video is required")
video_update_args.add_argument("likes", type=int, help="Error: Likes on video is required")


resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer,
}

#For making Requests i.e. GET, POST, PUT, DELETE
class Video(Resource):    

    #GET
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        #result = VideoModel.query.filter_by(id=video_id).all()
        if not result:
            abort(404, message="Couldn't find video with that id")
        return result
    
    #PUT -> post
    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        #Check if there is an existing video with that id
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="Error: Video ID already exists/taken...")

        video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video) #temporarily
        db.session.commit() # permanently
        return video, 201
    
    # PATCH
    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_update_args.parse_args()
        #Check if the video exists
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(409, message="Error: Video ID doesnt exists...")

        if  args["name"]:
            result.name = args["name"]
        if args["views"]:
            result.views = args["views"]
        if  args["likes"]:
            result.likes = args["likes"]

        db.session.commit()

        return result

    def delete(self, video_id):
        abort_if_video_does_not_exist(video_id)
        del videos[video_id]
        return (204, {'message':'Video deleted successfully.'})
#1
# http://127.0.0.1:5000/helloworld
# api.add_resource(Video, "/helloworld") 

#2
# http://127.0.0.1:5000/video/1
api.add_resource(Video, "/video/<int:video_id>") 

if __name__ == '__main__':
    app.run(debug=True) #for debuggin in test environnt