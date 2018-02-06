import java.util.ArrayList;  //import ArrayList from java.util. This is a resizeable Array type
public class ShoppingList {				//Declare our class. Every file is a class in java
	public static void main(String[] args) {		//main method
		
			ArrayList<String> shoppingList = new ArrayList<String>();	// To create a new ArrayList object from the ArrayList java class. Set the new object to our array "shoppingList"

shoppingList.add("Milk");	//Use the built in methods to add items to our ArrayList.
shoppingList.add("Beef");
shoppingList.add("Bread");
shoppingList.add("Eggs");
shoppingList.add("Beef");
shoppingList.add("Chicken");

 //ArrayLists dont have a length, but rather a size() method. This is because we can resize our arraylist by adding or removing elements. We can use this to iterate our arraylist.

for(int i=0; i < shoppingList.size(); i++){
	// Also notice that we cannot treat arraylists like an array to access its values. We must call the get() method on our list followed by the index we wish to access to retrieve its value.

	System.out.println(shoppingList.get(i));
		}

// We can also use the enhanced for loop, which lets us access the values without the need to refer to an index. This is useful in the case that we dont care about the index and just want the value. If you do need the index however, use a regular for loop like we've done above.
for(String stuff: shoppingList){
	System.out.println(stuff);
}


	}
}