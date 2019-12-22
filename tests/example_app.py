import time
from appear import helper


for i in range(20):
    print(f"Sending message {i}")
    helper("text", {"message": f"Message {i}"})
    time.sleep(1)
