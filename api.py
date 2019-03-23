from flask import Flask
from flask_restful import Resource, Api, reqparse
import json

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

board_parser = reqparse.RequestParser()
board_parser.add_argument('round', type=int, default=None, required=True, help='Round')
board_parser.add_argument('turn', type=int, default=None, required=True, help='Turn')

class Board(Resource):
    def get(self):
        args = board_parser.parse_args()
        round = args['round']
        turn = args['turn']
        with open("output/board_round_%d_turn_%d.json" % (round, turn), 'r') as f:
            board = json.load(f)
        return board

api.add_resource(Board, '/board')

action_parser = reqparse.RequestParser()
action_parser.add_argument('round', type=int, default=None, required=True, help='Round')
action_parser.add_argument('turn', type=int, default=None, required=True, help='Turn')

class Action(Resource):
    def get(self):
        args = action_parser.parse_args()
        round = args['round']
        turn = args['turn']
        with open("output/action_round_%d_turn_%d.json" % (round, turn), 'r') as f:
            action = json.load(f)
        return action

api.add_resource(Action, '/action')

if __name__ == '__main__':
    app.run(debug=True)
