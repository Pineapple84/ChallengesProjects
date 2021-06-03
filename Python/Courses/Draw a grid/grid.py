''' Draw a grid

+----+----+
|    |    |
|    |    |
|    |    |
|    |    |
+----+----+
|    |    |
|    |    |
|    |    |
|    |    |
+----+----+ '''

def one():
  print("+----+----+")
  
def two():
    i = 0
    
    while i < 4:
        print("|    |    |")
        i += 1
            
def output():
  one()
  two()
  one()
  two()
  one()

output()
