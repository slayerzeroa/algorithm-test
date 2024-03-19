// 백준 10773

#include <iostream>
#include <stack>

using namespace std;

int main() {
    stack<int> S;
    int K;
    int M;
    cin >> K;

    for(int i=0; i<K; i++){
        cin >> M;
        if (M == 0) {
            S.pop();
        }
        else {
            S.push(M);
        }
    }
    
    int sum;
    sum = 0;

    int top_num;

    while (!S.empty()) {
        top_num = S.top();
        sum += top_num;
        S.pop();
    }
    
    cout << sum;
}
