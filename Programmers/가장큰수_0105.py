def solution(numbers):
    answer = ""
    
    def quick_sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        greater_arr, equal_arr, lesser_arr  = [], [], []
        for num in arr:
            if  num + pivot > pivot + num:
                greater_arr.append(num)
            elif num + pivot < pivot + num:
                lesser_arr.append(num)
            else:
                equal_arr.append(num)
                
        greater_sort = quick_sort(greater_arr)
        lesser_sort = quick_sort(lesser_arr)
        
        return  greater_sort + equal_arr + lesser_sort

    data = list(map(str,numbers))
    answer = quick_sort(data)
    
    return str(int(''.join(answer)))