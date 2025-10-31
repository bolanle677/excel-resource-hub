A Flask web application for uploading, storing, and downloading Excel resources securely using AWS S3.
This project demonstrates the integration of Python (Flask) with Amazon S3, deployed on AWS EC2, and serves as a foundation for building scalable, cloud-based applications.

🚀 Features


🗂️ Upload Excel Files — Users can upload .xlsx or .xls files directly through the web interface.


☁️ AWS S3 Integration — All files are stored and retrieved from an S3 bucket (arin-excel-hub).


📥 Download Files — Automatically lists uploaded files for download.


🔐 Environment Variables — Uses .env to keep AWS credentials secure.


🌍 EC2 Deployment — Deployed and hosted on an AWS EC2 instance (Ubuntu).


⚙️ Boto3 + Flask + Python-dotenv — Handles AWS communication and app configuration cleanly.



🧰 Tech Stack
LayerTechnologyFrontendHTML, Jinja2 TemplatesBackendFlask (Python)Cloud ServicesAWS EC2, AWS S3Environment ManagementPython-dotenvVersion ControlGit & GitHubDeployment OSUbuntu (Amazon EC2)

🏗️ Project Structure
excel-resource-hub/
│
├── app.py                # Flask main application
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (not pushed to GitHub)
├── templates/
│   ├── index.html        # Home page
│   ├── upload.html       # Upload form
│   └── download.html     # File list and download links
└── README.md             # Project documentation


⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/bolanle677/excel-resource-hub.git
cd excel-resource-hub

2️⃣ Create and Configure .env
Inside your project root, create a .env file:
S3_BUCKET=arin-excel-hub
S3_REGION=us-east-1
S3_ACCESS_KEY=your_aws_access_key
S3_SECRET_KEY=your_aws_secret_key

3️⃣ Install Dependencies
pip3 install -r requirements.txt

4️⃣ Run the App Locally
python3 app.py

Access it on:
👉 http://127.0.0.1:5000

☁️ Deploying on AWS EC2


Launch an EC2 instance (Ubuntu).


SSH into it:
ssh -i "your-key.pem" ubuntu@your-ec2-public-ip



Clone your repo:
git clone https://github.com/bolanle677/excel-resource-hub.git
cd excel-resource-hub



Install dependencies:
pip3 install -r requirements.txt



Create .env and run:
python3 app.py



Visit:
http://<your-ec2-public-ip>:5000



💡 Future Improvements


🔹 Add authentication (login/signup).


🔹 Enable file type validation and size limits.


🔹 Configure Gunicorn + Nginx for production deployment.


🔹 Add CI/CD using GitHub Actions.


🔹 Extend to include database integration (RDS).



👩🏽‍💻 Author
Bolanle Akinbamowo
AWS DevOps & Cloud Enthusiast | CI/CD | Flask | Kubernetes | Terraform
📧 bolanleakinbamowo@gmail.com
🔗 LinkedIn | GitHub

🏁 Acknowledgment
This project was inspired by a friend who needed a simple platform for documenting and sharing Excel resources. I decided to build it to provide a practical solution while also improving my cloud and web development skills using Flask and AWS services.
