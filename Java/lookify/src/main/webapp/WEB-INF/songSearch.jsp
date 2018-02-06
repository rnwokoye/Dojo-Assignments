<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Lookify</title>
<link rel="stylesheet" type="text/css" href="css/style.css">
<script type="text/javascript" src="js/main.js"></script>
</head>
<body>

		<a href="/dashboard">Dashboard</a>		
		
		<table class="table">
		<tr>
			<th>Name</th>
			<th>Rating</th>
			<th>Actions</th>
		</tr>
	<c:forEach items="${ songs }" var="song" varStatus="loop">
		<tr>
			<td><a href="/songs/${song.id }">${ song.title }</a></td>
			<td>${ song.rating }</td>
			<td><a href="/songs/delete/${song.id }">Delete</a></td>
		</tr>
	</c:forEach>	
	</table><br><br> 	
</body>
</html>