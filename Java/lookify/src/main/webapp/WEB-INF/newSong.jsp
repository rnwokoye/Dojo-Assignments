<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
<a href="/dashboard">Dashboard</a>
</head>
<body>
	<form:form method="POST" action="/songs/new" modelAttribute="song">
		<form:label path="title">Title
		<form:errors path="title"/>
		<form:input path="title"/></form:label><br><br>
		
		<form:label path="artist">Artist
		<form:errors path="artist"/>
		<form:input path="artist"/></form:label><br><br>
		
		<form:label path="rating">Rating
		<form:errors path="rating"/>
		<form:select path= "rating">
		<form:option value="1"/>
		<form:option value="2"/>
		<form:option value="3"/>
		<form:option value="4"/>
		<form:option value="5"/>
		<form:option value="6"/>
		<form:option value="7"/>
		<form:option value="8"/>
		<form:option value="9"/>
		<form:option value="10"/>
		</form:select>
		</form:label><br><br>		
		
		<input type="submit" value="Submit"/>
	</form:form>
</body>
</html>