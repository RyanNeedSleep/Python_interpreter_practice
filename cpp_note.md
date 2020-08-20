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
