package com.richnwokoye.counter.controllers;

import javax.servlet.http.HttpSession;

import org.apache.catalina.servlet4preview.http.HttpServletRequest;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class Counter {
	@RequestMapping("/")
	public String index() {
		
		return "index";
	}
	
	@RequestMapping("/counter")
	public String counter(HttpSession session) {
		if(session.getAttribute("count") == null) {
			session.setAttribute("count",  0);
		}else {
			session.setAttribute("count", (Integer) session.getAttribute("count") +1);
	}
		return "counter"; 
	}
	@RequestMapping("/session")
	public String session() {
		
		return "redirect:/";
	}
	
	@RequestMapping("/reset")
	public String reset(HttpSession session) {
		session.setAttribute("count", 0);
		return "redirect:/";
	}	
	
}
