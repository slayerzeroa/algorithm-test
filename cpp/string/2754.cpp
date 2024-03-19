#include <string>
#include <iostream>
#include <vector>

using namespace std;

string check(string input);

int main() {
    string input;
    cin >> input;
    cout << check(input);
}

string check(string input) {
    if(input == "A+") {
        return "4.3";
    } else if(input == "A0") {
        return "4.0";
    } else if(input == "A-") {
        return "3.7";
    } else if(input == "B+") {
        return "3.3";
    } else if(input == "B0") {
        return "3.0";
    } else if(input == "B-") {
        return "2.7";
    } else if(input == "C+") {
        return "2.3";
    } else if(input == "C0") {
        return "2.0";
    } else if(input == "C-") {
        return "1.7";
    } else if(input == "D+") {
        return "1.3";
    } else if(input == "D0") {
        return "1.0";
    } else if(input == "D-") {
        return "0.7";
    } else if(input == "F") {
        return "0.0";
    }
    return "0";
}