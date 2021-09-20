/*#include<stdio.h>

int fulltime ():
int parttime();
int main()
{
 if staff == fulltime
 { 
  fulltime()
 }
 if staff == parttime
 {
  parttime()
 } 
}
int fulltime()
{

  float basic_salary;
  float deductions;
  float net_pay = basic_salary - deductions;
  printf("Your Net salary is: %f",net_pay);
}

int partime()
{
  int hours;
  print("Enter the number of hours worked this month: ");
  scanf("%d",&hours)
  int total_pay = 2500 * hours;
  tax = total_pay * 0.3;
  net_pay = total_pay - tax;
  printf("Your Net pay is: %f",net_pay);
} */

#include <stdio.h>
#include <string.h>
int main(void)
/* This program gets user input from user
   it should calculate the net pay of user where user can be full or part time
   A full time user has a basic pay less statutory deductions whic gives net pay
   A part user is paid by the hour at a rate of 2500 and pays 30% tax at the end of the month */
{
  //declare variables
   char f[30];
   char p[30];
   char name_f[30], name_p[30];
   int no, no_p;
    float basic, deduct, netpay;
    int hours;
    int one;
    int answer;
   const int parttime_perhr = 2500;

  // This part should ask the user if they are a full or part time employ
  // An if condition can do this well
 
   while(1){
            printf("Enter category of staff! \n");
            gets(&f); // try and use scanf
            gets(&p);
       printf("Enter full time staffName\n");
       gets(name_f);
       printf("Enter full time Number\n");
       scanf("%d",&no);
       printf("Enter Part time staffName\n");
       scanf("%s",name_p);
       printf("Enter Part time Number\n");
       scanf("%d",&no_p);
       printf("Full time netpay:\n");
       printf("Enter basic pay of fulltime:\n");
       scanf("%f",&basic);
       printf("Enter deduction amount:\n");
       scanf("%f",&deduct);
       netpay = basic - deduct;
       printf(" Netpay: %f \n", netpay);
       //part time
       printf("Enter number of hours worked of part time worker \n");
       scanf("%d",&hours);
       int parttime_pay = parttime_perhr * hours;
       printf("Parttime pay:%d", parttime_pay);
       printf("\n");
       printf("Do you want to continue with the program? \n");
       printf("Enter 1 to continue or any other digit to terminate the program \n");
        scanf("%d",&answer);
        if(answer == 1){
        continue;
        }
        break;
   }
   printf("you quit");
}
