//백준 1057
#include <iostream>

using namespace std;

int check(int num);

int main() {
    int N;
    int p;
    int q;
    int n = 0;
    cin >> N >> p >> q;

    while (true) {
        p = check(p);
        q = check(q);
        if (p==q) {
            n = n+1;
            cout << n;
            break;
        }
        n = n+1;
    }
}


int check(int num) {
    if (num % 2 == 1) {
        num = (num+1) / 2;
    } else {
        num = num / 2;
    }

    return num;
}