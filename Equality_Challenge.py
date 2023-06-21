from random import randint, shuffle

def generate_keys(num_of_keys: int) -> list:
    '''Генерация ключей для шкафов'''
    keys = []
    for i in range(num_of_keys):
        keys.append([randint(1, 100000000), randint(1, 100000000), ""])
    return keys

def open_box_alice(key: int, boxes: list) -> int:
    '''Проверка шкафа Алисы на наличия записки'''
    for i in range(len(boxes)):
        if boxes[i][0] == key:
            return i + 1
    return -1

def open_box_bob(key: list, boxes: list) -> int:
    '''Проверка всех шкафов на наличие записки'''
    for i in range(len(boxes)):
        if boxes[i][1] == key and boxes[i][2] != '':
            return i + 1
    return -1

def millioner(num_boxes: int, boxes: list, alice_box: int, bob_box: int, bob_note: str) -> None:
    '''Основной алгоритм задачи миллионеров-социалистов'''  
    alice_key = boxes[alice_box-1]
    boxes[bob_box-1] = [boxes[bob_box-1][0], boxes[bob_box-1][1], bob_note]
    shuffle(boxes)
    alice_result = open_box_alice(alice_key[0], boxes)

    bob_results = []
    for i in range(num_boxes):
        result = open_box_bob(boxes[i][1], boxes)
        if result != -1:
            bob_results.append(result)
    
    if len(bob_results) == 1:
        if alice_result == bob_results[0]:
            print("Результат: a = b")
        else:
            print("Результат: a ≠ b")
    else:
        print("Кто-то смухлевал!")

if __name__ == "__main__":
    '''Start'''
    print("Введите количество ящиков:")
    num_boxes = int(input())

    boxes = generate_keys(num_boxes)

    print("Введите номер ящика Алисы:")
    alice_box = int(input())

    print("Введите номер ящика Боба:")
    bob_box = int(input())
    bob_note = 'bob\'s note'

    millioner(num_boxes, boxes, alice_box, bob_box, bob_note)