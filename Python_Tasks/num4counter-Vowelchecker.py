
def Vowel_checker(letter):
    if(letter=='a'or letter=='e' or letter=='i' or letter== 'u '):
        return True
    return False

def number_4_counter(lis):
    count=0
    for num in lis:
        if(num==4):
            count+=1
    print("number of 4s = ",count)

lis=[3,4,6,7,4,2,3,4,6,4,2,5]
number_4_counter(lis)
let='i'
print(Vowel_checker(let))