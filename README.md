# littlelemon

paths:

	/api/menu/
		Methods:
			GET: Returns all  records in the restaurant_menu
			POST: adds a record to the restaurant_menu table 
			
	/api/menu/{menu-item}
		Methods:
			PUT/PATCH: update reord with the provided id
			DELETE: delete the record with the provided id

			
	/api/booking/tables/
		Methods:
			GET: Returns all  records in the restaurant_booking table 
			POST: adds a record to the restaurant_bookings table 
			PUT/PATCH: update reord with the provided id
			DELETE: delete the record with the provided id
			
	/auth/users/
		Methods:
			GET: returns all registered users
			POST: given the (username, password, email) registers new user 
			
	/auth/token/login/
		Methods:
			POST: generates auth token  for the user (given the username and password) 
			
			
			
