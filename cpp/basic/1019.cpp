#include <iostream>
#include <string>
#include <map>

using namespace std;

int main()
{
    string A;
    string B;
    cin >> A;
    map<string, int> myMap;
    myMap["1"] = 0;
    myMap["2"] = 0;
    myMap["3"] = 0;
    myMap["4"] = 0;
    myMap["5"] = 0;
    myMap["6"] = 0;
    myMap["7"] = 0;
    myMap["8"] = 0;
    myMap["9"] = 0;
    myMap["0"] = 0;

    for (int count = 1; count <= stoi(A); ++count)
        {
            to_string(count) = B;
            int length = B.size();
            
            for (int c = 0; c <= length; ++c)
            {
                int elem = myMap[B[c]]


            }

        }
}