from multiprocessing import Pool

import time

def f(n):
    sum = 0

    for x in range(1000):
        sum += x*x
    return sum

if __name__ == "__main__":
    t1 = time.time()
    p = Pool(processes=4) #change the value of noof processes to check the effect
    result = p.map(f,range(100000))
    p.close()
    p.join()

    print("Pool took: ", time.time()-t1)

    t2 = time.time()
    result2 = []
    for x in range(100000):
        result2.append(f(x))

    print("Serial Processing took: ", time.time() - t2)
