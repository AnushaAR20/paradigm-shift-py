def check_parameter(value, min_val, max_val, parameter_name):
    if value < min_val or value > max_val:
        print(f'{parameter_name} is out of range!')
        return False
    return True

def battery_is_ok(temperature, soc, charge_rate):
    parameters = [
        (temperature, 0, 45, 'Temperature'),
        (soc, 20, 80, 'State of Charge'),
        (charge_rate, 0, 0.8, 'Charge Rate')
    ]
    
    for value, min_val, max_val, name in parameters:
        if not check_parameter(value, min_val, max_val, name):
            return False
            
    return True

if __name__ == '__main__':
    assert(battery_is_ok(25, 70, 0.7) is True)
    assert(battery_is_ok(50, 85, 0) is False)
