from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Global variables for the calculator logic
input_values = []
x_value_global = 10  # Default X value

@app.route('/')
def index():
	return render_template('index.html', total="Total Pontuado: 0", pressed_buttons=[])

# Handle button clicks
@app.route('/button_click', methods=['POST'])
def button_click():
	global input_values, x_value_global

	value = str(request.json['value'])  # Ensure the value is treated as a string

	# Add the value to the input list if there are less than 10 inputs
	if len(input_values) < 10:
		input_values.append(value)

	total_sum = sum([int(v) for v in input_values if v.isdigit()])  # Only sum numeric values
	return jsonify({'total': f"Total Pontuado: {total_sum}", 'pressed_buttons': input_values})

# Handle reset
@app.route('/reset', methods=['POST'])
def reset():
	global input_values
	input_values = []
	return jsonify({'total': "Total Pontuado: 0", 'pressed_buttons': []})

if __name__ == '__main__':
	app.run(debug=True)
