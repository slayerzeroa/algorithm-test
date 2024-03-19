// 백준 25206

#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<string> split(string str, char delimiter);
double gpatodouble(std::string input);

int main() {
    double gpa = 0.0;
    int time;
    int totaltime = 0;
    string query;
    double gpa1 = 0.0;
    for(int i=0; i<20*3; i++) {
        cin >> query;
        if (i % 3 == 1) {
            time = stoi(query);
            totaltime += time;
        } else if (i % 3 == 2) {
            gpa1 = gpatodouble(query);
            if (gpa1 != -1.0) {
                gpa += time * gpa1;
            } else {
                totaltime -= time;
            }
        }
    }
    cout << gpa/totaltime << endl;
}


double gpatodouble(string input) {
    if (input == "A+") {
        return 4.5;
    } else if (input == "A0") {
        return 4.0;
    } else if (input == "B+") {
        return 3.5;
    } else if (input == "B0") {
        return 3.0;
    } else if (input == "C+") {
        return 2.5;
    } else if (input == "C0") {
        return 2.0;
    } else if (input == "D+") {
        return 1.5;
    } else if (input == "D0") {
        return 1.0;
    } else if (input == "F") {
        return 0.0;
    } else if (input == "P") {
        return -1.0;
    }
    return 0.0;
}