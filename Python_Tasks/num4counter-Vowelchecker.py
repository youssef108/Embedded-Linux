
def Vowel_checker(letter):
    vowels={'a','e','i','u'}
    if(letter in vowels):
        return True
    return False

def number_4_counter(lis):
    count=lis.count(4)
    print("number of 4s = ",count)

lis=[3,4,6,7,4,2,3,4,6,4,2,5]
number_4_counter(lis)
let='i'
print(Vowel_checker(let))