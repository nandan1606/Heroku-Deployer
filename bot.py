print("starting")
from subprocess import Popen as run
import os 
import shutil
import base64 as r
from apscheduler.schedulers.background import BackgroundScheduler
from os import execvp,sys , execl,environ
from sys import executable
from dotenv import load_dotenv
load_dotenv("config.env")
#Scheduler can  be used to automatically restart the program if any kind if memory issues
def restar():
     os.system("rm -rf /tmp/*")
     if not os.path.exists("/tmp/thumbnails/"):
        os.mkdir("/tmp/thumbnails/")
     execl(executable, executable,"bot.py")

#scheduler = BackgroundScheduler()
#scheduler.add_job(restar, "interval", minutes=30)
#scheduler.start()
try:
    runrepo=os.environ['repo_url']
    runcmd=os.environ['run_cmd']
except KeyError as e:
     sys.exit(f"Important environment variables are missing {e}")
x=f"git clone {runrepo} repo"
tx=r.b64encode(x.encode('ascii')).decode('ascii')
if os.path.exists("/app/repo/"):
   shutil.rmtree("/app/repo/")
   k= os.system(r.b64decode(tx.encode('ascii')).decode('ascii'))
   print(k)
   os.chdir("repo/")
   run(f"pip3 install -r requirements.txt && python3 -m {runcmd}",shell=True,text=True)

else:
     k= os.system(r.b64decode(tx.encode('ascii')).decode('ascii'))
     print(k)
     os.chdir("repo/")
     k=os.system(f"pip3 install -r requirements.txt && python3 -m {runcmd}")
     print(k)

print("service stoped")
