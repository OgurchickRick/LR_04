import os


def way():
    pass


def dictionary(path):
    result = {}
    for filename in os.listdir(path):
        current_puth = os.path.join(path, filename)
        if os.path.isdir(current_puth):
            result.update(dictionary(current_puth))
        else:
            result[current_puth] = os.path.getsize(current_puth)
    return result


def duplicate():
    pass
  
  
def my_print():
    pass
  
  
if __name__ == '__main__':
    
