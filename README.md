
# 🤖 Claude 3.5 AWS Chatbot

A simple chatbot powered by **Claude 3.5 Sonnet** via **Amazon Bedrock**, built using **Python Flask**.  
This chatbot is designed to only respond to questions related to **Amazon Web Services (AWS)** — making it a focused assistant for AWS learners and developers!

---

## 🚀 Features

- ✅ Clean and responsive chat interface with Bootstrap
- ✅ Powered by Claude 3.5 Sonnet on AWS Bedrock
- ✅ Claude only answers AWS-related questions
- ✅ Includes retry logic to handle throttling
- ✅ Displays input/output token usage for transparency

---

## 📦 Tech Stack

| Component    | Technology                            |
|--------------|----------------------------------------|
| Frontend     | HTML, CSS, Bootstrap 5                |
| Backend      | Python 3, Flask                       |
| AI Model     | Claude 3.5 Sonnet via Amazon Bedrock  |
| Cloud        | AWS (Bedrock + IAM)                   |

---

## 📁 Project Structure

```
chatbot-aws/
│
├── app.py                # Main Flask app
├── templates/
│   └── index.html        # Frontend UI
├── static/
│   └── style.css         # Custom CSS (optional)
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 🛠️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Apikmmar/chatbot-aws.git
cd chatbot-aws
```

### 2. Set up virtual environment (optional but recommended)

```bash
python -m venv venv
# Activate the virtual environment:
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install required Python packages

```bash
pip install -r requirements.txt
```

### 4. Set up AWS credentials

You must have access to **Amazon Bedrock**. Configure your AWS credentials using:

```bash
aws configure
```

Make sure the IAM user or role you're using has `bedrock:InvokeModel` permissions.

### 5. Run the Flask app

```bash
python app.py
```

Open your browser and visit:  
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧪 Sample Prompts

Try asking:

- ✅ *What is Amazon S3?*
- ✅ *How does AWS Lambda work?*
- ❌ *Tell me a joke* → The bot will politely refuse.

---

## ⚙️ Environment Requirements

- Python 3.8+
- AWS CLI installed and configured
- Bedrock model access (e.g., Claude 3.5 Sonnet)

---

## 📦 `requirements.txt`

```
flask
boto3
```

---

## 🔐 IAM Permissions Example

Make sure your IAM policy allows:

```json
{
  "Effect": "Allow",
  "Action": [
    "bedrock:InvokeModel"
  ],
  "Resource": "*"
}
```

---

## 🌍 Live Demo (optional)

You can deploy this app to:

- 🐳 Docker container
- ☁️ AWS EC2 or Elastic Beanstalk
- 🔄 Ngrok (for local testing)

---

## 💡 Future Improvements

- Add streaming response
- Support Claude Haiku & Opus
- Allow user to select models
- Add login/auth system
- Deploy to cloud with HTTPS

---

## 📚 What I Learned

This was my **first chatbot project**, and I learned how to:

- Use **Flask** to build a simple web app
- Interact with **Claude models via AWS Bedrock**
- Handle **API rate limiting and retries**
- Make a clean user interface with **Bootstrap**
- Connect backend to frontend using JSON and AJAX

---

## 📃 License

This project is licensed under the **MIT License**.  
Feel free to use and modify.

---

## 🙌 Acknowledgements

- [Anthropic Claude](https://www.anthropic.com/index/claude)
- [Amazon Bedrock](https://aws.amazon.com/bedrock/)
- [Bootstrap 5](https://getbootstrap.com/)
- [Flask Documentation](https://flask.palletsprojects.com/)

---

## 📬 Contact

Made with ❤️ by [Apikmmar](https://github.com/Apikmmar)  
Feel free to ⭐ this repo and share your feedback!
