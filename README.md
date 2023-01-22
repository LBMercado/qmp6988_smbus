# Notice
Cloned modified copy from repository [piqmp6988 (Author: Langur)](https://github.com/Langur/piqmp6988)\
This implementation simply abstracts the i2c communication interface in the sensor.\
Motivation is to use the SMBus instead of pgpiod since it is not compatible with non-RPi SBCs
# PiQmp6988's Methods

## Constructor(config={})

'config' is dictionary type.

### 'address'

Configure I2C address of QMP6988.

* Address.LOW.value
    * I2C address is 0x70
    * Default
* Address.HIGH.value
    * I2C address is 0x56

### 'filter'

Configure Infinite Impulse Response(IIR) Filter coefficient of QMP6988.

* Filter.COEFFECT_OFF.value
    * Do not use IIR Filter
    * Default
* Filter.COEFFECT_2.value
    * IIR filter coefficient is 2
* Filter.COEFFECT_4.value
    * IIR filter coefficient is 4
* Filter.COEFFECT_8.value
    * IIR filter coefficient is 8
* Filter.COEFFECT_16.value
    * IIR filter coefficient is 16
* Filter.COEFFECT_32.value
    * IIR filter coefficient is 32

### 'mode'

Configure Power Mode of QMP6988.

* Powermode.SLEEP.value
    * Power Mode is SLEEP
    * Default
* Powermode.FORCE.value
    * Power Mode is Force
* Powermode.NORMAL.value
    * Power Mode is Normal

### 'pressure'

Configure average times for pressure measurement of QMP6988.

* Oversampling.SKIP.value
    * Do not measure pressure
    * Default
* Oversampling.X1.value
    * Single Shot value
* Oversampling.X2.value
    * Average 2 times for mesurment value
* Oversampling.X4.value
    * Average 4 times for mesurment value
* Oversampling.X8.value
    * Average 8 times for mesurment value
* Oversampling.X16.value
    * Average 16 times for mesurment value
* Oversampling.X32.value
    * Average 32 times for mesurment value
* Oversampling.X64.value
    * Average 64 times for mesurment value

### 'temperature'

Configure average times for temperature measurement of QMP6988.

* Oversampling.SKIP.value
    * Do not measure temperature
    * Use 25.0 celsius value when 'pressure' measure
    * Default
* Oversampling.X1.value
    * Single Shot value
* Oversampling.X2.value
    * Average 2 times for mesurment value
* Oversampling.X4.value
    * Average 4 times for mesurment value
* Oversampling.X8.value
    * Average 8 times for mesurment value
* Oversampling.X16.value
    * Average 16 times for mesurment value
* Oversampling.X32.value
    * Average 32 times for mesurment value
* Oversampling.X64.value
    * Average 64 times for mesurment value

## read()

Read temperature and pressure.
Return value is dictionary type.

### 'temperature'

* OK
    * Type: float
    * Celsius temperature value [℃]
* NG
    * Type: False

### 'pressure'

* OK
    * Type: float
    * Atmospheric pressure value [hPa]
* NG
    * Type: False

# Sample

Run `sudo pigpiod` before running the sample.

## Indoor navigation (from QMP6988 Datasheet)

.. code-block:: shell

    # -*- coding: utf-8 -*-
    import piqmp6988 as QMP6988
    from piqmp6988.smbus_intf import Smbus
    import time
    
    config = {
        'temperature' : QMP6988.Oversampling.X4.value,
        'pressure' :    QMP6988.Oversampling.X32.value,
        'filter' :      QMP6988.Filter.COEFFECT_32.value,
        'mode' :        QMP6988.Powermode.NORMAL.value
    }
    
    bus = Smbus()
    obj = QMP6988.PiQmp6988(bus, config)
    
    try:
        while True:
            value = obj.read()
            if (isinstance(value['temperature'], float)):
                print("%8.2f" % round(valueb['temperature'], 2))
            if (isinstance(valueb['pressure'], float)):
                print("%8.2f" % round(valueb['pressure'], 2))
            time.sleep(10)
    except KeyboardInterrupt:
        pass


