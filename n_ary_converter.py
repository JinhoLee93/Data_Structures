NUM = '0123456789ABCDEF'

def n_ary_converter(number, base):
  q, r = divmod(number, base)
  n = NUM[r]
  
  return n_ary_converter(q, base) + n else n
