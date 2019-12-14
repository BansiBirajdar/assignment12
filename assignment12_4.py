'''Design automation script which accept directory name and mail id from user and create log
file in that directory which contains information of running processes as its name, PID,
Username. After creating log file send that log file to the specified mail.
Usage : ProcInfoLog.py Demo Marvellousinfosystem@gmail.com
Demo is name of Directory.
marvellousinfosystem@gmail.com is the mail id'''
import os
import time
import psutil
import mailcheck
import Conn
import smtplib
import sys
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


def ProcessLog(Listproces,path):
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except:
            pass
    filename=os.path.join(path,"logfile%s.log"%(time.time()))
    line = "-"*60
    fobj = open(filename,'w')
    fobj.write(line+"\n")
    fobj.write("Information of running processes as its name, PID, Username\n") 
    fobj.write(line+"\n\n")
    for k in Listproces:
        fobj.write(str(k)+"\n")
    fobj.close()
    return filename

def ProcessDisplay():
    listprocess=[]
    
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            listprocess.append(pinfo);
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    return listprocess
def MailSender(filename,toaddr,time):
    try:
        fromaddr = "bansiddha7@gmail.com"
        
        msg = MIMEMultipart()
        
        msg['From'] = fromaddr
        
        msg['To'] = toaddr
        
        body ="""
        Hello %s
        Welcome To Marvellour Infosystems.
        Please find attached document which contains 
        Log of Running Process.
        Log file is Created at :%s
        
        This is auto Gennerated Mail.
        
        Thanks & Regards,
        Bansiddha Chadrakant Birajdar
        Gmail:%s
        Student of Marvellour Infosystems
        """%(toaddr,time,fromaddr)
        
        Subject="""
        Marvellous Infosystem Process log Generated at:%s
        """%(time)
        
        msg['Subject'] =Subject
        
        msg.attach(MIMEText(body, 'plain'))
        
        attachment = open(filename, "rb")
        
        p = MIMEBase('application', 'octet-stream')
        
        p.set_payload((attachment).read())
        
        encoders.encode_base64(p)
        
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        
        msg.attach(p) 

        s = smtplib.SMTP('smtp.gmail.com', 587) 

        s.starttls() 

        s.login(fromaddr, "password") 

        text = msg.as_string() 

        s.sendmail(fromaddr, toaddr, text) 

        s.quit()
        
        print("Log file successfully sent through Mail")
    except Exception as E:
        print("Unable to send mail.",E)

def main():
    print("Marvellous Infosystems : Python Automation and Machine Learing ")
    print("\n Application name:",sys.argv[0])
    print("+++++++++- Process Monitor -+++++++++")

    
    if(len(sys.argv)<=2):
        if(len(sys.argv)==1):
            print("Error :invalid number of arguments")
            exit()
        if(sys.argv[1]=='-h') or(sys.argv[1]=='-H'):
            print("This script which accept directory name and mail id from user and create log\
file in that directory which contains information of running processes as its name, PID,\
Username. After creating log file send that log file to the specified mail.")
            exit()
        if(sys.argv[1]=='-u') or (sys.argv[1]=='-U'):
            print("Usage : ProcInfoLog.py Demo Marvellousinfosystem@gmail.com")
            exit()
        else:
            print("Error :invalid number of arguments")
            exit()
    try:
    
        if mailcheck.check(sys.argv[2]):
            connected=Conn.is_connected()
            if connected:
                start=time.time()
                Listproces = ProcessDisplay()
                filename=ProcessLog(Listproces,sys.argv[1])
                print(filename)
                MailSender(filename,sys.argv[2],time.ctime())
                end=time.time()
                print("Time::",(end-start))
            else:
                print("NO internet Connetion.....")
        else:
            print("Invalied email please enter the valied email")
    except ValueError:
            print("Error : Invalied datatype of input ")
    except Exception:
            print("Error : Invalid input ")
    finally:
            print("Thank You  !!!!!")
if __name__=="__main__":
    main()