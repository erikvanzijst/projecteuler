#define __STDC_FORMAT_MACROS
#include <inttypes.h>
#include <stdio.h>

int xx = 20;
int yy = 20;

uint64_t step(int x, int y, uint64_t total) {
    if (x == xx && y == yy)
        return total + 1;
    if (x < xx)
        total = step(x + 1, y, total);
    if (y < yy)
        total = step(x, y + 1, total);
    return total;
}

int main(int argc, char** argv) {
  printf("%" PRIu64 "\n", step(0, 0, 0));
}
