package com.richnwokoye.books.controllers;

//import java.util.ArrayList;
//import java.util.Arrays;
import java.util.List;

import javax.validation.Valid;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import com.richnwokoye.books.models.Book;
import com.richnwokoye.books.services.BookService;

@Controller
public class Books {
	private final BookService bookService;
	
	public Books(BookService bookService) {
		this.bookService = bookService;
	}
	
	@RequestMapping("/books")
	public String books(Model model) {
		List<Book> books = bookService.allBooks();
		model.addAttribute("books", books);
		return "books";
	}
	
	@RequestMapping("/bookslist")
	public String booksList(Model model) {
		List<Book> books = bookService.allBooks();		
		model.addAttribute("books", books);
		return "booksList";	
	}
	
	@RequestMapping("/books/{id}")
	public String findBookById(Model model, @PathVariable("id") Long id) {
		Book book = bookService.findBookById(id);
		model.addAttribute("Book", book);
			return "showBook";
		}
//		model.addAttribute("book", bookService.findBookById(id));
//		return "book";	
	
	@RequestMapping("/books/new")
	public String newBook(@ModelAttribute("book") Book book) {
		
		return "newBook";
	}
	
	@PostMapping("/books/new")
	public String createBook(@Valid @ModelAttribute("book") Book book, BindingResult result) {
		if (result.hasErrors()) {
			return "newBook";
		
		}else {
			bookService.addBook(book);
			System.out.println(book);
			return "redirect:/books";
		}
	}
	@RequestMapping("/books/edit/{id}")
	public String editBook(@PathVariable("id") long id, Model model) {
		Book book = bookService.findBookById(id);
		if(book != null) {
			model.addAttribute("book" , book);
			return "editBook";
		}else {
			return "redirect:/books";
		}
	}
	@PostMapping("/books/edit/{id}")
	public String updateBook(@Valid @ModelAttribute("book") Book book, BindingResult result, @PathVariable("id") long id) {
		if (result.hasErrors()) {
			return "editBook";
		}else {
			bookService.updateBook(book);
			return "redirect:/books";
		}
	}
	@RequestMapping(value="/books/delete/{id}")
	public String destroyBook(@PathVariable("id") long id) {
		bookService.destroyBook(id);
		return "redirect:/books";
	}
	
	
//	@RequestMapping("/books/{Desc}")
//		public String seachBooks(@PathVariable("Desc") String Desc) {
////			bookService.SearchByDesc(Desc);
//			System.out.println(bookService.SearchByDesc(Desc));
//			return "searchList";
//		}
	}
	

