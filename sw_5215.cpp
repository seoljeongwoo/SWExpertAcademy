#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;
int dp[21][10001];
int arr[21][2];
int n,l;
int solve(int curr, int s){
    if (curr==n) return 0;
    int &ret = dp[curr][s];
    if(ret != -1) return ret;
    ret = solve(curr+1,s);
    if(arr[curr][1] + s <= l) ret = max(ret, solve(curr+1,arr[curr][1] + s) + arr[curr][0]);
    return ret;
}
int main(){
    ios_base :: sync_with_stdio(false);
    int testcase; cin>>testcase;
    for(int i=1; i<=testcase; i++){
        memset(dp,-1,sizeof(dp));
        cin >> n>> l;
        for(int j=0; j<n; j++){
            cin >> arr[j][0] >> arr[j][1];
        }
        cout << "#"<<i << " "<<solve(0,0) << endl;
    }
}