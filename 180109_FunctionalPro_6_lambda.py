## lambda x : expression      def funcName(x)
##                        ==       return expression
## quick way of defining a ONE expression function


## exmaple
L = list(map(lambda x: x + 1, [1, 2, 3, 4, 5, 6])) 
           #|FirstPart     |, |SecondPart      |
print(L)

## prac
LN = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(LN)