import os
# Create required folders

try:
    os.mkdir("generated_outputs")
except:
    print("dir creation failed")

try:
    os.mkdir("data")
except:
    print("dir creation failed")