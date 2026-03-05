from flask import Flask 
app = Flask(__name__)

def speedcheck():
  st = speedtest.Speedtest()
  st.get_best_server()

  download_bps = st.download()
  upload_bps = st.upload()
  ping = st.results.ping

  download_mbs = round(download_bps / 10**6,2)
  upload_mbs = round(upload_bps / 10**6, 2)
  return{
    "download": download_mbs,
    "upload": upload_mbs,
    "ping": ping,
}

@app.route('/')
def index():
  return "Server is running!"

if __name__ == '__main__':
  print("Starting..")
  print("Testing speed... please wait (this takes a few seconds)...")
  results = speedcheck()
  prinf(f"Speed test done!\nResult: {results}")
  app.run(debug=True)
