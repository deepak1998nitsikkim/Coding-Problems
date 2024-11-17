#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {
    
    vector<int> v;
    
    for(int i=0;i<5;i++)
    {
        int x;
        cout<<"enter value : ";
        cin>>x;
        v.push_back(x);
    }
    vector<int>::iterator it;
    
    for(it=v.begin();it!=v.end();++it)
    {
        cout<<*it<<" ";
    }

    return 0;
}
