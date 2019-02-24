import glib

from pyudev import Context, Monitor
from usb import Usb

try:
    from pyudev.glib import MonitorObserver

    def device_event(observer, device):
        print 'event {0} on device {1}'.format(device.action, device)
        usb.get_mount_points()
except:
    from pyudev.glib import GUDevMonitorObserver as MonitorObserver

    def device_event(observer, action, device):
        print 'event {0} on device {1}'.format(action, device)


def get_usb_devices():
    context = Context()
    monitor = Monitor.from_netlink(context)
    monitor.filter_by(subsystem='usb')
    observer = MonitorObserver(monitor)
    observer.connect('device-event', device_event)
    monitor.start()
    glib.MainLoop().run()


if __name__ == '__main__':
     get_usb_devices()