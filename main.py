from website import create_app # wesbtie is a python package so we can import things from that file

app = create_app()

if __name__ == '__main__':
    app.run(debug= True) # starts up the web-server - anytime we make changes to the code it will restart the web server
