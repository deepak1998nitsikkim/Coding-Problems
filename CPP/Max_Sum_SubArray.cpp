// Online C++ compiler to run C++ program online
#include <iostream>
using namespace std;

int main() {
    // Write C++ code here
    int a[6]={1,2,3,4,5,6};
    int s=2;
    
    for(int i=0;i<6-s+1;i++)
    {
        for(int j=i;j<s+i;j++)
        {
            cout<<a[j];
        }
        cout<<endl;
    }

    return 0;
}
