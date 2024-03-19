// 백준 24264

#include <iostream>

using namespace std;

int main() {
    long n;
    long sum;
    cin >> n;

    sum = n * n;
    if (n==1) {
        cout << 1 << endl << 2;
    }
    else {
        cout << sum << endl << 2;
    }
}