#include <iostream>
using namespace std;

int main() {
    for (int i = 0; i < 5; i++) {
        cout << "i = " << i << endl;
    }

    int j = 0;
    while (j < 5) {
        cout << "j = " << j << endl;
        j++;
    }

    int arr[] = {1, 2, 3, 4, 5};
    for (int num : arr) {
        cout << "num = " << num << endl;
    }

    return 0;
}
