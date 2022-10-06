#include <stdio.h>

int main(){
	
	int a,w,h;
	int min,i;
	int s[3];
	
	while(1){
		
		min = 0;
		
		for(i=0;i<3;i++){
			
			scanf("%d",&s[i]);
			
		}
		
		for(i=0;i<3;i++){

			if(s[i]>min){
				min = s[i];
			}
			
		}
		
	    if(s[0] == 0 && s[1] == 0 && s[2] == 0){
	    	break;
		}
	    else if(s[0] == s[1] && s[1] == s[2]){
	    	printf("wrong\n");
		}
	    
	    else if(s[0] == min && min*min == s[1]*s[1] + s[2]*s[2]){
	    	printf("right\n");
		}
		else if(s[1] == min && min*min == s[0]*s[0] + s[2]*s[2]){
			printf("right\n");
		}
		else if(s[2] == min && min*min == s[0]*s[0] + s[1]*s[1]){
			printf("right\n");
		}
		else printf("wrong\n");
			
	}
	
}