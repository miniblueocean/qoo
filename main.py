def main():
    print("Hello World")


def sub(x, y):
   if x == 0 and y == 0:
       raise ValueError
   return x - y 


if __name__ == '__main__':
    main()
