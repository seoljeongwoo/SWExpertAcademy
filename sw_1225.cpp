#include <iostream>
#include <queue>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    for(int i=0; i<10; i++){
        int testcase; cin>> testcase;
        deque <int> q;
        for(int j=0; j<8;j++){
            int value; cin >> value;
            q.push_back(value);
        }

        while(true){
            bool ok = true;
            for(int j=1; j<=5; j++){
                if(q.front() - j <=0){
                    q.pop_front(); q.push_back(0);
                    ok=false; break;
                }
                else{
                    q.push_back(q.front() - j);
                    q.pop_front();
                }
            }
            if (!ok) break;
        }
        cout << "#" << testcase << " " ;
        while(!q.empty()){
            cout << q.front() << " ";
            q.pop_front();
        }
        cout << endl;
    }
}