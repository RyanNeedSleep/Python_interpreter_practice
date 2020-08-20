# include <iostream>
# include <complex>
# include <vector>

using namespace std; 

double square(double x){
    return x*x;
}

int main(){
    int a = 1;
    int b[3] = {1, 2, 3};
    int* p = &b[1];

    cout << "value: " << a << endl << "address: " << &a << endl;
    cout << "=========================" << endl;
    cout << "value: " << b << endl <<  "address: " << &b[1] << endl;

    cout << "b - &b[1]: " << (b - p) << endl;
    cout << "content of p: " << p << endl;
}





