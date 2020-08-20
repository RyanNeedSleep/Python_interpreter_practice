#include <iostream>


using namespace std;

int main(){
    int v[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int* p = v;
    
    for(auto& x : v)
    {
        cout << x << endl;   
    }
}
