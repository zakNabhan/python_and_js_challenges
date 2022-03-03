'''
Erstellen Sie eine Funktion,
die Spannung und Strom aufnimmt und die berechnete Leistung zurückgibt.
'''


def circuit_power(voltage, current):
    """
    :param voltage:
    :param current:
    :return:
    """
    return voltage * current


print(circuit_power(230, 10))
print(circuit_power(110, 3))
print(circuit_power(480, 20))


# other version
circuit_power=lambda v,c:v*c