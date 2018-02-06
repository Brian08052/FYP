def is_number(s):
  try:
    float(s)
    return True
  except ValueError:
    pass
  try:
    import unicodedata
    unicodedata.numeric(s)
    return True
  except (TypeError, ValueError):
    pass
  return False

def prepSearchString(string):
  s = string.split(',')
  for i in s:
    if not is_number(i):
      return False
  return True
