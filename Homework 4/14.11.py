#Caleb Covington
#1606086
def selection_sort_descend_trace(numbers):
    for i in range(len(numbers) - 1):
        max_ind = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[max_ind]:
                max_ind = j
        numbers[i], numbers[max_ind] = numbers[max_ind], numbers[i]
        print(' '.join([str(x) for x in numbers]),'')
    return numbers


if __name__ == '__main__':
    number=[]
    data = input("")
    numbers = [int(x) for x in data.split()]
    selection_sort_descend_trace(numbers)
