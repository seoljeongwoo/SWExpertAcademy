#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
vector<int>ans;
vector<int>dp;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int TC; cin >> TC;
	for (int Testcase = 1; Testcase <= TC; Testcase++) {
		
		ans.clear(); dp.clear();
		int N; cin >> N;
		ans.resize(N + 1);
		dp.resize(N + 1, 0);
		for (int i = 1; i <= N; i++) {
			cin >> ans[i];
		}
		for (int i = 1; i <= N; i++) {
			if (dp[i - 1] + ans[i] <= ans[i]) dp[i] = ans[i];
			else dp[i] = dp[i - 1] + ans[i];
		}
		int ret = -987654321;
		for (int i = 1; i <= N; i++) ret = max(ret, dp[i]);
		cout << "#" << Testcase << " " << ret << "\n";
	}
}