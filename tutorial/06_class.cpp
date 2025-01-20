#include <iostream>
#include <string>
using namespace std;

class Person {
private:
    string name;
    int age;

public:
    Person(string name, int age) : name(name), age(age) {}

    void sayHello() {
        cout << "Hello, my name is " << name << ", I am " << age << " years old." << endl;
    }
};

int main() {
    Person p("Alice", 20);
    p.sayHello();
    return 0;
}
