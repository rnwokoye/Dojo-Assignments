package com.richnwokoye.books.services;

import java.util.ArrayList;

import java.util.Arrays;
import java.util.List;

import org.springframework.stereotype.Service;

import com.richnwokoye.books.models.Book;
import com.richnwokoye.books.repositories.BookRepository;

@Service
public class BookService {
	List<Book> books = new ArrayList<Book>(Arrays.asList());
	
	private BookRepository bookRepository;
	public BookService(BookRepository bookRepository) {
		this.bookRepository = bookRepository;
	}
	
	
	
	public List<Book> allBooks(){
		return bookRepository.findAll();
	}
	public List<Book> SearchByDesc(String search){
		return bookRepository.findByDescriptionContaining(search);
	}
	
	public Book findBookById(Long id) {
		return bookRepository.findOne(id);
		}
	
	public void addBook(Book book) {
		bookRepository.save(book);
	}
	public void updateBook(Book book) {
//		if(id < books.size()) {
//			books.set(id, book);
		bookRepository.save(book);
		}
	
	public void destroyBook(long id) {
//		if(id < books.size()) {
//			books.remove(id);
		bookRepository.delete(id);
		}
	}
	



