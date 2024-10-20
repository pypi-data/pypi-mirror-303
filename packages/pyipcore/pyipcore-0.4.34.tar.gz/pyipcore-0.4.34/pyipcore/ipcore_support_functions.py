import math
SP_ENV_S = '''
import math

ceil = math.ceil
floor = math.floor
log2 = math.log2

def api_cwidth(reach_value:int) -> int:
    """
    Calculate the width of the counter.
    2 ** width - 1 >= reach_value
    """
    return ceil(log2(reach_value + 1))

api_cwidth_i_i = api_cwidth
    
def api_cmults(a:int, b:int) -> int|None:
    """
        Calculate the multiples of a b. if a/b is not multiple of b/a, return None
        计算
        * input must be int
    """
    if not isinstance(a, int):
        raise TypeError(f"a must be an integer, not {type(a).__name__}")
    if not isinstance(b, int):
        raise TypeError(f"b must be an integer, not {type(b).__name__}")
    
    if a <= 0 or b <= 0:
        return None
    
    if a % b == 0:
        return a // b
    elif b % a == 0:
        return b // a
    else:
        return None
        
api_cmults_ii_i = api_cmults
        
def api_wdint_ii_s(num, width) -> str:
    _max = 2 ** width
    num %= _max
    return f"{width}'d{num}"
'''


        






