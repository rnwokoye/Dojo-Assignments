package com.project.relationships.controllers;

import java.util.ArrayList;

import javax.validation.Valid;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import com.project.relationships.models.License;
import com.project.relationships.models.Person;
import com.project.relationships.services.LicenseService;
import com.project.relationships.services.PersonService;

@Controller
@RequestMapping("/license")
public class LicenseController {
	private PersonService personService;
	private LicenseService licenseService;
	
	public LicenseController(LicenseService licenseService, PersonService personService) {
		this.licenseService = licenseService;
		this.personService = personService;
	}
	@RequestMapping("")
	public String licenses(@ModelAttribute("license") License license, Model model) {
		ArrayList<Person> persons = personService.allPersons();
		model.addAttribute("persons", persons);
		return "newLicense";
	}
	
	@PostMapping("/new")
	public String newLicense(@Valid @ModelAttribute("license") License license, BindingResult result) {
		if(result.hasErrors()) {
			return "newLicense";
		}else {
			licenseService.create(license);
			return "redirect:/persons";
		}
	}
}
