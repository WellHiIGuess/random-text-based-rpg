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
    char read[100];

    fptr = fopen("player_data.json", "r");

    fgets(read, 100, fptr);

    return (Player){0, 0, 0, 0, 0, 0, 0};
}
