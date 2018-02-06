package com.funJava.advancedOOP;

import java.util.ArrayList;

public class Pokedex extends AbstractPokemon {
	public ArrayList<Object> pokemonInfo(Pokemon pokemon){
		ArrayList<Object> info = new ArrayList<Object>();
		info.add( pokemon.getName() );
		info.add( pokemon.getType() );
		info.add( pokemon.getHealth() );
		
	return info;
	
	}
	
	public static void main(String[] args) {
		Pokedex pokedex = new Pokedex();
		Pokemon pikachu = pokedex.createPokemon("Pikachu", "Electric", 125);
		Pokemon dugtrio = pokedex.createPokemon("Dugtrio", "Ground", 150);
		Pokemon charmanda = pokedex.createPokemon("Charmanda", "Fire", 145);
		
		
		System.out.println(pikachu.getHealth());
		pokedex.attackPokemon(pikachu);
		System.out.println(pikachu.getHealth());
		
		
		System.out.println(pokedex.pokemonInfo(pikachu));
		ArrayList<Object> p1 = pokedex.pokemonInfo(pikachu);
		for (Object pokemon : p1) {
			System.out.println(pokemon);
		}
		System.out.println(Pokemon.getCount());
		System.out.println(Pokemon.getEmAll());
		
		ArrayList<Pokemon> allPokes = Pokemon.getEmAll();
		
		for (Pokemon p2: allPokes ) {
			System.out.println(pokedex.pokemonInfo(p2));
		}
	}
	
}
