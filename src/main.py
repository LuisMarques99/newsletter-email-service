import os, smtplib, ssl, json

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email() -> None:
    """
    Email sender
    :return: None
    """
    SENDER_PLATFORM = "Gmail"
    RECEIVER_EMAIL_ADDRESS = "carloshps@outlook.pt"
    # RECEIVER_EMAIL_ADDRESS = "luisserafim99@hotmail.com"

    with open("secrets.json", "r") as secrets_file:
        secrets = json.load(secrets_file)
        SENDER_EMAIL_ADDRESS = secrets["senderEmailAddress"]
        SENDER_PASSWORD = secrets["senderPassword"]

    with open("platforms.json", "r") as platforms_file:
        platforms = json.load(platforms_file)
        for platform in platforms:
            if platform["name"] == SENDER_PLATFORM:
                SENDER_SMTP = platform["smtp"]
                break

    # Create MIMEMultipart object
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Python Test Email"
    msg["From"] = SENDER_EMAIL_ADDRESS
    msg["To"] = RECEIVER_EMAIL_ADDRESS
    # filename = os.path.join("..", "files", "invoice.pdf")

    # HTML Message Part
    html_message = str()
    with open(os.path.join("..", "files", "email_content.html"), "r") as html_file:
        for row in html_file:
            html_message += f"{row}\n"

    html_content = MIMEText(html_message, "html")
    msg.attach(html_content)

    # # Add Attachment
    # with open(filename, "rb") as attachment_file:
    #     attachment = MIMEBase("application", "octet-stream")
    #     attachment.set_payload(attachment_file.read())

    # encoders.encode_base64(attachment)

    # # Set attachment headers
    # attachment.add_header(
    #     "Content-Disposition",
    #     "attachment", filename=filename
    # )
    # msg.attach(attachment)

    # PORT = 465 # SSL
    PORT = 587  # TLS/STARTTLS
    CONTEXT = ssl.create_default_context()

    # Create secure SMTP connection
    server = smtplib.SMTP(SENDER_SMTP, PORT)
    try:
        server.starttls(context=CONTEXT)
        # Login
        server.login(SENDER_EMAIL_ADDRESS, SENDER_PASSWORD)
        # Send email
        server.sendmail(SENDER_EMAIL_ADDRESS, RECEIVER_EMAIL_ADDRESS, msg.as_string())
        print("Email sent")
    except Exception as exception:
        print(exception)
    finally:
        server.quit()


def main() -> None:
    """
    Main function
    :return: None
    """
    send_email()
    # for i in range(20):
    #     send_email()
    #     time.sleep(1)


if __name__ == "__main__":
    main()
