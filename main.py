def main():
    numbers = []
    
    previousVal = int(input())
    numbers.append(previousVal)
    
    while True:
        current = int(input())
        
        if current <= previousVal:
            numbers.append(current)
            previousVal = current
        else:
            break

    ########################################
    # Do not delete the return statement
    ########################################
    print(*numbers)
    return numbers


if __name__ == '__main__':
    main()
