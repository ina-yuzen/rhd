from copy import deepcopy
import json
from flask import Flask

app = Flask(__name__)


def judge_winner(board):
    winner = None

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            winner = board[i][0]
        elif board[0][i] == board[1][i] == board[2][i]:
            winner = board[0][i]

    if board[0][0] == board[1][1] == board[2][2]:
        winner = board[0][0]
    elif board[0][2] == board[1][1] == board[2][0]:
        winner = board[0][2]

    return winner


@app.route('/<mark>/<int:x>/<int:y>')
def put_mark_and_return(mark, x, y):
    winner = put_mark(mark, x, y)

    if winner:
        return return_value()

    wait_until_change()

    return return_value()


def put_mark(mark, x, y):
    global board
    board[x][y] = mark
    return judge_winner(board)


def wait_until_change():
    global board
    preserved = deepcopy(board)
    while preserved == board:
        pass


@app.route('/init')
def initialize():
    global board
    board = [[None, None, None], [None, None, None], [None, None, None]]
    return return_value()


@app.route('/wait')
def wait_first():
    initialize()
    wait_until_change()
    return return_value()


def return_value():
    global board
    winner = judge_winner(board)
    return json.dumps({'board': board, 'winner': winner}, ensure_ascii=False)


if __name__ == '__main__':
    initialize()
    app.run(debug=True, threaded=True)
