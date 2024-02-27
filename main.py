from app import app
#from gevent.pywsgi import WSGIServer

if __name__ == "__main__":
    #app.run()
    #http_server = WSGIServer(('', 5001), app)
    #http_server.serve_forever()
    from waitress import serve
    serve(app, host="0.0.0.0", port=8000)
