#include <iostream>
#include <time.h>
using namespace std;

int main () {
  int random_number;
  int input_var = 0;

  // Initialize random seed.
  srand (time(NULL));

  // Generate random number between 1 and 100
  random_number = rand() % 100 + 1;

  do {
    cout << "Enter a number (-1 = quit): ";
    if (!(cin >> input_var)) {
        cout << "You entered a non-numeric. Exiting..." << endl;
        break;
    }
    if (input_var > random_number) {
        cout <<  "Number is too big!" << endl;
    }
    if (input_var < random_number) {
        cout <<  "Number is too small!" << endl;
    }
    if (input_var == random_number) {
        cout << "Correct Number!" << endl;
        break;
    }
  } while (input_var != -1);
  cout << "All done." << endl;
  return 0;
}