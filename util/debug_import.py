import sys
print("Python executable:", sys.executable)
print("Python sys.path:")
for p in sys.path:
    print(" ", p)

try:
    import moviepy
    print("moviepy import success!")
    print("moviepy location:", moviepy.__file__)
except Exception as e:
    print("moviepy import failed:", e)
