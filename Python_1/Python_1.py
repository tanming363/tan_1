
import time
import webbrowser 

breaks =3
count = 0

print("started on"+time.ctime())
while(count<breaks):
 time.sleep(5)
 webbrowser.open("https://www.youtube.com/watch?v=2gcsgfzqN8k")

 count=count+1