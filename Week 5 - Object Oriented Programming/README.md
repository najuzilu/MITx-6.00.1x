## Object Oriented Programming (OOP) ##

### Object Oriented Programming (OOP) ###

* Python supports many different kinds of data
* each is an instance of an **object**, and every object has: 
	* a **type**
	* an internal **data representation** (primitive or composite)
	* a set of procedures for **interaction** with the object
* each **instance** is a particular type of object
	* `1234` is an instance of an `int`
	* `a == "hello"` `a` is an instance of string


* everything in Python is an **object** and has a **type**
* objects are a **data abstraction** that capture:
	* internal **representation** through data attributes
	* **interface** for interacting with object through methods (procedures), defines behaviors but hides implementation
* can **create new instances** of objects
* can **destroy objects**
	* explicityly using `del` or just "forget" about them
	* Python system will reclaim destroyed or inaccessible objects - called "garbage collection"

#### Standard data objects ####

Example:
* how are lists **represented internally**? linked list of cells
* how to **manipulate** lists?
	* L[i], L[i:j], L[i, j, k]
	* len(), min(), max(), del(L[i])
	* L.append(), L.extend(), L.count(), L.index(), L.insert(), L.pop(), L.remove(), L.reverse(), L.sort()

#### Creating and using your own objects with classes ####

* make a distinction between **creating a class* and **using an instance** of the class
* **creating** the class involves
	* defining the class name
	* defining the class attributes
* **using** the class involves:
	* creating new instances of objects
	* doing operations on the instances

#### Advantages of OOP ####

* **bundle data into packages** together with procedures that work on them through well-defined interfaces
* **divide-and-conquer** development
	* implement and test behavior of each class separately
	* increased modularity reduces complexity
* classes make it easy to **reuse** code
	* many Python modules defined new classes
	* each class has a separate environment (no collision on function names)
	* inheritance allows subclasses to redefine or extend a selected subset of a superclass' behavior

### Class Instances ###

Example:
```python
class Coordinate(object):
	<define attributes here>
```
* the word `object` means that `Coordinate` is a Python object and **inherits** all its attributes 
	* `Coordinate` is a subclass of `object`
	* `object` is a superclass of `Coordinate`


#### Exercise 1 ####

1. What method is called when an object is created?  
**Answer**: __init__
2. If you have an object instance, `obj`, and you want to call its `doSomething()` method (assuming it has one), how would you do this? (write the line of code you would use)  
**Answer**: obj.doSomething()
3. True or False? An object's attributes must be defined in the object's `__init__` method.  
**Answer**: False
4. The following code starts the definition of a class called `Address`. The class needs to have two attributes: `number` and `streetName`. Please add in the two lines of code that will create these attributes from the appropriate passed in parameters.  
**Answe**:
```python
class Address(object):
    def __init__(self, number, streetName):
        # Line 1: Creating a number attribute
        self.number = number
        # Line 2: Creating a streetName attribute 
        self.streetName = streetName 
```

### Methods ###

```python
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
    	x_diff_sq = (self.x - other.x) **2
    	y_diff_sq = (self.y - other.y) **2
    	return (x_diff_sq + y_diff_sq) **0.5
```

* procedural attribute, like a **function that works only with this class**  

* conventional way:
```python
c = Coordinate(3, 4)
origin = Coordinate(0, 0)
print(c.distance(origin))
```
**equivalent to**
```python
c = Coordinate(3, 4)
origin = Coordinate(0, 0)
print(Coordinate.distance(c, origin))
```

Print representation of an object:
```python
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
    	x_diff_sq = (self.x - other.x) **2
    	y_diff_sq = (self.y - other.y) **2
    
    def __str__(self):
    	return "<" + str(self.x) + "," + str(self.y) + ">"
c = Coordinate(3, 4)
origin = Coordinate(0, 0)
print(Coordinate.distance(c, origin))
```

To check if an object is `Coordinate`:
```python
print(isinstance(c, Coordinate))
```

#### Special operatos ####

* define them with double underscoures before/after  
`__add__(self, other)` --> self + other  
`__sub__(self, other)` --> self - other  
`__eq__(self, other)` --> self == other  
`__lt__(self, other)` --> self < other  
`__len__(self)` --> len(self)  
`__str__(self)` --> print(self)  

#### Exercise 2 ####
1. Consider the following code:
```python
class Clock(object):
    def __init__(self, time):
	self.time = time
    def print_time(self):
	time = '6:30'
	print(self.time)

clock = Clock('5:30')
clock.print_time()
```
**Answer**: 5:30

2. Consider the following code:
```python
class Clock(object):
    def __init__(self, time):
	self.time = time
    def print_time(self, time):
	print(time)

clock = Clock('5:30')
clock.print_time('10:30')
```
**Answer**: 10:30

3. Consider the following code:
```python
class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        print(self.time)

boston_clock = Clock('5:30')
paris_clock = boston_clock
paris_clock.time = '10:30'
boston_clock.print_time()
```
**Answer**: 10:30

Are `boston_clock` and `paris_clock` different objects?
**Answer**: No
#### Exercise 3 ####
Below is a transcript of a session with the Python shell. Provide the type and value of the expressions being evaluated inside the print. If evaluating an expression would cause an error, select NoneType and write error in the box. If the result is a function, select function and write function in the box. As always, try to do this problem by hand before turning to your interpreter for help.

Assume the following definitions have been made:
```python
class Weird(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return x 
    def getY(self):
        return y

class Wild(object):
    def __init__(self, x, y): 
        self.y = y
        self.x = x
    def getX(self):
        return self.x 
    def getY(self):
        return self.y

X = 7
Y = 8
```
1.
```python
w1 = Weird(X, Y)
print(w1.getX())
```
**Answer**: error  
2.
```python
print(w1.getY())
```
**Answer**: error  
3.
```python
w2 = Wild(X, Y)
print(w2.getX())
```
**Answer**: int 7  
4.
```python
print(w2.getY())
```
**Answer**: int 8  
5.
```python
w3 = Wild(17, 18)
print(w3.getX())
```
**Answer**: int 17  
6.
```python
print(w3.getY())
```
**Answer**: int 18  
7.
```python
w4 = Wild(X, 18)
print(w4.getX())
```
**Answer**: int 7  
8.
```python
print(w4.getY())
```
**Answer**: int 18  
9.
```python
X = w4.getX() + w3.getX() + w2.getX()
print(X)
```
**Answer**: int 31  
10.
```python
print(w4.getX())
```
**Answer**: int 7  
11.
```python
Y = w4.getY() + w3.getY()
Y = Y + w2.getY()
print(Y)
```
**Answer**: int 44  
12.
```python
print(w2.getY())
```
**Answer**: int 8

### Classes Example ###

#### Example 1 ####

```python
class fraction(object):
	def __init__(self, numer, denom):
		self.numer = numer
		self.denom = denom

	def __str__(self):
		return '{numer} / {denom}'.format(number, denom)

	def getNumer(self):
		return self.numer

	def getDenom(self):
		return self.denom

	def __add__(self, other):
		numerNew = other.getDenom() * self.getNumer() + other.getNumer() * self.getDenom()
		denomNew = other.getDenom() * self.getDenom()
		return fraction(numerNew, denomNew)

	def __sub__(self, other):
		numerNew = other.getDenom() * self.getNumer() - other.getNumer() * self.getDenom()
		denomNew = other.getDenom() * self.getDenom()
		return fraction(numerNew, denomNew)

	def convert(self):
		return self.getNumer() / self.getDenom()
```
#### Example 2 ####
```python
def intSet(object):
	def __init__(self):
		self.vals = []

	def insert(self, e):
		if not e in self.vals:
			self.vals.append(e)

	def member(self, e):
		return e in self.vals

	def remove(self, e):
		try:
			self.vals.remove(e)
		except:
			raise ValueError(str(e) + ' not found')

	def __str__(self):
		self.vals.sort()
		result = ''
		for e in self.vals:
			result = result + str(e) + ','
		return '{' + result[:-1] + '}'
```

#### Exercise: coordinate ####
```python
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        assert type(self) == type(other)
        if self.getX() == other.getX():
            if self.getY() == other.getY():
                return True
        return False

    def __repr__(self):
        return 'Coordinate({},{})'.format(self.getX(), self.getY())
```
#### Exercise: int set ####
```python
class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    def intersect(self, other):
    	intersectSet = intSet()

    	for x in self.vals:
    		if other.member(x):
    			intersectSet.insert(x)
    	return intersectSet

    def __len__(self):
    	return len(self.vals)
```

### Why OOP ###

```python
class Animal(object):
	def __init__(self, age):
		self.age = age
		self.name = None

	def get_age(self):
		return self.age

	def get_name(self):
		return self.name

	def set_age(self, newage):
		self.age = newage

	def set_name(self, newname=""):
		self.name = newname

	def __str__(self):
		return "animal {}: {}".format(self.name, self.age)
```

### Hierarchies ###

```python
class Animal(object):
	def __init__(self, age):
		self.age = age
		self.name = None

	def get_age(self):
		return self.age

	def get_name(self):
		return self.name

	def set_age(self, newage):
		self.age = newage

	def set_name(self, newname=""):
		self.name = newname

	def __str__(self):
		return "animal {}: {}".format(self.name, self.age)

class Cat(Animal):
	def speak(self):
		print("meow")

	def __str__(self):
		return 'cat: {}: {}'.format(self.name, self.age)

jelly = Cat(1)
jelly.get_name()
jelly.set_name('JellyBelly')
jelly.get_name()
print(jelly)
print(Animal.__str__(jelly))
blob = Animal(1)
blob.set_name()

class Rabbit(Animal):
	def speak(self):
		print("meep")

	def __str__(self):
		return 'rabbit: {}: {}'.format(self.name, self.age)

peter = Rabbit(5)
jelly.speak()
peter.speak()
blob.speak() # ERROR

class Person(Animal):
	def __init__(self, name, age):
		Animal.__init__(self, age)
		Animal.set_name(self, name)
		self.friends = []

	def get_friends(self):
		return self.friends

	def add_friend(self, fname):
		if fname not in self.friends:
			self.friends.append(fname)

	def speak(self):
		print("hello")
	
	def age_diff(self, other):
		diff = self.get_age() - other.get_age()
		if self.age > other.age:
			print('{} is {} years older than {}'.format(self.name, diff, other.name))
		else:
			print('{} is {} years younger than {}'.format(self.name, -diff, other.name))

	def __str__(self):
		return 'person: {}: {}'.format(self.name, self.age)

eric = Person("eric", 45)
john = Person("john", 55)
eric.speak()
eric.age_diff(john)
Person.age_diff(john, eric)
```
```python
import random

class Student(Person):
	def __init__(self, name, age, major = None):
		Person.__init__(self, name, age)
		self.major = major

	def change_major(self, major):
		self.major = major

	def speak(self):
		r = random.random()
		if r < 0.25:
			print("I have homework")
		elif 0.25 <= r < 0.5:
			print("I need sleep")
		elif 0.5 <= r < 0.75:
			print("I should eat")
		else:
			print("I am watching TV")

	def __str__(self):
		return 'student: {}: {}: {}'.format(self.name, self.age, self.major)
```

#### Exercise: spell ####

```python
class Spell(object):
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation
    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.getDescription()       
    def getDescription(self):
        return 'No description'
    def execute(self):
        print(self.incantation)


class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')

class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')
    def getDescription(self):
        return 'Causes the victim to become confused and befuddled.'

def studySpell(spell):
    print(spell)

spell = Accio()
spell.execute()
studySpell(spell)
studySpell(Confundo())
```

1. **Answer**: Spell
2. **Answer**: Accio and Confundo
3. **Answer**:
* Accio
* Summoning Charm Accio
* No description
* Confundus Charm Confundo
* Causes the victim to become confused and befuddled.
4. **Answer**: The `getDescription` method defined within the `Confundo` class
5. **Answer**:  
```python
class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')
        
    def getDescription(self):
        return 'This charm summons an object to the caster, potentially over a significant distance.'
        
    def __str__(self):
        print('{} {}'.format(self.incantation, self.name))
```

#### Exercise 4 ####

```python
class A(object):
    def __init__(self):
        self.a = 1
    def x(self):
        print("A.x")
    def y(self):
        print("A.y")
    def z(self):
        print("A.z")

class B(A):
    def __init__(self):
        A.__init__(self)
        self.a = 2
        self.b = 3
    def y(self):
        print("B.y")
    def z(self):
        print("B.z")

class C(object):
    def __init__(self):
        self.a = 4
        self.c = 5
    def y(self):
        print("C.y")
    def z(self):
        print("C.z")

class D(C, B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d = 6
    def z(self):
        print("D.z")
```

1. `print(obj.a)`
**Answer**: 2
2. `print(obj.b)`
**Answer**: 3
3.
```python
print(obj.c)
```
**Answer**: 5
4.
```python
print(obj.d)
```
**Answer**: 6
5.
```python
obj.x()
```
**Answer**: A.x
6.
```python
obj.y()
```
**Answer**: C.y
7.
```python
obj.z()
```
**Answer**: D.z

#### Class Variables ####

* **subclasses inherit** all data attributes and methods of the parent class

```python
class Rabbit(Animal):
	tag = 1

	def __init__(self, age, parent1=None, parent2=None):
		Animal.__init__(self, age)
		self.parent1 = parent1
		self.parent2 = parent2
		self.rid = Rabbit.tag
		Rabbit.tag += 1

	def get_rid(self):
		return str(self.rid).rfill(3) # fill with zeros

	def get_parent1(self):
		return self.parent1

	def get_parent2(self):
		return self.parent2

	def __add__(self, other):
		return Rabbit(0, self, other)

	def __eq__(self, other):
		parents_same = (self.parent1.rid == other.parent1.rid) and (self.parent2.rid == other.parent2.rid)
		parents_opposite = (self.parent2.rid == other.parent1.rid) and (self.parent1.rid == other.parent2.rid)
		return parents_same or parents_opposite

peter = Rabbit(2)
peter.set_name('Peter')
hopsy = Rabbit(3)
hopsy.set_name('Hopsy')
cotton = Rabbit(1, peter, hopsy)
cotton.set_name('Cottontail')
print(cotton)
print(cotton.get_parent1())
mopsy = peter + hopsy
mopsy.set_name('Mopsy')
print(mopsy.get_parent1())
print(mopsy.get_parent2())
print(mopsy == cotton)
```
* `tag` used to give **unique id** to each new rabbit instance





