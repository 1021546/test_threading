import threading

# 建立 RLock
rlock = threading.RLock()

# 取得 rlock
rlock.acquire()

# 不能讓多個執行緒同時進的工作...

# 重複取得 rlock
rlock.acquire()

# 不能讓多個執行緒同時進的工作...

# 釋放 rlock
rlock.release()

# 不能讓多個執行緒同時進的工作...

# 再次釋放 rlock
rlock.release()

# https://blog.gtwang.org/programming/python-threading-multithreaded-programming-tutorial/