#include <iostream>

using namespace std;

void copy_array(int* p1, int* p2){
    for(int i = 0; i < 10; i++){
        p2[i] = p1[i];
    }
 }

void print(int* x){
    for(int i = 0 ; i < 10; i++){
    cout << x[i] << " " ;
    }
    cout << endl;
}

int main(){
    int x[10];
    for(int i=0; i < 10; i++){
        x[i] = i;
    }
    
    int  p2[10];
    copy_array(x, p2);
    
    print(x);
    print(p2;
}
