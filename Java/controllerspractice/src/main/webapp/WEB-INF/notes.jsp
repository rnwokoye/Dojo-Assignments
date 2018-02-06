<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix = "c" uri = "http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
	
    <c:out value="${2+2}"/>
    
	<h3>My Notes Here</h3>
   
  	<p>
  		We pass data to our view using a model object. 
  		The model object implements the map interface and exposes the key-value pairs in our view. 
  		To pass data to our view can be as simple as injecting a Model object to our controller method:
  	</p>

</body>
</html>