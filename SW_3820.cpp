#include <iostream>
#include <algorithm>
#include <utility>
using namespace std;
#define MAX_N 200001
#define MOD 1000000007
typedef pair<long long , long long >pll;
int N;
pll arr[MAX_N];
void input() {
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> arr[i].first >> arr[i].second;
	}
}
bool cmp(const pll& A, const pll& B) {
	return A.second * (B.first - 1) < B.second * (A.first - 1);
}
void speed(long long &ret) {
	for (int i = 0; i < N; i++) {
		ret = arr[i].first * ret + arr[i].second;
		ret %= MOD;
	}
}
void solve() {
	int tc; cin >> tc;
	for (int Test = 1; Test <= tc; Test++) {
		cout << "#" << Test << " ";
		input();
		sort(arr, arr + N, cmp);
		long long ret = 1;
		speed(ret);
		cout << ret << "\n";
	}
}
int main() {
	ios_base::sync_with_stdio(false);
	solve();
}