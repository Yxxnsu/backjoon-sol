#include <stdio.h>

int main(){
	
	
	int i,num,max,min;
	
	scanf("%d",&num);
	
	int a[num];
	
	for(i=0;i<num;i++){
		a[i] = 0;
		scanf("%d",&a[i]);
	}

    max = min = a[0];
    
  	for(i=0;i<num;i++){
  		
  		if(a[i]>=max)max=a[i];
  		
  		if(a[i]<=min)min=a[i];

    }
		
	printf("%d %d",min,max);
}