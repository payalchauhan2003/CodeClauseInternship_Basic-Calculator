from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.json['num1'])
        num2 = float(request.json['num2'])
        operator = request.json['operator']

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                return jsonify({'error': 'Division by zero!'})
            else:
                result = num1 / num2
        else:
            return jsonify({'error': 'Invalid operator!'})

        return jsonify({'result': result})
    except ValueError:
        return jsonify({'error': 'Invalid input!'})


if __name__ == '__main__':
    app.run(debug=True)
