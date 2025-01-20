#include <iostream>
using namespace std;

int main() {
    int score = 85;

    if (score >= 90) {
        cout << "Excellent!" << endl;
    } else if (score >= 70) {
        cout << "Good!" << endl;
    } else {
        cout << "Need more effort." << endl;
    }

    int day = 3;
    switch (day) {
        case 1:
            cout << "Monday" << endl;
            break;
        case 2:
            cout << "Tuesday" << endl;
            break;
        case 3:
            cout << "Wednesday" << endl;
            break;
        default:
            cout << "Other day" << endl;
            break;
    }

    return 0;
}
