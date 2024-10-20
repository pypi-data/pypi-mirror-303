from concurrent.futures import Future, ProcessPoolExecutor



def test_p1():
    a = 114
    b = 514
    print(a, b)





def main():
    pool = ProcessPoolExecutor(max_workers=2)
    future = pool.submit(test_p1)
    print(future.result())
    pool.shutdown(wait=True)

if __name__ == '__main__':
    main()