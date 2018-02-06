<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Language</title>
<link rel="stylesheet" type="text/css" href="css/style.css">
<script type="text/javascript" src="js/main.js"></script>
<a href="/languages">Dashboard</a>
</head>
<body>



			<p>${ language.name }</p>
			<p>${ language.creator }</p>
			<p>${ language.version }</p>
			
			
			
			<a href="/languages/edit/${id }">Edit</a>
			<a href="/languages/delete/${id }">Delete</a>
</body>
</html>