package com.richnwokoye.lookify.controllers;

import java.util.ArrayList;
import java.util.List;

import javax.validation.Valid;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

import com.richnwokoye.lookify.models.Song;
import com.richnwokoye.lookify.services.SongService;

@Controller
public class Lookify {
	private final SongService songService;
	
	public Lookify(SongService songService) {
		this.songService = songService;
	}
	
	@RequestMapping("/")
	public String startLooking() {
		return "startLooking";
	}
	
	@RequestMapping("/dashboard")
	public String songs(Model model, @ModelAttribute("song") Song song) {
		List<Song> songs = songService.allSongs();
		model.addAttribute("songs", songs);
		return "dashBoard"; 
	}
	@RequestMapping("/songs/new")
	public String newSong(@ModelAttribute("song") Song song) {
		return "newSong";
	}
	@PostMapping("/songs/new")
	public String createSong(@Valid @ModelAttribute("song") Song song, BindingResult result) {
		if(result.hasErrors()) {
			return "newSong";
		}else {
			songService.addSong(song);
			return "redirect:/dashboard";
		}
	}
	@RequestMapping("/songs/delete/{id}")
	public String destroySong(@PathVariable("id") Long id) {
		songService.destroySong(id);
		return "redirect:/dashboard";
	}
	@RequestMapping("/songs/{id}")
	public String showSongById(Model model, @PathVariable("id") Long id) {
		Song song = songService.showSongById(id);
		model.addAttribute("song",song);
		return "showSong";
	}
	
	@RequestMapping("/search/topTen")
	public String topTen(Model model) {
		List<Song> songs = songService.orderByRatingDesc();
		model.addAttribute("songs", songs);
		return "topTen";
	}
	@RequestMapping("/search")
	public String findByArtistContaining(Model model, @RequestParam(value="artist") String artist) {
		model.addAttribute("songs", songService.findByArtistContaining(artist));
		return "songSearch";
		
	}
}




	
