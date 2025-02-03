# Using multiprocessing
import multiprocessing

def worker(n):
    print(f"Worker {n} running")

if __name__ == "__main__":
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()