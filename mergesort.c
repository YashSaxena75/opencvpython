#include<stdio.h>
int merge(int a[],int lb,int ub,int mid)
{
    int s,i,j,k,n;
    s=ub-lb;
    int b[s];
    i=lb;
    j=mid+1;
    k=1;
    while(i<=mid && j<=ub)
    {
        if(a[i]<=a[j])
            b[k++]=a[i++];
        else
            b[k++]=a[j++];
    }
    if(i>mid)
    {

        while(j<=ub)
            b[k++]=a[j++];
    }
    else
    {
        while(i<=mid)
            b[k++]=a[i++];
    }
k=1;
for(i=lb;i<=ub;i++)
    a[i]=b[k++];


}
int div(int a[],int lb,int ub)
{
    int m;
    if(lb<ub)
    {
        m=(lb+ub)/2;
        div(a,lb,m);
        div(a,m+1,ub);
        merge(a,lb,ub,m);
    }

}

int main()
{
    int a[100],n,i,lb,ub;
    printf("Yash Saxena 170111049\n\n\n");
    printf("Enter array size : ");
    scanf("%d",&n);
    printf("Enter array elements : ");
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    lb=0;
    ub=n-1;
    div(a,lb,ub);
    printf("Sorted array is : ");
    for(i=0;i<n;i++)
    {
        printf(" %d ",a[i]);
    }

}
