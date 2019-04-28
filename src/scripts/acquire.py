import cb
import sound
import time
import struct
import console
import numpy as np
import matplotlib.pyplot as plt


class SensorTag(object):
    def __init__(self):
        self.peripheral = None
        self.buffer = []

    def did_discover_peripheral(self, p):
        print(p.name)
        if p.name and 'Sensor_Tag' in p.name and not self.peripheral:
            self.peripheral = p
            print('Connecting to heart rate monitor...')
            cb.connect_peripheral(p)

    def did_connect_peripheral(self, p):
        print('Connected:', p.name)
        print('Discovering services...')
        p.discover_services()

    def did_fail_to_connect_peripheral(self, p, error):
        print('Failed to connect: %s' % (error,))

    def did_disconnect_peripheral(self, p, error):
        print('Disconnected, error: %s' % (error,))
        self.peripheral = None

    def did_discover_services(self, p, error):
        for s in p.services:
            print(s.uuid)
            p.discover_characteristics(s)

    def did_discover_characteristics(self, s, error):
        print('Did discover characteristics...')
        for c in s.characteristics:
            print(c.uuid)
            if '6E400003' in c.uuid:
                print('Connecting:', c.uuid)
                self.peripheral.set_notify_value(c, True)

    def did_update_value(self, c, error):
        if '6E400003' in c.uuid:
            try:
                parts = struct.unpack('>hhhhhhh', c.value)
                self.buffer.append(parts)
                print(parts)
            except ValueError:
                print(c.value)


name = console.input_alert('Start measurement', input='test')
filename = name + '.csv'

tag = SensorTag()
cb.set_central_delegate(tag)

print('Scanning for peripherals...')
cb.scan_for_peripherals()

console.alert('Measurement', '', 'Stop', hide_cancel_button=True)
cb.reset()

data = np.array(tag.buffer)
n = data.shape[0]
t = np.array([x*10 for x in range(n)])*0.001
accel = data[:,0:3]/2048
gyro  = data[:,4:7]/16.4
temp  = data[:,3]/340 + 36.53

csv = np.hstack((t[:, np.newaxis], accel, gyro, temp[:, np.newaxis]))
header = ','.join(['time', 'ax', 'ay', 'az', 'gx', 'gy', 'gz','temperature'])
np.savetxt(name + '.csv', csv, delimiter=',', header=header, fmt='%3.8f')
print('csv: ' + name + '.csv')

plt.figure()
for i, color, label in zip(range(3), 'rgb', 'XYZ'):
    plt.plot(t, accel[:,i], color, label=label, lw=1)
plt.grid(True)
plt.title(name + ' (Acceleration)')
plt.xlabel('t')
plt.ylabel('G')
plt.legend()
plt.show()
plt.savefig(name + '_accel.png')

plt.figure()
for i, color, label in zip(range(3), 'rgb', 'XYZ'):
    plt.plot(t, gyro[:,i], color, label=label, lw=1)
plt.grid(True)
plt.title(name + ' (Angular Speed)')
plt.xlabel('t')
plt.ylabel('deg/s')
plt.legend()
plt.show()
plt.savefig(name + '_gyro.png')



