package com.richnwokoye.code.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;
import org.w3c.dom.Attr;

@Controller
public class Code {
	@RequestMapping("/")
	public String index() {
		
		return "index";
	}
	
	@RequestMapping("/code")
	public String code() {
		
		return "code";
	}
	
	@PostMapping("/process")
	public String index(@RequestParam(value="codeinput") String codeinput, RedirectAttributes red) {
		String ans = "bushido"; 
		if(codeinput.equals(ans)) {
			return "redirect:/code";
		}else {
			
			red.addFlashAttribute("error", "You must Try harder");
			System.out.println(red);
		}
		return "redirect:/";
		
	}
	

}
