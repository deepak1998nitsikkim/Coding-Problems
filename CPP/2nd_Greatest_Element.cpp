// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;

int main() {
    
    int m1,m2;
    int a[5]={2,3,1,6,20};
    
    if(a[0]>a[1])
    {
        m1=a[0];
        m2=a[1];
    }
    
    else
    {
        m1=a[1];
        m2=a[0];
    }
    
    for(int i=2;i<5;i++)
    {
        if(a[i]>m1)
        {
            m2=m1;
            m1=a[i];
        }
        else if(a[i]>m2)
        {
            m2=a[i];
        }
    }
    cout<<m2;

    return 0;
}
