from flask import Flask
import os

app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/')
def execute_judger():
    player_list = ['judger/player_example'] * 3
    os.system('java -jar judger/Splendor.jar --player_binary_paths %s,%s,%s --game_log_path log.txt' %
              (player_list[0], player_list[1], player_list[2]))
    with open('log.txt', 'r') as f:
        lines = f.readlines()
    return ''.join(lines)

if __name__ == '__main__':
    app.run()
