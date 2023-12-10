import streamlit as st 
import requests
import pandas as pd
import pymongo
st.set_page_config(page_title="Movie Web", layout="wide")
st.header("Sản phẩm demo Web Application")
st.markdown("***")
poster_data = pd.read_csv("movie_poster.csv", names=["itemID", "url"])
# @st.cache()
# Hàm liên kết với mongodb
def get_collection(connection_str):
    myclient = pymongo.MongoClient(connection_str)
    mydb = myclient["result"]
    mycol = mydb["06-12-2023"]
    return mycol
# Hàm lấy hình ảnh - bổ sung thêm title các thứ
def fetch_poster(movie_id):
    url = str(poster_data[poster_data["itemID"] == movie_id]["url"].values[0])
    st.image(url, width = 100)
# Nhập userID
userID = st.number_input("Nhập vào id người dùng: ", min_value=1, max_value=6040, step=1)
connection_str = "mongodb://longnguyenuit:ZkhrACfJflUhurRi1xUBFVLXMxNQrn2czSp5yHvomR4pvzmRPJX4niIdQT0FxdJCRVUtTx0eUkv4ACDbiTmXsQ%3D%3D@longnguyenuit.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@longnguyenuit@"
res_collection = get_collection(connection_str)
# Duyệt qua từng dòng trên collection dựa trên userID, duyệt qua các movieID trong list 10 movieID
data = res_collection.find({"userID": userID})
img_urls = []
for row in data:
    for movieID in row["itemIDs"]:
        img_urls.append(fetch_poster(movieID))
        