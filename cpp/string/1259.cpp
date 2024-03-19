// 백준 1259

#include <string>
#include <iostream>
#include <vector>

using namespace std;

string check(string input);

int main() {
    string input;
    string result;

    while (true){
        cin >> input;
        if (input == "0"){
            break;
        }
        else {
            result = check(input);
            cout << result << endl;   
        }
    }
}

string check(string input) {
    int size = input.size();
    if (size % 2 == 0) {
        for(int i = 0; i < size / 2; i++) {
            if (input[i] != input[size-1-i]) {
                return "no";
            }
        }
        return "yes";
    } else {
        if (size == 1) {
            if (input != "0") {
                return "yes";
            }
        }
        else { // 길이가 홀수 일 때
            for(int i = 0; i < ((size-1) / 2); i++) {
                if (input[i] != input[size-1-i]) {
                    return "no";
                }
            }
            return "yes";
        }
    }
    return 0;
}