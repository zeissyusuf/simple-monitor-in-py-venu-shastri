def check_temp(temperature):
  if temperature < 0 or temperature > 45:
    print('Temperature is out of range!')
    return False

def check_soc(soc):
  if soc < 20 or soc > 80:
    print('State of Charge is out of range!')
    return False

def check_cr(charge_rate):
  if charge_rate > 0.8:
    print('Charge rate is out of range! eeeeeeee')
    return False

def battery_is_ok(temperature, soc, charge_rate):
  check_temp(temperature)
  check_soc(soc)
  check_cr(charge_rate)

  return True


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
