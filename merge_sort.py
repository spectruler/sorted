def mergeSort(nums):
    if len(nums) > 1:
        pivot = len(nums)//2
        left = nums[:pivot]
        right = nums[pivot:]

        # divide 
        mergeSort(left)
        mergeSort(right)
        # conquer
        i=j=k=0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                nums[k] = right[j]
                j += 1 
            else:
                nums[k] = left[i]
                i += 1 
            k += 1  
        while i < len(left):
            nums[k] = left[i]
            i += 1 
            k += 1 
        while j < len(right):
            nums[k] = right[j]
            j += 1 
            k += 1 



if __name__ == '__main__':
    nums = [int(num.strip()) for num in input('Enter numbers to sort: ').split()]
    # nums = [2,1,3,0]

    mergeSort(nums) 
    print(nums)

            
         