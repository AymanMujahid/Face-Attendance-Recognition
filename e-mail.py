import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os
import schedule
import time
import logging


logging.basicConfig(filename='attendance_email.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def send_email_with_attachment(subject, body, to_email, file_path):
    try:
        from_email = "email@example.com"
        from_password = "email_password"

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        attachment = open(file_path, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename= {os.path.basename(file_path)}')
        msg.attach(part)


        server = smtplib.SMTP('smtp.example.com', 587)  
        server.starttls()
        server.login(from_email, from_password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()

        logging.info("تم إرسال البريد الإلكتروني بنجاح إلى %s", to_email)

    except Exception as e:
        logging.error("حدث خطأ أثناء محاولة إرسال البريد الإلكتروني: %s", str(e))

def job():
    try:
        file_path = "employee_attendance.xlsx"
        
        send_email_with_attachment(
            subject="Employee Attendance Report",
            body="Dear HR,\n\nPlease find attached the latest employee attendance report.\n\nBest regards,\nAyman",
            to_email="hr@example.com",
            file_path=file_path
        )
        logging.info("تم إرسال البريد الإلكتروني بنجاح في الساعة 12 ظهرًا.")

    except Exception as e:
        logging.error("فشل في إرسال البريد الإلكتروني: %s", str(e))

schedule.every().day.at("12:00").do(job)

if __name__ == "__main__":
    logging.info(" بدأ. سيتم إرسال البريد الإلكتروني تلقائيًا كل يوم في الساعة 12 ظهرًا.")
    while True:
        schedule.run_pending()
        time.sleep(60)  