<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
<script type="text/javascript" src="js/main.js"></script>
</head>
<body>
	
	<h3>Show Books by Index View</h3>
		
			<p>Title: ${ Book.title }</p>
			<p>Desc: ${ Book.description }</p>
			<p>Lang: ${ Book.language }</p>
			<p>Pages: ${ Book.numberOfPages }</p>
	
</body>
</html>