nums = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11,
'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30,
'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90,
'hundred': 100, 'thousand': 1000, 'million': 1000000, 'billion': 1000000000}

str_input = input("Please provide a number: ").lower().split()

current = 0
total = 0

# for word in str_input:
#     for string, num in nums.items():
#         if word == "string":
#             value *= num

for word in str_input:
    if word in nums:
        value = nums[word]
        
        if value == 100:
            current *= value
            
        elif value in [1000, 1000000, 1000000000]:
            current *= value
            total += current
            current = 0
            
        else:
            current += value
            
total +=current
print(total)
