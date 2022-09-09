def check_temp(temperature):
  ez = True
  if temperature < 0 or temperature > 45:
    ez= False
    print('Temperature is out of range!')
   return ez

def check_soc(soc):
  ez = True
  if soc < 20 or soc > 80:
    ez = False
    print('State of Charge is out of range!')
   return ez

def check_cr(charge_rate):
  ez = True
  if charge_rate > 0.8:
    ez = False
    print('Charge rate is out of range!')
   return ez

def battery_is_ok(temperature, soc, charge_rate):
  onebool = check_temp(temperature)
  twobool = check_soc(soc)
  threebool = check_cr(charge_rate)

  return onebool and twobool and threebool


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
