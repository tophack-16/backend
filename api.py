from flask import Flask
from flask_restful import Resource, Api, reqparse
import json

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

parser = reqparse.RequestParser()
parser.add_argument('class', type=list)
parser.add_argument('round', type=int, default=None, required=True, help='Round')
parser.add_argument('turn', type=int, default=None, required=True, help='Turn')

class Board(Resource):
    def get(self):
        args = parser.parse_args()
        round = args['round']  # List ['A', 'B']
        turn = args['turn']  # Boolean True
        with open("output/board_round_%d_turn_%d.json" % (round, turn), 'r') as f:
            board = json.load(f)
        return board

api.add_resource(Board, '/board')

if __name__ == '__main__':
    app.run(debug=True)
