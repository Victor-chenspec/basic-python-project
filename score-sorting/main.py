import random

score = [42, 7, 91, 18, 63, 29, 55, 4, 88, 76,
 12, 34, 67, 23, 90, 1, 58, 31, 47, 84,
 26, 73, 9, 65, 38, 99, 14, 52, 6, 79,
 21, 60, 45, 82, 3, 70, 28, 95, 11, 49,
 66, 17, 86, 24, 54, 8, 92, 36, 71, 5,
 80, 19, 41, 68, 27, 94, 15, 57, 32, 77,
 10, 64, 35, 83, 2, 72, 30, 97, 13, 51,
 59, 20, 44, 69, 25, 89, 16, 56, 33, 78,
 22, 62, 40, 85, 98, 48, 74, 37, 93, 61]

class Sort_Algo():
    def __init__(self):
       pass

    def QuickSort(self,array,type=None):
        if len(array) <= 1:
            return array

        pivot = array[-1]
        if type == "random_pivot":
            pivot = random.choice(array)

        lower = []
        greater = []
        equal = []

        for item in array:
            if item > pivot:
                greater.append(item)
            elif item < pivot:
                lower.append(item)
            else:
                equal.append(item)

        return self.QuickSort(lower) + equal + self.QuickSort(greater)
    
    def MergeSort(self,array):

        def Merge(left,right):
            result = []
            i,j = 0,0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        
        if len(array) <= 1:
            return array
        
        mid = len(array)//2
        
        left = self.MergeSort(array[:mid])
        right = self.MergeSort(array[mid:])

        return Merge(left,right)


