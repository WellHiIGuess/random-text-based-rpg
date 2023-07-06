#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include "JSONKit/JSONKit.h"
#include "player.h"


int main() {
    while (1) {
        // game loop
        char input[20];
        fgets(input, 20, stdin);

        for (int i = 0; i < 20; i++) {
            input[i] = tolower(input[i]);
        }

        if (strcmp(input, "quit") != 0) {
            return 0;
        }
    }

    return 0;
}

