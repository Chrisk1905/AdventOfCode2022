# print the level of monkey bussiness over 20 rounds 
f = open(  "day11/input.txt" , "r" )

class Monkey:
    def __init__(self, items : list[int], operation: str, test:int , throw_true: int, throw_false: int ):
        self.items = items
        self.operation = operation
        self.test = test
        self.throw_true = throw_true
        self.throw_false = throw_false
        self.inspected = 0

    def do_operation(self, old : int) -> int:
        new = eval(self.operation)
        idx = self.items.index(old)
        self.items[idx] = new
        return new
    
    def do_test(self, item : int) -> bool:
        return item % self.test == 0

    def throw(self, item : int, catch_monkey) -> None:
        self.items.remove(item)
        catch_monkey.catch(item)
        
    def catch(self, item):
        self.items.append(item)


monkey_map = {}

for line in f:
    line = line.strip()
    line = line.split(" ")
    if line[0] == "Monkey":
        end = len(line[1]) - 1
        monkey_number = int(line[1][0:end])
        #items
        items = []
        attribute = f.readline().strip()
        attribute = attribute[15: len(attribute)]
        attribute = attribute.split(",")
        for item in attribute:
            item = int(item.strip())
            items.append(item)
        #operation
        attribute = f.readline().strip()
        start = attribute.find("=")
        attribute = attribute[start+2:len(attribute)]
        operation = attribute        
        #Test
        attribute = f.readline().strip().split(" ")
        test = int(attribute[3])
        #true throw and false throw
        attribute = f.readline().strip().split(" ")
        true_throw = int(attribute[5])
        attribute = f.readline().strip().split(" ")
        false_throw = int(attribute[5])

        new_monkey = Monkey(items, operation, test, true_throw, false_throw)
        monkey_map[monkey_number] = new_monkey


def round(monkey_map: dict, bigmod: int)->None:
    for monkey in monkey_map.values():
        while len(monkey.items) > 0:
            monkey.do_operation(monkey.items[0])            
            if monkey.do_test(monkey.items[0]):
                catch_monkey = monkey_map[monkey.throw_true]
            else:
                catch_monkey = monkey_map[monkey.throw_false]
            monkey.items[0] = monkey.items[0] % bigmod
            monkey.throw(monkey.items[0], catch_monkey)
            monkey.inspected += 1

bigmod = 1
for monkey in monkey_map.values():
    bigmod *= monkey.test

for _ in range(10000):
    round(monkey_map, bigmod)

first_max = 0 
second_max = 0

for monkey in monkey_map.values():
    if monkey.inspected > second_max:
        if monkey.inspected > first_max:
            temp = first_max
            first_max = monkey.inspected
            second_max = max(second_max,temp)
        else:
            second_max = monkey.inspected

print(first_max, second_max)
print(first_max * second_max)