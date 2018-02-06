package com.richnwokoye.lookify.repositories;

import java.util.ArrayList;
import java.util.List;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.richnwokoye.lookify.models.Song;

@Repository
public interface SongRepository extends CrudRepository<Song, Long>{
	List<Song> findAll();
	public ArrayList<Song> findByArtistContaining(String artist);
//	Long countByTitleContaining(String search);
//	Long deleteByTitleStartingWith(String search);
	public ArrayList<Song> OrderByRatingDesc();

	
	
}
	


