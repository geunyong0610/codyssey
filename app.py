from flask import Flask

app = Flask(__name__)

# 사용자가 / 경로로 들어오면 "Hello, DevOps!"를 보여줌.
@app.route("/")  
def hello_world():
    return "Hello, DevOps!"  

# 이 파일이 직접 실행될 때만 아래 내용을 실행됨 
# 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)