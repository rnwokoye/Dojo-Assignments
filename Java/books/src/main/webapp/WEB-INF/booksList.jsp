<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<%-- <%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%> --%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
	<ul>
	<c:forEach items="${ books }" var="book">
		<li>
			<c:out value="${ book.title }"/>
			<c:out value="${ book.description }"/>
			<c:out value="${ book.language }"/>
			<c:out value="${ book.numberOfPages }"/>
		</li>
	</c:forEach>	
	</ul>
	
	<h3>break</h3>
	<h3>Show Books by Index View</h3>
			
			
			
			<p>${ Book.title }</p>
			<p>${ Book.description }</p>
			<p>${ Book.language }</p>
			<p>${ Book.numberOfPages }</p>
	
	
	
	
</body>
</html>