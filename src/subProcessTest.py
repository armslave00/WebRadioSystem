import subprocess
import sys
# subprocess.call(["node", "test.js"])
# output = subprocess.check_output(
#   "ls non_existent_file; exit 0",
#   stderr=subprocess.STDOUT)
# print("OUTPUT: " + output)

output = subprocess.check_output(["node", "test.js"]).decode(sys.stdout.encoding)
print("OUTPUT: " + output)