public class BasicJava{
	public void printNums(){
		for(int i=1; i < 256; i++){
			System.out.println(i);
		} 
	}
	public void printOddNums(){
		for(int i=1; i < 256; i++){
			if(i % 2 != 0){
				System.out.println(i);
			}
		}
	}
	public void printSum(){
		int sum = 0;
		for(int i=0; i < 256; i++){ 
			sum+= i; 
			System.out.println(sum);
		}

	}

}