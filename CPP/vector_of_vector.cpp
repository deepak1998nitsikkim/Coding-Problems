#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {
    
    int n,m;
    
    cout<<"enter n : ";
    cin>>n;
    
    vector<vector<int>> v;
    
    for(int i=0;i<n;i++)
    {
    
        cout<<"enter m : ";
        cin>>m;
        
        vector<int> t;
        for(int j=0;j<m;j++)
        {
            int x;
            
            cout<<"enter x : ";
            cin>>x;
            
            t.push_back(x);
        }
        v.push_back(t);
    }
    
    for(int i=0;i<n;i++)
    {
        for(int j=0;j<v[i].size();j++)
        {
            cout<<v[i][j]<<" ";
        }
        cout<<endl;
    }

    return 0;
}
