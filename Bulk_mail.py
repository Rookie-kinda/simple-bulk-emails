def confirmation_mail(From, to, password, subject, body, attachment_file = None):
    import smtplib
    import ssl
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
  
    email = MIMEMultipart()
    email["From"] = From
    email["To"] = to
    email["Subject"] = subject
    context = ssl.create_default_context()
    email.attach(MIMEText(body, 'plain'))

    if attachment_file:  # to send attachments
        attachment = open(attachment_file, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {attachment_file}")
        email.attach(part)
        
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as email_mail:
        email_mail.login(From, password)
        email_mail.sendmail(From, to, email.as_string())
        email_mail.quit()
