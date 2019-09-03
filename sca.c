#include<stdio.h>
#include<conio.h>
#include<graphics.h>
void tra(int r[][2],int t[])
{
rectangle(r[0][0],r[0][1],r[1][0],r[1][1]);
r[0][0]=r[0][0]*t[0];
r[0][1]=r[0][1]*t[1];
r[1][0]=r[1][0]*t[0];
r[1][1]=r[1][1]*t[1];
rectangle(r[0][0],r[0][1],r[1][0],r[1][1]);
}
void main()
{
int gd=DETECT,gm;
int x1,y1,x2,y2,s1,s2;
int r[2][2];
int t[2];
initgraph(&gd,&gm,"C:\\TURBOC3\\BGI");
printf("Enter co-oridnates of recgtangle : ");
scanf("%d%d%d%d",&x1,&y1,&x2,&y2);
printf("Enter points to shift the rectangle:");
scanf("%d%d",&s1,&s2);
r[0][0]=x1;
r[0][1]=y1;
r[1][0]=x2;
r[1][1]=y2;
t[0]=s1;
t[1]=s2;
tra(r,t);
getch();
}
