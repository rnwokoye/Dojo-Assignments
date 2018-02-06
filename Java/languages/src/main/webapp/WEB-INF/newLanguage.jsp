<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
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
</body>
</html>