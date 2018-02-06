package com.project.relationships.controllers;

import javax.validation.Valid;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import com.project.relationships.models.Person;
import com.project.relationships.services.PersonService;

@Controller
@RequestMapping("/persons")
public class PersonController {
	private PersonService personService;
	
	public PersonController(PersonService personService) {
		this.personService = personService;
	}
	@RequestMapping("")
	public String persons(@ModelAttribute("person") Person person) {
		return "newPerson";
	}
	@PostMapping("/new")
	public String create(@Valid @ModelAttribute("person") Person person, BindingResult result) {
		if(result.hasErrors()) {
			return "newPerson";
		}else {
			personService.addPerson(person);
			return "redirect:/license";
		}
	}
	@RequestMapping("/{index}")
	public String showPersonsbyId(Model model, @PathVariable("index") long index) {
		Person person = personService.findPersonsById(index);
		model.addAttribute("person", person);
		return "/showPerson";
	}
	
}
