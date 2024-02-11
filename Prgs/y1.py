import multiprocessing

def worker(num):
    """Function to be executed by each process"""
    return num * 2

if __name__ == "__main__":
    # Create a pool of processes
    pool = multiprocessing.Pool(processes=4)

    # Map the worker function to multiple arguments
    results = pool.map(worker, [1, 2, 3, 4, 5])

    # Close the pool and wait for all processes to finish
    pool.close()
    pool.join()

    print("Results:", results)
