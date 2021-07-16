# def gcd(a,b):
#         if b == 0:
#             return a
#         else:
#             return gcd(b, a % b)

            
# print(gcd(35,14))

from flask import Flask
from flask import request

app = Flask(__name__)

# 지시사항을 참고하여 함수를 완성하세요.
@app.route("/")
def hello():

    return "hello"

# @app.route('/', methods = ['GET'])
# def name_age():
    
#     name = request.args.get("name")
#     age = request.args.get("age")
#     print("hello")
    
#     return name + ": " + age

if __name__ == '__main__':
    app.run()