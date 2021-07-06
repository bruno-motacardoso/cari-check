import sys

def badUsage(scriptname):
  print('Error: Bad usage')
  print(f'{scriptname} noReg dateOfBirth fromDate endDate wirepusher_id')
  sys.exit(1)