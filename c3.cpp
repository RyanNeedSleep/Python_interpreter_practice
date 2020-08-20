#include <iostream>

using namespace std;

int main()
{
    int* p;
    
    for(int i = 0; i < 5; i++)
    {
        *p = i;
        cout << *p << endl;
        p = p + 1;
    }
    
    cout << "==============" << endl;

    p = p - 5;
    for(int i = 0; i < 5; i++)
    {
        cout << *p << " ";
        p++;
    }
    cout << endl;
}
