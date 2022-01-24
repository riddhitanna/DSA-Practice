
def reverse_arr(arr):
    for i in range(int(q/2)):
        temp = arr[i]
        arr[i] = arr[q-i-1]
        arr[q-i-1] = temp

    return arr


if __name__ == "__main__":
    q = int(input('Enter the number of elements in the array to be reversed:'))
    string = list(input().split())
    arr = [int(x) for x in string]
    print('The given array is:', arr)
    rev_arr = reverse_arr(arr)
    print('The reversed array is:', rev_arr)
