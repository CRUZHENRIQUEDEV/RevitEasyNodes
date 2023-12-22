#https://stackoverflow.com/questions/30488751/clean-list-or-list-of-lists-of-all-none-or-empty-lists-in-python


def ClearList(primList):
  result = []
  for sublist in primList:
    if sublist is "":
      continue
    elif sublist is None:
      continue
    if isinstance(sublist, list):
      sublist = ClearList(sublist)
      if not sublist:
        continue
    result.append(sublist)
  return result


OUT = ClearList(IN[0])
