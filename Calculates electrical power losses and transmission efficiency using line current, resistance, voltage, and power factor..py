voltage = float(input("Voltage (V): "))
current = float(input("Current (A): "))
resistance = float(input("Line resistance (ohms): "))
pf = float(input("Power factor: "))

if voltage <= 0 or current < 0 or resistance < 0:
    print("Invalid electrical values")
elif not 0 <= pf <= 1:
    print("Invalid power factor")
else:
    input_power = voltage * current * pf
    losses = current ** 2 * resistance
    output_power = input_power - losses

    print("Input power:", round(input_power, 2), "W")
    print("Power losses:", round(losses, 2), "W")

    if input_power > 0 and output_power >= 0:
        efficiency = output_power / input_power * 100
        print("Efficiency:", round(efficiency, 2), "%")
    else:
        print("Check the input parameters")
