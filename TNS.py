# DATA STRACTURE AND ALGORTHMS
# Two Number Sum
# 3 Different approach 



def two_number_sum(number, target):
    number_indices={}


    for i, number in enumerate(numbers):
        complement = target - number
        
        # Check if the complement exists in the dictionary
        if complement in number_indices:
            # Return the indices of the two numbers that add up to the target
            return [number_indices[complement], i]
        
        # If complement is not found, add the current number and its index to the dictionary
        number_indices[number] = i
    
    # If no such pair is found, return None
    return None

numbers = [-4, -1, 1, 3, 5, 6, 8, 11]
target = 10
result = two_number_sum(numbers, target)

if result:
    print(f'The indices of the two numbers that sum up to {target} are: {result}')
else:
    print(f'No such pair found that sums up to {target}')






def twonumber_sum(numbers, target):
    for i in range(len(numbers) - 1):
        first_num = numbers[i]
        for k in range(i+1, len(numbers)):
            second_num = numbers[k]
            if first_num + second_num == target:
                return[first_num, second_num]

numbers = [-4, -1, 1, 3, 5, 6, 8, 11]
target = 10
result = twonumber_sum(numbers, target)

if result:
    print(f'the indices of the two numbers that sum up to {target} are:{result}')
else:
    print(f"no such pair found that sums up to {target}")


def twonumberSum(numbers, target):
   numbers.sort()
   left = 0
   right = len(numbers) - 1
   while left < right:
       current_sum = numbers[left] + numbers[right]
       if current_sum == target:
           return[numbers[left], numbers[right]]
       elif current_sum < target:
           left +=1
       elif current_sum > target:
           right -=1
   return[]
         
       
numbers = [-4, -1, 1, 3, 5, 6, 8, 11]
target = 10
result = twonumberSum(numbers, target)

if result:
    print(f'The numbers that sum up to {target} are: {result}')
else:
    print(f'No such pair found that sums up to {target}')

