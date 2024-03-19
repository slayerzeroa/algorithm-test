// 백준 27433

#include <iostream>

using namespace std;

long long factorial(long long N) {
    if (N<=1) {
        return 1;
    }
    return N * factorial(N-1);
}


int main() {
    long long N;
    cin >> N;
    
    cout << factorial(N);
    return 0;
}


// #include <iostream>
// using namespace std;

// long long factorial(long long N) {
//     if (N <= 1) {
//         return 1;
//     }
//     return N * factorial(N - 1);
// }

// int main() {
//     long long N;
//     cin >> N;
    
//     cout << factorial(N);
//     return 0;
// }