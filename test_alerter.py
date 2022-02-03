import alerter
import stub_alerter

def test_alerter():
  alerter.alert_in_celcius(400.5,stub_alerter.network_not_ok)
  assert(alerter.alert_failure_count == 1)
  alerter.alert_in_celcius(303.6,stub_alerter.network_not_ok)
  assert(alerter.alert_failure_count == 2)
  print(f'{alerter.alert_failure_count} alerts failed.')
  alerter.alert_in_celcius(100,stub_alerter.network_ok)
  assert(alerter.alert_failure_count == 2)
  
if __name__ == '__main__':
  test_alerter()
  print('All is well')
