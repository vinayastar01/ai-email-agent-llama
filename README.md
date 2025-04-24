# 🧠 AI Email Agent (TinyLlama Edition)

This is a Python-based email automation tool powered by the [TinyLlama-1.1B-Chat](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0) model. It generates and sends emails based on a prompt or a predefined text file, with optional attachments. Built using Hugging Face Transformers and Python's built-in `smtplib`.

---

## 📁 Folder Structure

```
ai-email-agent-llama/
│
├── attachments/             # Folder to store all email attachments
├── emails.csv               # CSV file containing recipient emails (one per line)
├── email_body.txt           # Optional: Contains full email body text if not using AI
├── .env                     # Environment variables (email credentials)
├── main.py                  # Main script to run the email agent
├── requirements.txt         # All Python dependencies
└── README.md                # This documentation
```

---

## 🔧 Prerequisites

- Python 3.8+
- A Gmail account with [App Passwords enabled](https://support.google.com/mail/answer/185833?hl=en)
- Access to Hugging Face to download TinyLlama model

---

## 🛠️ Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/ai-email-agent-llama.git
cd ai-email-agent-llama
```

2. **Create a Virtual Environment**

```bash
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows
```

3. **Install Requirements**

```bash
pip install -r requirements.txt
```

4. **Configure Environment Variables**

Create a `.env` file and add your Gmail credentials:

```env
EMAIL_ADDRESS=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
```

5. **Prepare Your Data**

- Add recipient emails (one per line) to `emails.csv`.
- To **use AI-generated content**, write a prompt when the app runs.
- To **use a custom email body**, write your message in `email_body.txt`.

6. **Run the App**

```bash
python main.py
```

---

## 📤 Features

- 📬 Sends emails to all recipients in a CSV.
- 🤖 Generates professional emails using TinyLlama.
- 📎 Adds attachments from the `attachments/` folder.
- ✅ Validates emails before sending.

---

## 🧪 Example Usage

```
📝 Describe the email (prompt): Invitation for a project collaboration.
✉️ Enter subject: Exciting Collaboration Opportunity
📎 Include attachments? (yes/no): yes
🚀 Confirm sending email to all recipients in emails.csv? (yes/no): yes
```

✅ Email sent to recipient@example.com  
📎 Attached: project_overview.pdf  

---

## 🔒 Security Note

Do **NOT** hardcode email credentials. Always use `.env` and App Passwords (not your main password).

---

## 🛠 Future Features

- Web UI for sending emails
- Deployment on Heroku or Render
- Scheduling emails with a CRON job
- Email open tracking (via tracking pixels)

---

## 🤝 Contributing

Pull requests and suggestions are welcome. Let's improve it together!

---

## 📄 License

This project is licensed under the MIT License.