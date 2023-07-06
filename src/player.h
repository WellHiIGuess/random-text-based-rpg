#include <stdio.h>


typedef struct player {
    float health;
    float maxHealth;

    // Stats
    float strength; // Phyisical capabilities
    float indurance; // Physical ressistance
    float dextarity; // Movement capabilities
    float vigor; // Mental strength
    float inteligence; // Mental capabilities
} Player;


Player playerInit() {
    FILE *fptr;
    char reading[100];
    char read[100];

    fptr = fopen("src/player_data.json", "r");

    while (fgets(reading, 100, fptr)) {
        strcat(read, reading);
    }

    fclose(fptr);

    

    return (Player){0, 0, 0, 0, 0, 0, 0};
}
