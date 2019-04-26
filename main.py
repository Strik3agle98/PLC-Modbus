from pyModbusTCP.client import ModbusClient
try:
    c = ModbusClient(host="localhost", port=502)
except ValueError:
    print("Error with host or port params")