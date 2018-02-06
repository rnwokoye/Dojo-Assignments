package com.richnwokoye.controllerspractice.controllers;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
//
//@RestController // REstController is a combo of the controller annotation and the response body annotation
//@RequestMapping("/hello")  //RqMp adding to the whole controller
//public class HomeController {
//	// RqMping map web requests to one specific controller, either class level or method level
//	// we now change this to an empty mapping.
//	@RequestMapping("") 
//	public String hello() {
//		return "Hello  Again World Controller";
//	}
//	
//	@RequestMapping("/world")
//	public String world() {
//		return "Hello World too";
//	}

//}
//notes: @Controller annotation.when we want to have a view (HTML or JSP) in our response
//@ResponseBody annotation: we want Spring boot to return data and not a view
//@RestController annotation: We use this annotation when we want our controller to respond with data
//Using @ controller as bellow: 

@Controller
public class HomeController{
	@RequestMapping("/")
	public String index(Model model) {
		model.addAttribute("dojoname", "Richard");
		return "index";
	}
	
	@RequestMapping("/notes")
	public String notes() {
		return "notes";
	}
	
	@RequestMapping("/new")
	public String helpers(Model model) {
		model.addAttribute("firstName", "Uba3");
		return "new"; 
	
	}
	
}
