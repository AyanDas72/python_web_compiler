from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/run', methods=['POST'])
def compile_code():
    data = request.get_json()
    #print("Received JSON:", data)  

    code = data.get("code", "")
    language = data.get("language", "python").strip()
    user_input = data.get("user_input", "").strip()  

    commands = {
        "python": ["python", "-c", code],  
        #"java": [],  
    }

    if language not in commands:
        return jsonify({"error": "Invalid language"}), 400  

    try:
        process = subprocess.Popen(
            commands[language],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        output, error = process.communicate(input=user_input, timeout=15)

        final_output = output if output else error

    except subprocess.TimeoutExpired:
        final_output = "Execution timed out after 15 seconds."
    except Exception as e:
        final_output = f"Error: {str(e)}"

    return jsonify({"output": final_output})

if __name__ == '__main__':
    app.run(debug=True)
