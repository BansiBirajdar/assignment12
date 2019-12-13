'''Design automation script which accept directory name from user and create log file in that
directory which contains information of running processes as its name, PID, Username.
Usage : ProcInfoLog.py Demo
Demo is name of Directory.'''
import sys
import psutil
import time
import os

def Dis(Listproces,path):
    
    if not os.path.exists(path):
        try:        
            os.mkdir(path)
        except:
            pass
        filename=os.path.join(path,"log.txt")
        line = "-"*60
        fobj = open(filename,'w')
        fobj.write(line+"\n")
        fobj.write("Information of running processes as its name, PID, Username\n") 
        fobj.write(line+"\n\n")
        for k in Listproces:
            fobj.write(str(k)+"\n")
        fobj.close()
    
        
        
    
def ProcessDisplay():
    listprocess=[]
    
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            #pinfo['vms']=proc.memory_info().vms/(1024*1024)
            
            listprocess.append(pinfo);
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    return listprocess

def main():
    print("Marvellous Infosystems : Python Automation and Machine Learing ")
    print("\n Application name:",sys.argv[0])
    print("Process Monitor")

    if(len(sys.argv)==1):
        print("Error :invalid number of arguments")
        exit()
    if(len(sys.argv)!=2):
        if(sys.argv[1]=='-h') or(sys.argv[1]=='-H'):
            print("This script which accept directory name from user and create log file in that\
directory which contains information of running processes as its name, PID, Username")
            exit()
        if(sys.argv[1]=='-u') or (sys.argv[1]=='-U'):
            print("Usage : ProcInfoLog.py “Demo”")
            exit()
    try:
        start=time.time()
        Listproces = ProcessDisplay()
        Dis(Listproces,sys.argv[1])
        end=time.time()
        print("Time::",end-start)
    except ValueError:
            print("Error : Invalied datatype of input ")
    except Exception:
            print("Error : Invalid input ")
    finally:
            print("Thank You  !!!!!")
if __name__=="__main__":
    main()