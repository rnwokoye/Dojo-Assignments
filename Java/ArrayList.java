import java.util.ArrayList;
public class ArrayList {
	public static void main(String[] args) {
		
			ArrayList<String> shoppingList = new ArrayList<String>();

shoppingList.add("Milk");
shoppingList.add("Beef");
shoppingList.add("Bread");
shoppingList.add("Eggs");
shoppingList.add("Beef");
shoppingList.add("Chicken");

for(int i=0; i < shoppingList.size(); i++){
	System.out.println(shoppingList.get(i));
		}

	}



}