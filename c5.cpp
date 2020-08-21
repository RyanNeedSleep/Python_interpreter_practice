#include <iostream>

using namespace std; 

int main(){
    enum color{
        red,
        blue, 
        black
    };
    
   enum class card{
        red,
        blue,
        black
   }; 
   color x = color::red;
   int y = x; 
}
