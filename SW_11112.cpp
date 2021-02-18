#include <iostream>
using namespace std;
int p, q, r, a, b, c, d;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	int TC; cin >> TC;
	for (int i = 1; i <= TC; i++) {
		cout << "#" << i << " ";
		cin >> p >> q >> r >> a >> b >> c >> d;
		if (a <= p - r && p + r <= c && b <= q - r && q + r <= d) cout << "N";
		else cout << "Y";

		if (((p - a) * (p - a) + (q - b) * (q - b) <= r * r) && ((p - a) * (p - a) + (q - d) * (q - d) <= r * r) && ((p - c) * (p - c) + (q - b) * (q - b) <= r * r) && ((p - c) * (p - c) + (q - d) * (q - d) <= r * r)) cout << "N";
		else cout << "Y";
		cout << "\n";
	}
}