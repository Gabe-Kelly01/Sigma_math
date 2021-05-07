import sys

def main():
    try:
        num = int(sys.argv[1])
        binary_num = ""

        while num > 1:
            q, mod = divmod(num, 2)
            num = q 
            binary_num += str(mod)

        print(binary_num)

    except Exception as e:
        raise e
    

main()