def minflips(pwd):
    count = 0
    curr = '1'
    for i in range(len(pwd)):
         
        # If curr occurs in the final string
        if (pwd[i] == curr):
            count += 1
             
            # Switch curr to '0' if '1'
            # or vice-versa
            curr = chr(48 + (ord(curr) + 1) % 2)
        
    return count

strg = '101011'
print(minflips(strg))