#include <iostream>
using namespace std;

int main () {
    int horse = 10;
    int pig = 3;
    float rabbit = 0.5;

    for (int i = 0; i <= 10; ++i) {
        for (int j = 0; j<=34; ++j) {
            for (int k = 0; k <= 200; ++k) {
                if ((i*horse+j*pig+k*rabbit) == 100 && (i+j+k == 100)) {
                    cout << i << " ";
                    cout << j << " ";
                    cout << k << " ";
                    return 0;
                }
            }
        }
    }
}