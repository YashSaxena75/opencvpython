#include<stdio.h>

void search(int a[],int lb,int ub,int x)
{
    int mid;
    if(lb==ub)
    {
        if(a[lb]==x)
            printf("Element found at position : %d \n" , lb+1);
        else
            printf("Element not found ! \n");
    }

    else
    {
        mid=(lb+ub)/2;
        if(a[mid]==x)
            printf("Element found at position : %d \n" ,mid+1);
        else if (a[mid]<x)
            search(a,mid+1,ub,x);
        else
            search(a,lb,mid-1,x);
    }
}
int main()
{
    int n,a[100],i,x,ub,lb,mid;
    printf("Yash Saxena 170111049\n\n\n");
    printf("Enter length : ");
    scanf("%d",&n);
    lb=0;ub=n;
    printf("Enter array elements : ");
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    printf("Enter the element to search for : ");
    scanf("%d",&x);
    search(a,lb,ub,x);
    return 0;
}
