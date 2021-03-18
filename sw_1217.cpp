#include <iostream>
using namespace std;
int solve(int n,int k){
    if (k==0) return 1;
    if (k==1) return n;
    int ret = solve(n,k/2);
    ret = ret*ret;
    if(k%2==1) ret*=n;
    return ret;
}
int main(){
    ios_base :: sync_with_stdio(false);
    for(int i=0; i<10; i++){
        int testcase; cin>>testcase;
        int n,m; cin >> n>> m;
        cout << "#" << testcase << " " << solve(n,m) << endl;
    }
}