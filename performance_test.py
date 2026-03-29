# load_test.py

import requests
import time

URL = "http://127.0.0.1:8000/"

def load_test(num_requests=50):

    start_time = time.time()
    success = 0

    for i in range(num_requests):
        res = requests.get(URL)
        if res.status_code == 200:
            success += 1

    total_time = time.time() - start_time

    print(f"Total Requests: {num_requests}")
    print(f"Successful: {success}")
    print(f"Average Time: {total_time/num_requests:.4f} sec")


if __name__ == "__main__":
    load_test(50)