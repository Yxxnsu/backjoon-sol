#include <stdio.h>

int main(){
	
	int i,num,hap=0;
	int num1,num2;
	
	scanf("%d",&num);

	for(i=0;i<num;i++){
		
		scanf("%d %d",&num1,&num2);
		hap = num1 + num2;
		printf("%d\n",hap);
	}
	

}