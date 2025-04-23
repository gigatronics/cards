from flask import Flask, request, jsonify
from risk_score_logic import calc_risk_score

app = Flask(__name__)

@app.route('/api/risk-score', methods=['POST'])
def risk_score():
    data = request.json
    score, reasons = calc_risk_score(data)
    return jsonify({'score': score, 'reasons': reasons})

if __name__ == '__main__':
    app.run(debug=True)