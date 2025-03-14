#include <iostream>
#include <windows.h>

bool is_debugger_active() {
    return IsDebuggerPresent();
}

std::string getHiddenFlag() {
    char key[] = { 'N', 'A', 'I', 'T', 'C', 'T', 'F', '{', 'S', 'T','R','0', 'N','G', '_', 'Y', '3', 'A','?','}', '\0' };
    for (int i = 0; i < sizeof(key) - 1; i++) {
        key[i] ^= 0x42;
    }
    return std::string(key);
}

int main() {
    if (is_debugger_active()) {
        std::cout << "Debugger Detected!" << std::endl;
        return 1;
    }

    std::string userInput;
    std::cout << "Write flag: ";
    std::cin >> userInput;

    std::string flag = getHiddenFlag();

    for (int i = 0; i < flag.size(); i++) {
        flag[i] ^= 0x42;
    }

    if (userInput == flag) {
        std::cout << "Good! flag: " << flag << std::endl;
    }
    else {
        std::cout << "Wrong flag!" << std::endl;
    }

    return 0;
}
