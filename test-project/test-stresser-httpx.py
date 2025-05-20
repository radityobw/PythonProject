import asyncio
import httpx
import time

# Target URL
TARGET_URL = "https://example.com"
# Jumlah total permintaan yang akan dikirim
TOTAL_REQUESTS = 100000
# Jumlah permintaan bersamaan (concurrency)
CONCURRENCY = 10000

# Fungsi untuk mengirim satu request
async def send_request(client, i):
    try:
        response = await client.get(TARGET_URL, timeout=10)
        print(f"[{i}] Status: {response.status_code}")
    except httpx.RequestError as e:
        print(f"[{i}] Request error: {e}")

# Fungsi utama
async def stress_test():
    async with httpx.AsyncClient() as client:
        tasks = []
        for i in range(TOTAL_REQUESTS):
            task = asyncio.create_task(send_request(client, i))
            tasks.append(task)

            # Batasi jumlah task yang aktif sekaligus
            if len(tasks) >= CONCURRENCY:
                await asyncio.gather(*tasks)
                tasks = []

        # Sisa task yang belum dieksekusi
        if tasks:
            await asyncio.gather(*tasks)

if __name__ == "__main__":
    start = time.time()
    asyncio.run(stress_test())
    print(f"Completed {TOTAL_REQUESTS} requests in {time.time() - start:.2f} seconds")