<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h1>New License</h1>
		<form:form action="/license/new" method="post" modelAttribute="license">
			<p><form:label path="person">Person:	</form:label>
			<form:select path="person"> 
				<c:forEach items="${persons}" var="person" varStatus="loop">
					<form:option value="${person.id}">${ person.firstName }</form:option>
				</c:forEach>
			</form:select>
			</p>

			<p><form:label path="state">State:
				<form:errors path="state"></form:errors>			
				<form:input path="state"></form:input>
			</form:label>
			</p>

			<p><form:label path="expiration_date">Expiration Date:
				<form:errors path="expiration_date"></form:errors>			
				<form:input type= "date" path="expiration_date"></form:input>
			</form:label>
			</p>

			<input type="submit" value="Create License" />
		</form:form>
	
	
</body>
</html>