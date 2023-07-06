#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include "JSONKit/JSONKit.h"
#include "player.h"


int main() {
    Player player = playerInit();

    while (0) {
        // game loop
        char input[20];
        fgets(input, 20, stdin);

        for (int i = 0; i < 20; i++) {
            input[i] = tolower(input[i]);
        }

        if (strcmp("quit\n", input) == 0) {
            return 0;
        }
    }

    return 0;
}

