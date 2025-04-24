import os
import csv
import smtplib
import mimetypes
import re
from pathlib import Path
from dotenv import load_dotenv
from email.message import EmailMessage
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Load environment variables
load_dotenv()
EMAIL = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("EMAIL_PASSWORD")

# Load TinyLlama model
model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def generate_email(prompt):
    input_prompt = f"Write a professional email for: {prompt}"
    result = generator(input_prompt, max_length=512, do_sample=True, temperature=0.7)
    return result[0]['generated_text'].replace(input_prompt, "").strip()

def send_email(to, subject, body, attachment_dir=None):
    msg = EmailMessage()
    msg["From"] = EMAIL
    msg["To"] = to
    msg["Subject"] = subject
    msg.set_content(body)

    if attachment_dir and os.path.isdir(attachment_dir):
        for filename in os.listdir(attachment_dir):
            filepath = os.path.join(attachment_dir, filename)
            if os.path.isfile(filepath):
                mime_type, _ = mimetypes.guess_type(filepath)
                if mime_type is None:
                    mime_type = "application/octet-stream"
                maintype, subtype = mime_type.split("/", 1)
                with open(filepath, "rb") as f:
                    msg.add_attachment(f.read(), maintype=maintype, subtype=subtype, filename=filename)
                print(f"📎 Attached: {filename}")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL, PASSWORD)
        smtp.send_message(msg)
        print(f"✅ Email sent to {to}")

def main():
    print("📧 Welcome to AI Email Agent (TinyLlama Edition)")
    subject = input("✉️ Enter subject: ")
    attach = input("📎 Include attachments from 'attachments/' folder? (yes/no): ").strip().lower()

    # Choose between AI-generated or file-based body
    choice = input("🧠 Use AI to generate email body? (yes/no): ").strip().lower()
    if choice == 'yes':
        prompt = input("📝 Describe the email (prompt): ")
        print("\n🧠 Generating email...")
        body = generate_email(prompt)
    else:
        try:
            with open("email_body.txt", "r", encoding="utf-8") as f:
                body = f.read().strip()
        except FileNotFoundError:
            print("❌ Error: email_body.txt file not found.")
            return

    print(f"\n📄 Email Content Preview:\n{'-'*40}\n{body}\n{'-'*40}")
    confirm = input("🚀 Confirm sending email to all recipients in emails.csv? (yes/no): ").strip().lower()
    if confirm != 'yes':
        print("❌ Cancelled.")
        return

    with open("emails.csv", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            recipient = row[0].strip()
            if not is_valid_email(recipient):
                print(f"⚠️ Skipping invalid email: {recipient}")
                continue
            send_email(recipient, subject, body, attachment_dir="attachments" if attach == 'yes' else None)

    print("\n✅ All emails sent successfully!")

if __name__ == "__main__":
    main()
