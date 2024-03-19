// 백준 2581

#include <iostream>
#include <cmath>

using namespace std;

// 소수 판별
int is_prime(int x) {
    if(x==1){
        return 0;
    }
    for(int i = 2; i < int(sqrt(x)+1); i++){
        if(x%i == 0){
            return 0;
        }
    }
    return 1;
}

int main() {
    int M;
    int N;

    cin >> M >> N;

    int sum;
    int min;
    sum = 0;
    min = N;

    for(int i=M; i < N+1; i++) {
        if(is_prime(i)==1){
            sum += i;
            if(min > i) {
                min = i;
            }
        }
    }
    if(sum==0) {
        cout << -1;
    }
    else{
        cout << sum << endl;
        cout << min;
    } 
}