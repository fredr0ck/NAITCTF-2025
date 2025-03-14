#include <iostream> 
#include <string> 

int main() {
    std::string password;

    do {
        std::cout << "Password:\n";
        std::getline(std::cin, password);

        if (password != "NAITCTF{d3bug_3v3ryth1ng}") {
            std::cout << "Incorrect password. Repeat please..." << std::endl;
        }
    } while (password != "NAITCTF{d3bug_3v3ryth1ng}");

    std::cout << "Password accepted\n";

    return 0;
}
