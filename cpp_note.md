# C++ Note

```cpp
// to iterate over an iterable
// lets say v is an array
for(auto x : v){
    // some tasks 
}

/* if want to create the iterating variable without copying
the orginal data. we can pass x by reference */
for(auto& x : v){
    // some tasks
}
```

### Pass-by-reference
it is like passing the address of the data at the arguments

```cpp
// avoid copying the passing data

void sort(vector<double>& v);

/* don't want to modify the arguments, also don't want to 
copy it */
double sum(const vector<double>& v);
```
## User-Defined Types

- structure `struct`

```cpp
// basic structure
struct Vector{
    int sz;
    double* elem;
}

// however, elem points to nothing, so we have to initialize it
void vector_init(Vector& v, int s){
    v.elem = new double[s];
    v.sz = s;
}

// The following demonstrate how to access `struct` member
void f(Vector r, Vector& rv, Vector* pv){
    int i1 = r.sz;
    int i2 = rv.sz;  // access through reference
    int i3 = pv->sz; // access through pointer
}
// reference is like a nickname, though different name, but the same person
```
- Class

Notice that regardless of the number of elements of each object, 
all the objects are of the same size (i.e. taking up the same size of space) 
```cpp
class Vector{
    public:
        Vector(int s): elem{new double[s]}, sz{s}{} // constructor
        // the part before {} is called memeber initializer list
        // TODO
    private:
        double* elem;
        int sz;
        // TODO
}
```
_A struct is simply a class with its members public by default_
Notice that you can also define constructor and member function for `struct` objects.

- Union

The purpose of union is to save memory by using the same memory region for storing different objects at different times.\
That is the same class might have some subtypes, which can effect the type of clas member it uses.

```cpp
enum Type{ str, num};

struct Entry{
    Type t;
    char* s; // if type is str
    int i; // if type is num
} 

void f(Entry* p ){
    if(p->t == str){
        // do something on p->s
    }
    if(p->t == num){
        // do something on p->i
    }
}
// the above can be improved by:
union Value{ // all member share the same memory space and does't exist at the same time
    char* s;
    int i;
}

struct Entry{
    Type t;
    Value v;
}

void f(Entry* p){
    if(p->t == str){
        // do on p->v.s
    }
    if(p->t == num){
        // do on p->v.i
    }
}
```
- Enumeration
    1. `enum class`
    2. plain `enum`

In `enum class`, the variables are in a local scope of enum class.\
However, for plain `enum`,  those variables are in the same scope of `enum` name.

```cpp
// Error, cuz redefinition of variables
enum TrainLight{
    red,
    blue,
    pink
}
enum TrafficLight{
    red,
    blue,
    pink
}

// better use enum class
// No error
enum TrainLight{
    red,
    blue,
    pink
}
enum TrafficLight{
    red,
    blue,
    pink
}
```

