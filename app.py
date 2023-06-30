from flask import Flask, render_template, jsonify, request
import json

# Create the application instance
app = Flask(__name__)

# Create a URL route in our application for "/"
@app.route('/')
def index():
    return render_template('index.html')

# Create a URL route in our application for "/roster"
@app.route('/roster')
def roster():
    with open('data/team_roster.json', 'r') as f:
        team_roster = json.load(f)
    return render_template('roster.html', roster=team_roster)

# Create a URL route in our application for "/stats"
@app.route('/stats')
def stats():
    with open('data/game_stats.json', 'r') as f:
        game_stats = json.load(f)
    game_dates = list(set([game['date'] for game in game_stats]))
    return render_template('stats.html', game_dates=game_dates)

# Create a URL route in our application for "/schedule"
@app.route('/schedule')
def schedule():
    with open('data/schedule_events.json', "r") as json_file:
        schedule_events = json.load(json_file)
    return render_template('schedule.html', schedule_events=schedule_events)

# Create a URL route in our application for "/api/roster"
@app.route('/api/game-stats')
def api_game_stats():
    game_date = request.args.get('date')
    if not game_date:
        return jsonify(None)

    with open('data/game_stats.json', 'r') as f:
        game_stats = json.load(f)

    matching_games = [game for game in game_stats if game['date'] == game_date]

    return jsonify(matching_games)

if __name__ == '__main__':
    app.run(debug=True)
