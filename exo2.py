def total(n1, n2):
    n1 = n1[::-1]
    n2 = n2[::-1]
    
    if len(n2) > len(n1):
        n1, n2 = n2, n1
    
    result = []
    carry = 0
    
    for i in range(len(n1)):
        digit_sum = n1[i] + carry
        if i < len(n2):
            digit_sum += n2[i]
        
        result.append(digit_sum % 10)
        carry = digit_sum // 10
    
    if carry:
        result.append(carry)
    
    return result[::-1]

print(total([8, 4, 0], [8, 3]))    
print(total([1, 8, 3], [7]))        
print(total([1, 2, 3], [0]))        
print(total([9, 9, 9], [1]))        