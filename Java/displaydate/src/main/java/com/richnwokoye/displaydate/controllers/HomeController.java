package com.richnwokoye.displaydate.controllers;

import java.util.Date;
import java.text.SimpleDateFormat;

import org.apache.catalina.servlet4preview.http.HttpServletRequest;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
@RequestMapping("/")
public class HomeController {
	@RequestMapping("")
	public String index() {
		
		return "index";
	}
	
	
	@RequestMapping("/date")
	public String date(Model model) {
		Date date = new Date();
		SimpleDateFormat dateFrmt = new SimpleDateFormat("EEEE, 'the' dd 'of' MMMM, yyyy");
		model.addAttribute("date", dateFrmt.format(date));
		return "date";
	}
	
	@RequestMapping("/time")
	public String time(Model model) {
		Date time = new Date();
		SimpleDateFormat dateFrmt = new SimpleDateFormat("h:mm:a"); 
		model.addAttribute("time", dateFrmt.format(time));	
		return "time";
	}
	
//	@RequestMapping("/")
//	public String redirect(HttpServletRequest req) {
//		
//		String url = req.getRequestURI().toString();
//		return "redirect:/index"; 
//	}

}
