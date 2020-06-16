import requests

if __name__=="__main__":
    resp=requests.post("http://localhost:5000/predict",files={
        "file":open("./sample_file.jpg","rb")
    })
    print(resp.json())