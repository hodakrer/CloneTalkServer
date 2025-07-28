from flask import Flask, request, jsonify

app = Flask(__name__)

# 임시 유저 DB (예시)
users = {
    "01012345678": "password123"
}

@app.route("/")
def home():
    return "Welcome to the home page!"

@app.route("/member/login", methods=["POST"])
def login():
    data = request.get_json()
    print(f"[LOG] /member/login 요청 데이터: {data}")
    phone_number = data.get("phoneNumber")
    password = data.get("password")

    if not phone_number or not password:
        return jsonify({"error": "phoneNumber and password are required"}), 400

    # 로그인 검증 (임시)
    if users.get(phone_number) == password:
        # 로그인 성공: 토큰 발급 (여기선 간단한 문자열 토큰)
        token = "dummy_token_12345"
        return jsonify({"token": token}), 200
    else:
        # 로그인 실패
        return jsonify({"error": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run(debug=True)