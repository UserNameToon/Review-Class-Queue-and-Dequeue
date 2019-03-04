"""*****************************************************************************
Name:    Chanchatri Chaichanathong
course:  CMPT 200 X03L
purpose: Review Class
ID:      3056450
*****************************************************************************"""
'''
this is DQueue class that is used by main() enqueue and dequeue a list element that
contain string that represent job numbers and int representing print numbers. 
the class will allow for checking if the queue is empty or not.
the class contain a linked class - _Node in order to used node fuction of python

This class is base on linkedQueue.py by MacEwan's Computer Science department 
'''
class DQueue:
    class _Node :
        __slots__ = '_element', '_next'
        # Purpose: this method initialize node
        # Parameters: element 
        # Return: none       
        def __init__(self, element, next):
            self._element = element
            self._next = next
    # Purpose: this method initialize DQueue
    # Parameters: none
    # Return: none              
    def __init__(self) :
        self._head = None
        self._tail = None
        self._size = 0
        # Purpose: this method initialize DQueue
        # Parameters: none
        # Return: none     
    def is_empty(self) :
        return self._size == 0 
    # Purpose: this method initialize DQueue
    # Parameters: none
    # Return: none     
    def dequeue(self) :
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty() :
            self._tail = None
        return answer
    # Purpose: this method initialize DQueue
    # Parameters: none
    # Return: none     
    def enqueue(self, e) :
        newest = self._Node(e,None)
        if self.is_empty() :
            self._head = newest
        else :
            self._tail._next = newest
        self._tail = newest
        self._size += 1
# Purpose: this method will similated the fuctionality of network of printers 
# Parameters: none
# Return: none 
def main():
    #crete a DQueue obj
    qJob = DQueue()
    #printers represent as redd and green
    red,green  = [],[]
    #number of jobs
    count = 0
    while True:
        #check if red or green is free, if free auto add job to printers if queue not empty
        if not qJob.is_empty() and len(red) == 0:
            temp = qJob.dequeue()
            red = [temp[0],temp[1]]
        if not qJob.is_empty() and len(green) == 0:
            temp = qJob.dequeue()
            green = [temp[0],temp[1]]
            
        print('\na) Add a print job. '+
              '\nb) Apply a number of cycles (Page print)'+
              '\nc) Display the current status of the printers and jobs left'+
              '\nd) Exit menu')
        
        userInput = input("\nPlease choose one of the option: ")
        
        if userInput == 'a':
            numJob = 0
            while True:
                numJob = input('\nPlease enter number of page for the job: ')
                if  numJob.isdigit() and int(numJob) > 0:
                    break
            count += 1
            qJob.enqueue(['job #' + str(count), int(numJob)])
        
        if userInput == 'b':
            numCycles = 0
            while True:
                numCycles = input('\nPlease enter number of cycle: ')
                if  numCycles.isdigit() and int(numCycles) > 0:
                    break
                
            red = checking_printer(red, numCycles, qJob)
            green = checking_printer(green, numCycles, qJob)
            
            if qJob.is_empty() and len(green) == 0 and len(red) == 0:
                print('\nQueue is empty')
       
        if userInput == 'c':
            print('\nStatus of printers:')
            if len(red) != 0 and red[1] == 0:
                red = []
            if  len(green) != 0 and green[1] == 0:
                green = []
            if len(red) == 0 :
                print('red: empty')
            else:
                print('red: '  + red[0]   + ' page: '+ str(red[1]))
            if len(green) == 0:
                print('green: empty')          
            else: 
                print('green: '+ green[0] + ' page: '+ str(green[1]))
        if userInput == 'd':
            print('\nExiting...')
            break  
# Purpose: this method check the status of the printer
# Parameters: item: printer, numCycles: number of cycles input, qJob: DQueue obj 
# Return: item: printer with job number and amount of works        
def checking_printer(item, numCycles, qJob):
    if len(item) == 0:
        if not qJob.is_empty():
            temp = qJob.dequeue()
            item = [temp[0],temp[1]]
    else:
        for i in range(int(numCycles)):
            if len(item) != 0 and item[1] != 0:
                item[1] -= 1                    
            else:
                item = []
                if not qJob.is_empty() and len(item) != 0:
                    temp = qJob.dequeue()
                    item = [temp[0],temp[1]-1] 
    return item
     