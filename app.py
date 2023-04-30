from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roster')
def roster():
    with open('data/team_roster.json', 'r') as f:
        team_roster = json.load(f)
    return render_template('roster.html', roster=team_roster)

@app.route('/stats')
def stats():
    with open('data/game_stats.json', 'r') as f:
        game_stats = json.load(f)
    return render_template('stats.html', stats=game_stats)

@app.route('/schedule')
def schedule():
    return render_template('schedule.html')

@app.route('/api/game-stats')
def api_game_stats():
    game_date = request.args.get('date')
    if not game_date:
        return jsonify(None)

    with open('data/game_stats.json', 'r') as f:
        game_stats = json.load(f)

    for game in game_stats:
        if game['date'] == game_date:
            return jsonify(game)

    return jsonify(None)

if __name__ == '__main__':
    app.run(debug=True)
