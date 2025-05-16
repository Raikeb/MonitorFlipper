import win32api

i = 0
device = win32api.EnumDisplayDevices(None, i)
while device.DeviceName:
    print(f"Monitor {i}: {device.DeviceName} - Ativo: {bool(device.StateFlags & 1)}")
    i += 1
    device = win32api.EnumDisplayDevices(None, i)