package com.project.relationships.services;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.springframework.stereotype.Service;

import com.project.relationships.models.Person;
import com.project.relationships.repositories.PersonRepository;

@Service
public class PersonService {
	public ArrayList<Person> persons = new ArrayList<Person>(Arrays.asList());
	
	private PersonRepository personRepository;
	public PersonService(PersonRepository personRepository) {
		this.personRepository = personRepository;
	}
	
	public ArrayList<Person> allPersons(){
		return (ArrayList<Person>)personRepository.findAll();
	}
	public void addPerson(Person person) {
		personRepository.save(person);
	}

	public Person findPersonsById(long id) {
		return personRepository.findOne(id);
	}
	
	

}
