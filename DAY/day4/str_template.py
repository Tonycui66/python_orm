import math
import string
from string import Template



if __name__ == '__main__':
    s= Template("cost $duration s total $total")
    aa="123"
    s = Template(s.safe_substitute(duration=10))
    print(aa.isalnum())
    print(aa.isprintable())
    print(aa.isalpha())
    print(aa.format())
    bb= s.safe_substitute(total=200)
    print(aa)
    print(bb)
    print(string.hexdigits)
    print(string.ascii_letters)
    print(string.ascii_lowercase)
    print(string.ascii_uppercase)
    print(string.punctuation)
    print(string.octdigits)
    print(string.capwords("Abac Tfaaf afaf"))
    print(math.fmod(10,2))
    print(math.factorial(3))  ## 因子,阶乘
    print(math.frexp(65536))  ## 返回(m,e) (m*2^e)