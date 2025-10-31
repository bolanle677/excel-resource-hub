from flask import Flask, render_template, request, redirect
import boto3
import os
from dotenv import load_dotenv

# --- Load environment variables ---
load_dotenv()

app = Flask(__name__)

# --- AWS S3 Configuration ---
S3_BUCKET = "arin-excel-hub"
S3_REGION = "us-east-1"
S3_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")   # ✅ corrected key name
S3_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")  # ✅ corrected key name

# --- Initialize S3 client ---
s3 = boto3.client(
    "s3",
    aws_access_key_id=S3_ACCESS_KEY,
    aws_secret_access_key=S3_SECRET_KEY,
    region_name=S3_REGION
)

# --- Home page ---
@app.route("/")
def index():
    return render_template("index.html")

# --- Upload page ---
@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        if "file" not in request.files:
            return "No file part"
        file = request.files["file"]
        if file.filename == "":
            return "No selected file"
        
        try:
            s3.upload_fileobj(file, S3_BUCKET, file.filename)
            return redirect("/downloads")
        except Exception as e:
            return f"Error uploading file: {str(e)}"
    
    return render_template("upload.html")

# --- List and Download Files ---
@app.route("/downloads")
def list_files():
    try:
        response = s3.list_objects_v2(Bucket=S3_BUCKET)
        if "Contents" in response:
            files = response["Contents"]
        else:
            files = []
        return render_template("download.html", files=files, bucket_name=S3_BUCKET)
    except Exception as e:
        return f"Error fetching files: {str(e)}"

# --- Run the app ---
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
