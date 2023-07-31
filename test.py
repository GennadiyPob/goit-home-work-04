'''Task 14/14'''

import sys

#for arg in sys.argv:
 #    print(arg)

def parse_args():
    result =''
    args = sys.argv[1:]
    result = ' '.join(args)  
    return result

parsed_args = parse_args()
print(parsed_args)

     
