import os


def way():
    pass


def dictionary():
    pass


def duplicate(a: dict):
    keys = list(a.keys())
    copies = {}
    for key_ind1 in range(len(keys) - 1):
        key1 = keys[key_ind1]
        result_key = (a[key1], key1)
        for key_ind2 in range(key_ind1 + 1, len(keys)):
            key2 = keys[key_ind2]
            if os.path.basename(key1) == os.path.basename(key2) and a[key1] == a[key2]:
                if result_key not in copies:
                    copies[result_key] = []
                copies[result_key].append(key2)
        if result_key in copies:
            yield result_key, copies[result_key]
  
  
def my_print():
    pass
  
  
if __name__ == '__main__':
    
