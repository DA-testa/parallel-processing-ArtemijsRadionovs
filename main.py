# python3
from queue import PriorityQueue
from threading import Thread


def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    priorQ = PriorityQueue()

    for i in range(n):
        if i < m:
            priorQ.put((data[i], i))
            output.append((i, 0))
            
    for i in range(n, m):
        duration, thread_idx = priorQ.get()
        start_time = duration
        output.append((thread_idx, start_time))
        priorQ.put((duration + data[i], thread_idx))

    while not priorQ.empty():
        duration, thread_idx = priorQ.get()
        output.append((thread_idx, duration))

    return output


def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    
    n, m = map(int, input().split())
    # print(m)

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line

    for i, j in result:
        print(i, j)

        
if __name__ == "__main__":
    main()
