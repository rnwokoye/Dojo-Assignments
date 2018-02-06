package com.funJava;

import java.util.HashMap;

public class TrackList {
	public static void main(String[] args) {
		HashMap<String, String> trackList = new HashMap<>(); 
		trackList.put("Man in the Mirror", "I'm standing with the man in the mirro");
		trackList.put("Bad", "You know I'm baad");
		trackList.put("Billie Jean", "I'm Billie Jean and I'm mad as hell");
		trackList.put("Black or White", "It's black, it's white");
		
		
		String track1 = trackList.get("Bad"); 
		System.out.println(track1);
		
		for (String key : trackList.keySet()) {
			System.out.println(key + " : " + trackList.get(key));	
		
	}
	
	}		
	
}