// // Passing parameters by reference.
// #include <iostream>
// using namespace std;

// void Duplicate(int& a, int& b, int& c) {
//   a *= 2;
//   b *= 2;
//   c *= 2;
// }

// int main() {    
//   int x = 1, y = 3, z = 7;
//   Duplicate(x, y, z);
//   // The following outputs: x=2, y=6, z=14.
//   cout << "x="<< x << ", y="<< y << ", z="<< z;
//   return 0;
// }

#include <iostream>
using namespace std;

int main() {
    int* x;
    int* y;

    int x_value = 5;
    int y_value = 10;

    x = &x_value;

    cout << "x is " << *x << "";

    return 0;
}