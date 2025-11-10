from flask import Flask,jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app) #允许cross port
@app.route('/')  # 访问根目录的时候调用root


def home():
    return jsonify({"message":"....ˊˋ------｡:.ﾟ_ヽ(_´∀`_)ﾉ_.:｡((浮水"})


if __name__ == "__main__":
    app.run(debug=True)  #启动一个服务，监听http请求