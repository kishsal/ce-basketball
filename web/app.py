from flask import Flask, render_template, jsonify, request
import json
import os

app = Flask(__name__)

data_path = os.path.join(os.path.dirname(__file__), 'data')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roster')
def roster():
    with open(os.path.join(data_path, 'team_roster.json'), 'r') as f:
        team_roster = json.load(f)
    return render_template('roster.html', roster=team_roster)

@app.route('/stats')
def stats():
    with open(os.path.join(data_path, 'game_stats.json'), 'r') as f:
        game_stats = json.load(f)
    return render_template('stats.html', stats=game_stats)

@app.route('/api/game-stats')
def api_game_stats():
    game_date = request.args.get('date')
    if not game_date:
        return jsonify(None)

    with open(os.path.join(data_path, 'game_stats.json'), 'r') as f:
        game_stats = json.load(f)

    for game in game_stats:
        if game['date'] == game_date:
            return jsonify(game)

    return jsonify(None)

if __name__ == '__main__':
    app.run(debug=True)
