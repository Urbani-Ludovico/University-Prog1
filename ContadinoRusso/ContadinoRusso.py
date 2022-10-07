
import re

print("\n- - - - - START PROGRAM - - - - -\n\n")

op = input("Insert operation [NxN] :  ")

if re.match("^[0-9]+[x][0-9]+$", op):
    try:
        n1, n2 = op.split("x")
        m = int(n1)
        n = int(n2)
    except:
        pass
    
    if "n" in locals() and "m" in locals():
        print("\nInput of N and M\n")
        ops = 1
        
        print("%.5i\t%i\t%s" % (ops, 1, "p = 0"))
        ops += 1
        p = 0
        
        while True:
            print("%.5i\t%i\t%s" % (ops, 2, "If m == 0: end  ->  " + ("FALSO", "VERO")[m == 0]))
            ops += 1
            if m > 0:
                print("%.5i\t%i\t%s" % (ops, 3, "If m even: goto 5  ->  " + ("FALSO", "VERO")[m % 2 == 0]))
                ops += 1
                if m % 2 != 0: 
                    print("%.5i\t%i\t%s" % (ops, 4, "p = p + %i = %i" % (n, p + n)))
                    ops += 1
                    p += n
                print("%.5i\t%i\t%s" % (ops, 5, "m = m // %i = %i" % (2, m // 2)))
                ops += 1
                m = m // 2
                
                print("%.5i\t%i\t%s" % (ops, 6, "n = n * %i = %i" % (2, 2 * 2)))
                ops += 1
                n = n * 2
                
                print("%.5i\t%i\t%s" % (ops, 7, "goto 2"))
                ops += 1
            else:
                break
            
        print("\nOutput :         ", p)
        print("Operations:      ", ops - 1)
                
        
        # while n1 > 0:
        #     if n1 % 2 == 1:
        #         p += n2
        #     n1 = n2 // 2
        #     n2 = n2 * 2
    else:        
        print("Input error")

else:
    print("Operation not match format")
    
print("\n\n - - - - - END PROGRAM - - - - -\n\n")