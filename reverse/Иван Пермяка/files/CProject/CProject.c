#include <stdio.h>
#include <string.h>

char shift_char(unsigned int c);
void encrypt_flag(const char* s, char* encrypted);

int main(int argc, const char** argv, const char** envp) {
    char s1[256];
    char s[256];
    char s2[48] = "8HA!c2_@M99#P_B$a_C%yHA^lwc&7O0*L0R(JW";

    printf("flag: ");
    fgets(s, sizeof(s), stdin);
    s[strcspn(s, "\n")] = 0;

    encrypt_flag(s, s1);

    if (!strcmp(s1, s2)) {
        puts("Good!");
    }
    else {
        puts("Bad!");
    }

    return 0;
}

void encrypt_flag(const char* s, char* encrypted) {
    char special_chars[] = "!@#$%^&*()";
    char s_shifted[256];
    int len = strlen(s);
    int i, j, k;
    int special_char_index = 0;
    int encrypted_index = 0;

    for (i = 0; s[i]; ++i) {
        s_shifted[i] = shift_char((unsigned int)s[i]);
    }
    s_shifted[len] = 0;

    for (j = 0; j < len / 2; ++j) {
        char temp = s_shifted[j];
        s_shifted[j] = s_shifted[len - j - 1];
        s_shifted[len - j - 1] = temp;
    }

    for (k = 0; s_shifted[k]; ++k) {
        encrypted[encrypted_index++] = s_shifted[k];
        if ((k + 1) % 3 == 0 && s_shifted[k + 1]) {
            encrypted[encrypted_index++] = special_chars[special_char_index++ % 10];
        }
    }
    encrypted[encrypted_index] = 0;
}

char shift_char(unsigned int c) {
    const char* dictionary = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ{}";
    const int dict_size = 62 + 2;
    const int shift = 9;

    const char* pos = strchr(dictionary, c);
    if (pos) {
        int index = (int)(pos - dictionary);
        return dictionary[(index + shift) % dict_size];
    }
    return (char)c;
}