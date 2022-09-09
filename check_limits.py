def print_temp():
  print('Temperature is out of range!')
  
def print_soc():
  print('State of Charge is out of range!')

  
def print_cr():
   print('Charge rate is out of range!')

def check_temp(temperature):
  if temperature < 0 or temperature > 45:
    return False
  return True
    
def check_soc(soc):
  if soc < 20 or soc > 80:
    return False
  return True

def check_cr(charge_rate):
  if charge_rate < 0.8:   
    return True
  return False

def battery_is_ok(temperature, soc, charge_rate):
  boolone = check_temp(temperature)
  booltwo = check_soc(soc)
  boolthree = check_cr(charge_rate)

  return boolone and booltwo and boolthree


if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
