import alerter
import stub_alerter

if __name__ == '__main__':
  alerter.alert_in_celcius(400.5)
  alerter.alert_in_celcius(303.6)
  print(f'{alerter.alert_failure_count} alerts failed.')
  assert(alerter.alert_failure_count == 2)
  print('All is well (maybe!)')
