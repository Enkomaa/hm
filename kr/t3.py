string = str(input())
l = len(string)-1
letter = 1
new_string = ''
if len(string) == 1:
    new_string = new_string +string+str(letter)
else:
    for i in range(0,l):
        if string[i] == string[i+1]:
            letter +=1
        elif string[i] != string[i+1]:
            new_string = new_string + string[i]+str(letter)
            letter = 1
    for j in range(l,l+1):
        if string[-1] == string[-2]:
            new_string = new_string +string[j]+str(letter)
        elif string[-1] != string[-2]:
            new_string = new_string +string[j]+str(letter)
            letter = 1
print(new_string)