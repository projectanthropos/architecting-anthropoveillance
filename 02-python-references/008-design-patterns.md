## Python References

* Types of design patterns
  * creational
  * structural
  * behavioral
* Factory method
* Strategy
* Proxy

&nbsp;
&nbsp;
&nbsp;

### Factory method

```python
class Pizza(object):
    def __init__(self):
        self._price = None

    def get_price(self):
        return self._price

class HamAndMushroomPizza(Pizza):
    def __init__(self):
        self._price = 8.5

class DeluxePizza(Pizza):
    def __init__(self):
        self._price = 10.5

class HawaiianPizza(Pizza):
    def __init__(self):
        self._price = 11.5

class PizzaFactory(object):
    @staticmethod
    def create_pizza(pizza_type):
        if pizza_type == 'HamMushroom':
            return HamAndMushroomPizza()
        elif pizza_type == 'Deluxe':
            return DeluxePizza()
        elif pizza_type == 'Hawaiian':
            return HawaiianPizza()

if __name__ == '__main__':
    for pizza_type in ('HamMushroom', 'Deluxe', 'Hawaiian'):
          print('Price of {0} is {1}'.format(pizza_type, PizzaFactory.create_pizza(pizza_type).get_price())
```

&nbsp;

### Strategy

```python
class StrategyExample:

    def __init__(self, func=None):
        if func:
            self.execute = func

    def execute(self):
        print "Original execution"


def executeReplacement1(self):
        print "Strategy 1"


def executeReplacement2(self):
    print "Strategy 2"

if __name__ == "__main__":

    strat0 = StrategyExample()
    strat1 = StrategyExample(executeReplacement1)
    strat2 = StrategyExample(executeReplacement2)

    strat0.execute()
    strat1.execute()
    strat2.execute()
```

&nbsp;

### Proxy

```python
class IMath:
    """Interface for proxy and real subject."""
    def add(self, x, y):
        raise NotImplementedError()

    def sub(self, x, y):
        raise NotImplementedError()

    def mul(self, x, y):
        raise NotImplementedError()

    def div(self, x, y):
        raise NotImplementedError()

class Math(IMath):
    """Real subject."""
    def add(self, x, y):
        return x + y

    def sub(self, x, y):
        return x - y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        return x / y

class Proxy(IMath):
    """Proxy."""
    def __init__(self):
        self.math = Math()

    def add(self, x, y):
        return self.math.add(x, y)

    def sub(self, x, y):
        return self.math.sub(x, y)

    def mul(self, x, y):
        return self.math.mul(x, y)

    def div(self, x, y):
        if y == 0:
            return float('inf') # Вернуть positive infinity
        return self.math.div(x, y)

p = Proxy()
x, y = 4, 2
print '4 + 2 = ' + str(p.add(x, y))
print '4 - 2 = ' + str(p.sub(x, y))
print '4 * 2 = ' + str(p.mul(x, y))
print '4 / 2 = ' + str(p.div(x, y))
```

&nbsp;
&nbsp;
&nbsp;
> https://github.com/gennad/Design-Patterns-in-Python
