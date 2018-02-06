<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Language</title>
<link rel="stylesheet" type="text/css" href="css/style.css">
<script type="text/javascript" src="js/main.js"></script>
</head>
<body>

	<table class="table">
		<tr>
			<th>Name</th>
			<th>Creator</th>
			<th>Version</th>
			<th>Action</th>
		
		</tr>
	<c:forEach items="${ languages }" var="lang" varStatus="loop">
		<tr>
			<td><a href="/languages/${lang.id}">${ lang.name }</a></td>
			<td>${ lang.creator }</td>
			<td>${ lang.version }</td>
			<td><a href="/languages/edit/${lang.id}">Edit</a> <a href="/languages/delete/${lang.id}">Delete</a></td> 
		</tr>
	</c:forEach>	
	</table><br><br>
	
	<form:form method="POST" action="/languages/new" modelAttribute="language">
		<form:label path="name">name
		<form:errors path="name"/>
		<form:input path="name"/></form:label><br><br>
		
		<form:label path="creator">creator
		<form:errors path="creator"/>
		<form:input path="creator"/></form:label><br><br>
		
		<form:label path="version">version
		<form:errors path="version"/>
		<form:input path="version"/></form:label><br><br>		
		
		<input type="submit" value="Submit"/>
	</form:form>
	
	
	
	
	<!-- <a href="/languages/new">add language</a> -->
	
		
</body>
</html>