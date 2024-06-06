"""
pycnanorestore will use pydebuggerconfig to reprogram the connected Curiosity Nano board and device configs.
"""

SUPPORTED_KITS = [
    {'Name' : 'AVR16EB32 Curiosity Nano',
     'DeviceConfig' : 'device-configs//AVR16EB32-device-blob.xml',
     'BoardConfig' : 'board-configs//AVR16EB32-CNANO.xml'
    }, 
    {'Name' : 'AVR64DU32 Curiosity Nano',
     'DeviceConfig' : 'device-configs//AVR64DU32-device-blob.xml',
     'BoardConfig' : 'board-configs//AVR64DU32-CNANO.xml'
    }
    ]

from pykitinfo.pykitinfo import detect_edbg_kits
from pydebuggerconfig import backend

print ("Welcome to pycnanorestore")
print ("This utility can be used to install latest board and device configurations")

kits = detect_edbg_kits()
if len(kits) > 1:
    raise Exception("Connect only one supported Curiosity Nano kit for this procedure")

kit = kits[0]
kitname = kit['debugger']['kitname']
kitserial = kit['usb']['serial_number']
print (f"Detected: {kitname}")

serial_number = ""
for kit in SUPPORTED_KITS:
    if kitname == kit['Name']:
        serial_number = kitserial
        break

if not serial_number:
    raise Exception(f"Kit {kitname} not supported")

configurator = backend.Backend()
print("Writing device config")
configurator.write_device_config(kit['DeviceConfig'])
print("Writing board config")
configurator.write_board_config(kit['BoardConfig'])

print("pycnanorestore done - OK")

