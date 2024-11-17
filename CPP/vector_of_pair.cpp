// Online C++ compiler to run C++ program online
#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {
    
    vector<pair<int,string>> v;
    
    int n,fe;
    string se;
    
    cout<<"enter the range of vector : ";
    cin>>n;
    
    for(int i=0;i<n;i++)
    {
        cout<<"\nenter vector first element : ";
        cin>>fe;
        
        cout<<"\nenter vector second element : ";
        cin>>se;
        
        v.push_back({fe,se});
    }
    
    for(int i=0;i<n;i++)
    {
        cout<<v[i].first<<" "<<v[i].second<<endl;
    }

    return 0;
}
