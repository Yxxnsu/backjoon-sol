#include <stdio.h>

int main(){
	
	int i;
	int num,num1;
	
	scanf("%d %d",&num,&num1);
	
	int a[num];
	
	for(i=0;i<num;i++){
		a[i] = 0;
		scanf("%d",&a[i]);
	}
	
    for(i=0;i<num;i++){
    	
    	if(a[i]<num1){
    		printf("%d ",a[i]);
		}
	}

}