from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    return "FLASK IS WORKING PROPERLY"

if __name__=='__main__':
    app.run()
