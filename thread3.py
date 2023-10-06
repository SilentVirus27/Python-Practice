#Q4. Write a program to print current time of each thread with its name
import threading
import time

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# Create two threads as follows
try:
   #threading.Thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   #threading.Thread.start_new_thread( print_time, ("Thread-2", 4, ) )
   t1 = threading.Thread(target=print_time, args=('t1',100,))
   t2 = threading.Thread(target=print_time, args=('t2',200,)) 
  
   # starting threads
   t1.start()
   t2.start()
except:
   print ("Error: unable to start thread")

while 1:
   pass
