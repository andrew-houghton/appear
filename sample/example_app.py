import time
from appear import helper


for i in range(100):
    start = time.time()
    helper("http://localhost:5000/broadcast", "numbers", {"num": f"Message {i}"})
    time.sleep(0.25)
