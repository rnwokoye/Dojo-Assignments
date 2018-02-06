package com.richnwokoye.lookify.services;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.springframework.stereotype.Service;

import com.richnwokoye.lookify.models.Song;
import com.richnwokoye.lookify.repositories.SongRepository;

@Service
public class SongService {
	private List<Song> songs = new ArrayList<Song>(Arrays.asList());
	
	private SongRepository songRepository;
	public SongService(SongRepository songRepository) {
		this.songRepository = songRepository;
	}
	public List<Song> allSongs(){
		return songRepository.findAll();
	}
	public void addSong(Song song) {
		songRepository.save(song);
		
	}
	public void destroySong(Long id) {
		songRepository.delete(id);
		
	}
	public Song showSongById(Long id) {
		return songRepository.findOne(id);
	}
	public ArrayList<Song> findByArtistContaining(String artist){
		return (ArrayList<Song>) songRepository.findByArtistContaining(artist);
		
	}

	public ArrayList<Song> orderByRatingDesc() {
		ArrayList<Song> songs = (ArrayList<Song>) songRepository.OrderByRatingDesc();
		for(int i= 0; i < songs.size(); i++) {
			if(i > 10) {
				songs.remove(i);
			}
		}
		return songs;
	}

}
