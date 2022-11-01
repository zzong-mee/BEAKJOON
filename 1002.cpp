#include <stdio.h>
#include <math.h>

int main() {

	int t, x1, x2, r1, y1, y2, r2, i;
	double dt, minus;

	scanf("%d", &t);

	for (i = 0; i < t; i++) {
		scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2);

		dt = sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1));
		minus = (r1 > r2) ? (r1 - r2) : (r2 - r1);

		int r_sum = r1 + r2;

		if (!dt && r1 == r2) {
			printf("-1\n");
		}
		else if (dt < r_sum && dt > minus) {
			printf("2\n");
		}
		else if (dt == r_sum || minus == dt) {
			printf("1\n");
		}
		else printf("0\n");
	}

	return 0;
}