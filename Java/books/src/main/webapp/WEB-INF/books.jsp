<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Books</title>
<link rel="stylesheet" type="text/css" href="css/style.css">
<script type="text/javascript" src="js/main.js"></script>
</head>
<body>
	<div class=wrapper>
			<table class="table">
				<tr>
					<th>Book Title</th>
					<th>Book Description</th>
					<th>Book Language</th>
					<th>Book Pages</th>
					<th>Book Action</th>
				</tr>
			<c:forEach items="${ books }" var="book" varStatus="loop">
				<tr>
					<td>${ book.title }</td>
					<td>${ book.description }</td>
					<td>${ book.language }</td>
					<td>${ book.numberOfPages }</td>
					<td><a href="/books/edit/${book.id}">edit</a> <a href="/books/delete/${book.id}">delete</a></td>	
				</tr>
			</c:forEach>	
			</table>
	
			<button><a href="/books/new">add book</a></button>
	</div>
</body>
</html>