<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
	<h1>Survey Form</h1>

	<form action="/process" method="post">
		Your Name: <input type="text" name="your_name"><br><br>
		Dojo Location: <select name="dojo_location">
			<option value="Washington_DC">Washington_DC</option>
			<option value="Baltimore">Baltimore</option>
			<option value="Miami">Miami</option>
		</select><br><br>
		Favorite Language: <select name="favorite_lang"><br>
			<option value="JavaScript">JavaScript</option>
			<option value="python">Python</option>
			<option value="C++">C++</option>
		</select><br><br>
		Comment (optional):<textarea name="comments"></textarea><br><br>
		<input type="submit" value="button">
	</form>	
		
</body>
</html>