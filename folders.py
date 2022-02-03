import os


def way():
    while True:
        path = str(input('Введите путь до папки:'))
        if os.path.exists(path):
            return path
        else:
            print("Неверный путь")


def dictionary(path):
    result = {}
    for filename in os.listdir(path):
        current_puth = os.path.join(path, filename)
        if os.path.isdir(current_puth):
            result.update(dictionary(current_puth))
        else:
            result[current_puth] = os.path.getsize(current_puth)
    return result


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
  
  
def my_print(result):
    for key, val in result:
        print(key)
        for item in val:
            print(f'\t{item}')
        print()
  
  
if __name__ == '__main__':
    p = way()
    print('start')
    files = dictionary(p)
    print(f'Получение файлов завершено, найдено {len(files)}')
    print('Поиск дубликатов')
    my_print(duplicate(files))
    print('Вывод дубликатов завершен')
