package com.richnwokoye.queryparameters.controllers;

import javax.servlet.http.HttpSession;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RequestMapping("/")
@Controller
public class MainController {
	@RequestMapping("/")
	public String index(Model model, @RequestParam(value="name", defaultValue="Human") String searchQuery) {	
		model.addAttribute("name", searchQuery);
		return "index";
	}
	
	@RequestMapping("/main")
	public String main() {	
		return "main";
	}
	
	@RequestMapping("/result")
	public String result() {	
		return "result";
	}
	
	@PostMapping("/process")
	public String process(
			@RequestParam(value="your_name") String name,
			@RequestParam(value ="dojo_location") String Dojo_location,
			@RequestParam(value= "favorite_lang") String Favorite_Language,
			@RequestParam(value="comments") String Comments,
			HttpSession session){
		session.setAttribute("Name", name);
		session.setAttribute("dojo_loc", Dojo_location);
		session.setAttribute("fav_lang", Favorite_Language);
		session.setAttribute("comments", Comments);
		
		return "redirect:/result";
		
	}
}
