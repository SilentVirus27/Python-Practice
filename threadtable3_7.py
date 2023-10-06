#create table of 3 and 7 using thread and print it
import threading
def print_table(num):
    """
    function to print multiplication table of given num
    """
    for i in range(1,10):
        print(i,'*',num,'=',i*num)

if __name__=="__main__":
    #creating thread
    t1=threading.Thread(target=print_table, args=(3,))
    t2=threading.Thread(target=print_table, args=(7,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Done!")
