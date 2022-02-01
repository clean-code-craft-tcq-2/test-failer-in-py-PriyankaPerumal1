import alerter
from stub_alerter import *

if __name__ == '__main__':
  alerter.alert_in_celcius(400.5,network_not_ok)
  assert(alerter.alert_failure_count == 1)
  alerter.alert_in_celcius(303.6,network_not_ok)
  assert(alerter.alert_failure_count == 2)
  print(f'{alerter.alert_failure_count} alerts failed.')
  alerter.alert_in_celcius(100,network_ok)
  assert(alerter.alert_failure_count == 2)
  print('All is well (maybe!)')
