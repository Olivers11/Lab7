import pyfirmata, time
from alert_window import *
_sensor = 0
_led = 13
_port = "/dev/ttyUSB0"
_target = pyfirmata.Arduino(_port)
_target.analog[_sensor].mode = pyfirmata.INPUT
_target.digital[_led].mode = pyfirmata.OUTPUT
_iterator = pyfirmata.util.Iterator(_target)
_iterator.start()

while True:
    if _target.analog[_sensor].read() == None:
        pass
    else:
        result = _target.analog[_sensor].read()
        # result = pow(4, 10) * result
        print(f"Obtained Result {result}")
        if result > 0.0100:
            _target.digital[_led].write(1)
            time.sleep(0.1)
            showMessage()
        else:
            _target.digital[_led].write(0)

 
