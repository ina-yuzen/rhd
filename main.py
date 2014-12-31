from copy import deepcopy
import json
from flask import Flask

app = Flask(__name__)
board = [[None, None, None], [None, None, None], [None, None, None]]


def judge_end(board):
    winner = None
    for i in range(3):
        if board[i] == ['o', 'o', 'o'] or (board[0][i] == 'o' and board[1][i] == 'o' and board[2][i] == 'o'):
            winner = 'o'
        elif board[i] == ['x', 'x', 'x'] or (board[0][i] == 'x' and board[1][i] == 'x' and board[2][i] == 'x'):
            winner = 'x'
    if (board[0][0] == 'o' and board[1][1] == 'o' and board[2][2] == 'o') or \
            (board[0][2] == 'o' and board[1][1] == 'o' and board[2][0] == 'o'):
        winner = 'o'
    elif (board[0][0] == 'x' and board[1][1] == 'x' and board[2][2] == 'x') or \
            (board[0][2] == 'x' and board[1][1] == 'x' and board[2][0] == 'x'):
        winner = 'x'
    return winner


@app.route('/game/<mark>/<int:x>/<int:y>')
def put_mark(mark, x, y):
    global board
    board[x][y] = mark
    winner = judge_end(board)
    if winner is not None:
        return json.dumps({'status': '%sが勝ちました。' % winner, 'winner': winner, 'board': board}, ensure_ascii=False)

    preserved = deepcopy(board)
    while preserved == board:
        pass

    winner = judge_end(board)
    if winner is not None:
        return json.dumps({'status': '%sが勝ちました。' % winner, 'winner': winner, 'board': board}, ensure_ascii=False)

    return json.dumps({'status': 'OKです。', 'board': board}, ensure_ascii=False)


@app.route('/init')
def initialize():
    global board
    board = [[None, None, None], [None, None, None], [None, None, None]]
    return json.dumps({'status': 'OKです。', 'board': board}, ensure_ascii=False)


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
