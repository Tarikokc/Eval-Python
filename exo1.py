def find_triplets_with_zero_sum(numbers):
    numbers.sort()  
    result = []
    n = len(numbers)

    for i in range(n - 2):
        if i > 0 and numbers[i] == numbers[i - 1]:
            continue  

        left = i + 1
        right = n - 1

        while left < right:
            current_sum = numbers[i] + numbers[left] + numbers[right]

            if current_sum == 0:
                result.append([numbers[i], numbers[left], numbers[right]])
                
                
                while left < right and numbers[left] == numbers[left + 1]:
                    left += 1
                while left < right and numbers[right] == numbers[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    return result

exemple1 = [2, 7, 9, -9]
exemple2 = [-33, -10, -8, -2, 1, 4, 9, 10]

print("Exemple 1:")
print("Entrée:", exemple1)
print("Sortie:", find_triplets_with_zero_sum(exemple1))

print("\nExemple 2:")
print("Entrée:", exemple2)
print("Sortie:", find_triplets_with_zero_sum(exemple2))