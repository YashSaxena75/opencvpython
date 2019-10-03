#include <bits/stdc++.h>
using namespace std;
void heapify_me(int a[],int n,int i)
{
    int large=i;
    int l=2*i+1;
    int r=2*i+2;
    if(l<n && a[l]>a[large])
        large=r;
    if(r<n && a[r]>a[large])
        large=l;
    if(large!=i)
    {
        swap(a[i],a[large]);
        heapify_me(a, n, large);
    }

}

void sort_me(int a[],int n)
{

    for(int i=n/2-1;i>=0;i--)
    {
        heapify_me(a,n,i);
    }
    for(int i=n-1;i>=0;i--)
    {
    	swap(a[0],a[i]);
    	heapify_me(a,i,0);
    }
}
int main()
{
    int n,a[100],i;
    cout<<"Yash Saxena 170111049\n\n"<<endl;
    cout<<"Enter array size :" ;
    cin>>n;
    printf("Enter array elements : ");
    for(i=0;i<n;i++)
    {
        cin>>a[i];
    }
    sort_me(a,n);
    cout<<"Sorted array is : " ;
    for(i=0;i<n;i++)
        cout<<a[i];
    return 0;
}
