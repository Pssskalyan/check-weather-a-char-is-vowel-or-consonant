ch = input()

if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
 or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
    print("Vowel")
elif(ch=='!' or ch=='@' or ch=='#' or ch=='$' or ch=='%' or ch=='^' or ch=='&' or ch=='*' or ch=='(' or ch==')'):
    print("invalid")
else:	
    print("Consonant")
