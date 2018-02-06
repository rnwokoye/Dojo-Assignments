package com.richnwokoye.languages.controllers;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import javax.validation.Valid;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import com.richnwokoye.languages.models.Language;
import com.richnwokoye.languages.services.LanguageService;


@Controller
@RequestMapping("/languages")
public class Languages {
	private final LanguageService languageService;
	
	public Languages(LanguageService languageService) {
		this.languageService = languageService; 
	}
		
	@RequestMapping("")
	public String languages(Model model,@ModelAttribute("language") Language language) {
		List<Language> languages = languageService.allLanguages();		
		model.addAttribute("languages",languages);
		return "languages";
	}
	
	@RequestMapping("/{id}")
	public String showLanguageById(Model model, @PathVariable("id") Long id) {
		Language language = languageService.showLanguageById(id);
		model.addAttribute("language", language);
		return "showLanguage";	
	}
	
	@RequestMapping("/new")
	public String newLanguage(@ModelAttribute("language") Language language) {
		
		return "newLanguage";
	}
	
	@PostMapping("/new")
	public String createLanguage(@Valid @ModelAttribute("language") Language language, BindingResult result) {
		if (result.hasErrors()) {
			return "newLanguage";
		}else {
			languageService.addLanguage(language);
			System.out.println(language);
			return "redirect:/languages";
		}
	}
	@RequestMapping("/edit/{id}")
	public String editLanguage(@PathVariable("id") Long id, Model model) {
		Language language = languageService.showLanguageById(id);
		if(language != null) {
			model.addAttribute("language", language);
			return "editLanguage";
		}else {
			return "redirect:/languages";
		}
		
	}
	@PostMapping("/edit/{id}")
	public String updateLanguage(@PathVariable("id") Long id, @Valid @ModelAttribute("language") Language language, BindingResult result) {
		if(result.hasErrors()) {
			return "editLanguage";
		}else {
			languageService.updateLanguage(id, language);
			return "redirect:/languages";
		}
	}
	@RequestMapping(value="/delete/{id}")
	public String destroyLanguage(@PathVariable("id") Long id) {
		languageService.destroyLanguage(id);
		return "redirect:/languages";
	}
	
}
