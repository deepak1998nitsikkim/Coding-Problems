#include <iostream>
using namespace std;

int main() {
    
    int a[100] = {1,5,4,3};
    int l,r;
    
    cout<<"enter left and right : ";
    cin>>l>>r;
    
    for(int i=l;i<=r;i++)
    {
        int f=0;
        
        for(int j=0;j<4;j++)
        {
            if(i==a[j])
            {
                f=1;
                break;
            }
        }
        
        if(f==0)
        {
            cout<<i<<" ";
        }
    }
    return 0;
}