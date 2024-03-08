#include <iostream>
#include <string>
using std::string;
using std::cout;
using std::endl;

int main() {
    int A;
    std::string B;

    std::cin >> A;
    std::cin >> B;

    std::string str3(1, B[0]);
    std::string str2(1, B[1]);
    std::string str1(1, B[2]);

    int B_1 = stoi(str1);
    int B_2 = stoi(str2);
    int B_3 = stoi(str3);

    int result1 = A * B_1;
    int result2 = A * B_2;
    int result3 = A * B_3;

    int result4 = result1 + result2*10 + result3*100;
    
    cout << result1 << endl;
    cout << result2 << endl;
    cout << result3 << endl;
    cout << result4 << endl;

    
    return 0;
}