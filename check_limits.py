def check_range(value, min_value, max_value, error_message):
    if value < min_value or value > max_value:
        print(error_message)
        return False
    return True

def battery_is_ok(temperature, soc, charge_rate):
    return (check_range(temperature, 0, 45, 'Temperature is out of range!') and
            check_range(soc, 20, 80, 'State of Charge is out of range!') and
            check_range(charge_rate, 0, 0.8, 'Charge rate is out of range!'))

if __name__ == '__main__':
    assert(battery_is_ok(25, 70, 0.7) is True)
    assert(battery_is_ok(50, 85, 0) is False)
