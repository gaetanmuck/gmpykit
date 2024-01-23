import time
import gmpykit as kit

eta = kit.Eta()

eta.begin(10, 'Testing')
for i in range(10):
    time.sleep(0.2)
    eta.iter()
eta.end()