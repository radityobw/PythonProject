import threading
import requests
import time

# Target URL yang akan diuji
TARGET_URL = "http://example.com"
# Jumlah permintaan total
TOTAL_REQUESTS = 100000000
# Jumlah thread (semakin banyak, semakin agresif)
THREAD_COUNT = 10000000

# Fungsi untuk mengirim permintaan HTTP GET
def send_request():
    try:
        response = requests.get(TARGET_URL)
        print(f"Status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Fungsi utama untuk mengatur thread
def stress_test():
    threads = []
    for _ in range(TOTAL_REQUESTS):
        t = threading.Thread(target=send_request)
        threads.append(t)
        t.start()

        # Batasi jumlah thread aktif
        while threading.active_count() > THREAD_COUNT:
            time.sleep(0.01)

    for t in threads:
        t.join()

if __name__ == "__main__":
    start_time = time.time()
    stress_test()
    duration = time.time() - start_time
    print(f"Completed {TOTAL_REQUESTS} requests in {duration:.2f} seconds")