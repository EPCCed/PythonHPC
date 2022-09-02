#define SEED  5743

int initroad(int *road, int n, float density, int seed);
void updatebcs(int *road, int n);
int updateroad(int *newroad, int *oldroad, int n);
double gettime();
