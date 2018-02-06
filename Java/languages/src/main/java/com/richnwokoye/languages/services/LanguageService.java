package com.richnwokoye.languages.services;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.springframework.stereotype.Service;

//import com.richnwokoye.books.models.Book;
import com.richnwokoye.languages.models.Language;
import com.richnwokoye.languages.repositories.LanguageRepository;

@Service
public class LanguageService {
		
	private List<Language> languages = new ArrayList<Language>(Arrays.asList(
			new Language("Java", "James Gosling", 1.8),
			new Language("Phyton", "Guido van Rossum", 3.6),
			new Language("Javascript", "Brendon Eich", 1.95)
			));
	
	
	private LanguageRepository languageRepository;
	public LanguageService(LanguageRepository languageRepository) {
		this.languageRepository = languageRepository;
	}
	
	public List<Language> allLanguages(){
		return languageRepository.findAll();

	}

	public Language showLanguageById(Long id) {
		return languageRepository.findOne(id);
		}

	public void addLanguage(Language language) {
		languageRepository.save(language);	
	}

	public void updateLanguage(Long id, Language language) {
		languageRepository.save(language);
	}

	public void destroyLanguage(Long id) {
		languageRepository.delete(id);
	}
	

}
