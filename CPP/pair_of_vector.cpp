#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {
    
    pair<vector<int>,vector<int>> p[3];
    
    for(int i=0;i<2;i++)
    {
        
        vector<int> t1;
        vector<int> t2;
        
        for(int j=0;j<2;j++)
        {
            int x,y;
            cout<<"enter value of x and y : ";
            cin>>x>>y;
            
            t1.push_back(x);
            t2.push_back(y);
            
            
        }
        p[i]=make_pair(t1,t2);
    }
    
    for(int i=0;i<2;i++)
    {
        cout<<endl<<"first vector : ";
        
        for(int x:p[i].first)
        {
            cout<<x<<" ";
        }
        
        
        cout<<endl<<"second vector : ";
        for(int y:p[i].second)
        {
            cout<<y<<" ";
        }
    }

    return 0;
}
