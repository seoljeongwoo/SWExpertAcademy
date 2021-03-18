#include <iostream>
#include <utility>
using namespace std;
int gap[10001][2];
int ind;
void cal(int v, int &a, int &b){
    for(int i=1; i<ind; i++){
        if(gap[i][0] <= v && v <= gap[i][1]){
            int gg = v-gap[i][0];
            a = 1+gg;
            b = i-gg;
            return;
        }
    }
}
int recal(int x, int y){
    int idx = x+y-1;
    int cnt = gap[idx-1][1]+1;
    cnt += (x-1);
    return cnt;
}
void preprocess(){

    int l=1,r=1,g =1;
    ind =1;
    while(true){
        if (ind >=400) break;
        
        gap[ind][0] = l;
        gap[ind][1] = r;
        l = r+1;
        r = l+g;
        g++;
        ind++;
    }
}
int main(){
    ios_base :: sync_with_stdio(false);
    preprocess();
    int tc ; cin >> tc;
    for(int i=1; i<=tc; i++){
        int p,q,px,py,qx,qy,nx,ny;
        cin >> p >> q;
        cal(p,px,py);
        cal(q,qx,qy);
        nx = px+qx;
        ny = py+qy;
        int ret = recal(nx,ny);
        cout << "#" << i << " " << ret << endl;
    }
}