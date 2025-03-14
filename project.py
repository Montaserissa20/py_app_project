from PyQt5 import QtWidgets, uic
import sys
import sqlite3
from datetime import datetime,timedelta
from PyQt5.QtGui import QRegularExpressionValidator
from PyQt5.QtCore import QRegularExpression
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('project.ui', self)
        self.current_user_id = None  # Initialize current_user_id
        self.setupUi()

    def setupUi(self):
        # Set the initial page to loginPage
        self.stackedWidget = self.findChild(QtWidgets.QStackedWidget, 'stackedWidget')
        self.stackedWidget.setCurrentIndex(0)
       
        
        # Find widgets by their object names in the login page 
        #self.findchild is used to know if the widget is there or not
        self.emailLineEdit = self.findChild(QtWidgets.QLineEdit, 'emailLineEdit')
        self.passwordLineEdit = self.findChild(QtWidgets.QLineEdit, 'passwordLineEdit')
        self.createEmailLineEdit = self.findChild(QtWidgets.QLineEdit, 'createEmailLineEdit')
        self.createPasswordLineEdit = self.findChild(QtWidgets.QLineEdit, 'createPasswordLineEdit')
        self.confirmPasswordLineEdit = self.findChild(QtWidgets.QLineEdit, 'confirmPasswordLineEdit')
        self.addressLineEdit = self.findChild(QtWidgets.QLineEdit, 'addressLineEdit')
        self.createAccountButton = self.findChild(QtWidgets.QPushButton, 'createAccountButton')
        self.loginButton = self.findChild(QtWidgets.QPushButton, 'loginButton')
        self.gotoCreateAccountButton = self.findChild(QtWidgets.QPushButton, 'gotoCreateAccountButton')
        self.backToLoginButton = self.findChild(QtWidgets.QPushButton, 'backToLoginButton')
        self.forgotPasswordButton = self.findChild(QtWidgets.QPushButton, 'forgotPasswordButton')  # Add this line
        # Connect buttons to their respective functions
        # every button connected to the function that let it works 
        self.loginButton.clicked.connect(self.login)
        self.gotoCreateAccountButton.clicked.connect(self.show_create_account_page)
        self.createAccountButton.clicked.connect(self.create_account)
        self.backToLoginButton.clicked.connect(self.show_login_page)
        self.forgotPasswordButton.clicked.connect(self.forgot_password)  # Add this line
        # Widgets for search page
        #same as up
        self.searchButton = self.findChild(QtWidgets.QPushButton, 'searchButton')
        self.gamesTableWidget = self.findChild(QtWidgets.QTableWidget, 'gamesTableWidget')
        self.notFoundButton = self.findChild(QtWidgets.QPushButton, 'notFoundButton')
        self.addToCartButton = self.findChild(QtWidgets.QPushButton, 'addToCartButton')
        self.gotoCartPageFromSearchButton = self.findChild(QtWidgets.QPushButton, 'gotoCartPageFromSearchButton')
        self.gotoCheckoutPageFromSearchButton = self.findChild(QtWidgets.QPushButton, 'gotoCheckoutPageFromSearchButton')
        self.searchScrollUpButton = self.findChild(QtWidgets.QPushButton, 'searchScrollUpButton')
        self.searchScrollDownButton = self.findChild(QtWidgets.QPushButton, 'searchScrollDownButton')
        self.logoutButton = self.findChild(QtWidgets.QPushButton, 'goFromSearchPagetologinpage')
        self.genreComboBox = self.findChild(QtWidgets.QComboBox, 'genreComboBox')  # Find the combo box
        # Connect buttons to their respective functions
        #same as up
        self.searchButton.clicked.connect(self.search_games)
        self.notFoundButton.clicked.connect(self.show_wishlist_page)
        self.addToCartButton.clicked.connect(self.add_to_cart)
        self.gotoCartPageFromSearchButton.clicked.connect(self.show_cart_page)
        self.gotoCheckoutPageFromSearchButton.clicked.connect(self.show_checkout_page)
        self.searchScrollUpButton.clicked.connect(self.search_scroll_up)
        self.searchScrollDownButton.clicked.connect(self.search_scroll_down)
        self.logoutButton.clicked.connect(self.logout)
        # Widgets for wishlist page
        # same as up
        self.gameTitleLineEdit = self.findChild(QtWidgets.QLineEdit, 'gameTitleLineEdit')
        self.gameGenreLineEdit = self.findChild(QtWidgets.QLineEdit, 'gameGenreLineEdit')
        self.submitWishlistButton = self.findChild(QtWidgets.QPushButton, 'submitWishlistButton')
        # Connect button to its function
        # same as up
        self.submitWishlistButton.clicked.connect(self.add_to_wishlist)
        # Widgets for wishlist view page
        #same as up
        self.viewWishlistButton = self.findChild(QtWidgets.QPushButton, 'viewWishlistButton')
        self.wishlistTableWidget = self.findChild(QtWidgets.QTableWidget, 'wishlistTableWidget')
        self.removeFromWishlistButton = self.findChild(QtWidgets.QPushButton, 'removeFromWishlistButton')
        self.wishlistScrollUpButton = self.findChild(QtWidgets.QPushButton, 'wishlistScrollUpButton')
        self.wishlistScrollDownButton = self.findChild(QtWidgets.QPushButton, 'wishlistScrollDownButton')
        # Connect buttons to their respective functions
        # same as up
        self.viewWishlistButton.clicked.connect(self.show_wishlist_view)
        self.removeFromWishlistButton.clicked.connect(self.remove_from_wishlist)
        self.wishlistScrollUpButton.clicked.connect(self.wishlist_scroll_up)
        self.wishlistScrollDownButton.clicked.connect(self.wishlist_scroll_down)
        # Widgets for cart page
        # same as up
        self.cartTableWidget = self.findChild(QtWidgets.QTableWidget, 'cartTableWidget')
        self.proceedButton = self.findChild(QtWidgets.QPushButton, 'proceedButton')
        self.removeFromCartButton = self.findChild(QtWidgets.QPushButton, 'removeFromCartButton')
        self.cartScrollUpButton = self.findChild(QtWidgets.QPushButton, 'cartScrollUpButton')
        self.cartScrollDownButton = self.findChild(QtWidgets.QPushButton, 'cartScrollDownButton')
        self.gotoWishlistPageButton = self.findChild(QtWidgets.QPushButton, 'gotoWishlistPageButton')
        self.gotoSearchPageButton = self.findChild(QtWidgets.QPushButton, 'gotoSearchPageButton')
        self.gotoWishlistViewPageButton = self.findChild(QtWidgets.QPushButton, 'gotoWishlistViewPageButton')
        self.goFromCarttosearch = self.findChild(QtWidgets.QPushButton, 'goFromCarttosearch')
        # Connect buttons to their respective functions
        # same as up
        self.proceedButton.clicked.connect(self.show_checkout_page)
        self.removeFromCartButton.clicked.connect(self.remove_from_cart)
        self.cartScrollUpButton.clicked.connect(self.cart_scroll_up)
        self.cartScrollDownButton.clicked.connect(self.cart_scroll_down)
        self.goFromCarttosearch.clicked.connect(self.show_search_page)
        # Widgets for checkout page
        # same as up
        self.checkoutTitleLabel = self.findChild(QtWidgets.QLabel, 'checkoutTitleLabel')
        self.rentRadioButton = self.findChild(QtWidgets.QRadioButton, 'rentRadioButton')
        self.buyRadioButton = self.findChild(QtWidgets.QRadioButton, 'buyRadioButton')
        self.cardNumberLineEdit = self.findChild(QtWidgets.QLineEdit, 'cardNumberLineEdit')
        self.expiryDateLineEdit = self.findChild(QtWidgets.QLineEdit, 'expiryDateLineEdit')
        self.cvvLineEdit = self.findChild(QtWidgets.QLineEdit, 'cvvLineEdit')
        self.proceedCheckoutButton = self.findChild(QtWidgets.QPushButton, 'proceedCheckoutButton')
        self.goFromCheckouttocart = self.findChild(QtWidgets.QPushButton, 'goFromCheckouttocart')
        # Connect button to its function
        # same as up
        self.proceedCheckoutButton.clicked.connect(self.proceed_with_checkout)
        self.goFromCheckouttocart.clicked.connect(self.show_cart_page)
        # down there is some kind of rules to do the format for the information of the card
        # for the card number i used QRegularExpressinValidator to make it only have 16 digits no more than that 
        card_number_validator = QRegularExpressionValidator(QRegularExpression(r'\d{16}'), self)
        self.cardNumberLineEdit.setValidator(card_number_validator)
        # for the cvv the same thing the only difference is it only takes 3 digits no more than that 
        cvv_validator = QRegularExpressionValidator(QRegularExpression(r'\d{3}'), self)
        self.cvvLineEdit.setValidator(cvv_validator)
        # the one down used for the date we have 0[1-9] for months from 01to09 and 1[0-2] for months from 10to12 and the last one for the year takes any 2 digits
        expiry_date_validator = QRegularExpressionValidator(QRegularExpression(r'(0[1-9]|1[0-2])/\d{2}'), self)
        self.expiryDateLineEdit.setValidator(expiry_date_validator)
        # Navigation buttons for wishlist and wishlist view
        self.goFromWishlisttosearch = self.findChild(QtWidgets.QPushButton, 'goFromWishlisttosearch')
        self.goBackFromWishlistviewtossearchpage = self.findChild(QtWidgets.QPushButton, 'goBackFromWishlistviewtossearchpage')
        # connecting buttons to their functions 
        self.goFromWishlisttosearch.clicked.connect(self.show_search_page)
        self.goBackFromWishlistviewtossearchpage.clicked.connect(self.show_search_page)
        # Admin page widgets
        self.adminTableWidget = self.findChild(QtWidgets.QTableWidget, 'adminTableWidget')
        self.updateGameButton = self.findChild(QtWidgets.QPushButton, 'updateGameButton')
        self.removeGameButton = self.findChild(QtWidgets.QPushButton, 'removeGameButton')
        self.backButton = self.findChild(QtWidgets.QPushButton, 'backButton')
        self.addButton = self.findChild(QtWidgets.QPushButton, 'addButton')  # Add this line
        self.gotoUserAdminPageButton = self.findChild(QtWidgets.QPushButton, 'gotoUserAdminPageButton')
        self.adminLineEdit = self.findChild(QtWidgets.QLineEdit, 'adminline')
        self.adminSearchButton = self.findChild(QtWidgets.QPushButton, 'adminsearch')
        self.adminFilterComboBox = self.findChild(QtWidgets.QComboBox, 'adminComboBox')
        # connecting buttons to their functions 
        self.updateGameButton.clicked.connect(self.update_game)
        self.removeGameButton.clicked.connect(self.remove_game)
        self.backButton.clicked.connect(self.show_login_page)
        self.addButton.clicked.connect(self.add_game)  # Add this line
        self.adminSearchButton.clicked.connect(self.admin_search_games)
        # Navigation buttons for admin page
        self.gotoUserAdminPageButton.clicked.connect(self.show_user_admin_page)
        # Widgets for user admin page
        self.userTableWidget = self.findChild(QtWidgets.QTableWidget, 'usertable')
        self.removeUserButton = self.findChild(QtWidgets.QPushButton, 'removeuser')
        self.backToAdminPageButton = self.findChild(QtWidgets.QPushButton, 'backtoadminpage')
       # Connect buttons to their respective functions
        self.removeUserButton.clicked.connect(self.remove_user)
        self.backToAdminPageButton.clicked.connect(self.show_admin_page)
        # Connect the button to the function
        # Widgets for wishlist admin page
        self.adminWishlistTable = self.findChild(QtWidgets.QTableWidget, 'adminwishlistTable')
        self.addFromWishlistToGameTableButton = self.findChild(QtWidgets.QPushButton, 'addfromwishlisttogameTable')
        self.backToAdminPageFromWishlistButton = self.findChild(QtWidgets.QPushButton, 'backToAdminPageFromWishlistButton')
        # Navigation button for admin page to wishlist admin page
        self.gotoWishlistAdminPageButton = self.findChild(QtWidgets.QPushButton, 'gotowishlistadminpage')
        self.gotoWishlistAdminPageButton.clicked.connect(self.show_wishlist_admin_page)
        # Connect buttons to their respective functions
        self.addFromWishlistToGameTableButton.clicked.connect(self.prompt_add_game)
        self.backToAdminPageFromWishlistButton.clicked.connect(self.show_admin_page)
        # Initialize tables
        # the code for the tables is down below 
        self.init_games_table()
        self.init_wishlist_table()
        self.init_cart_table()
        self.init_admin_table()
        # Call this function in setupUi
        self.populate_genre_combobox()
        # Populate the admin filter combo box
        self.populate_admin_filter_combobox()

    def show_login_page(self):
      print("Navigating to login page")
      self.emailLineEdit.clear()  # Clear the email input
      self.passwordLineEdit.clear()  # Clear the password input
      self.stackedWidget.setCurrentIndex(0)  # Set the index to login page


    def logout(self):
      self.current_user_id = None  # Clear current user id
      self.current_user_email = None  # Clear current user email
      self.emailLineEdit.clear()  # Clear email input
      self.passwordLineEdit.clear()  # Clear password input
      self.load_games()  # Reload games to reflect any updates
      self.show_login_page()  # Navigate to login page
      self.clear_checkout_fields()  # Clear checkout fields


    def show_create_account_page(self):
        print("Navigating to create account page")
        self.stackedWidget.setCurrentIndex(1)

    def login(self):
      email = self.emailLineEdit.text()
      password = self.passwordLineEdit.text()
      conn = sqlite3.connect('game_shop.db') # this line for connection
      cursor = conn.cursor() # we use cursor so we can use sql commands 

      try:
        # the line down check the user table for the information 
        cursor.execute('SELECT id, email FROM users WHERE email = ? AND password = ?', (email, password))
        user = cursor.fetchone()
        
        if user:
            QtWidgets.QMessageBox.information(self, "Login", "Login successful!")
            self.current_user_id = user[0]  # Store the current user's id
            self.current_user_email = email  # Store the current user's email
            
            # Check if the user is an admin
            if email == 'admin':
                self.show_admin_page()
            else:
                self.show_search_page()
        else:
            # the one down check the admin table for the information 
            cursor.execute('SELECT id, email FROM admins WHERE email = ? AND password = ?', (email, password))
            admin = cursor.fetchone()
            if admin:
                QtWidgets.QMessageBox.information(self, "Admin Login", "Admin login successful!")
                self.current_user_id = admin[0]  # Store the current admin's id
                self.current_user_email = email  # Store the current admin's email
                self.show_admin_page()
            else:
                QtWidgets.QMessageBox.warning(self, "Login", "Invalid email or password!")
      finally:
        conn.close()  # Ensure the connection is closed after the query is executed


    def create_account(self):
        email = self.createEmailLineEdit.text()
        password = self.createPasswordLineEdit.text()
        confirm_password = self.confirmPasswordLineEdit.text()
        address = self.addressLineEdit.text()
        # check if the password match or not 
        if password != confirm_password:
            QtWidgets.QMessageBox.warning(self, "Error", "Passwords do not match!")
            return
        conn = sqlite3.connect('game_shop.db')
        cursor = conn.cursor()
        # check if the email is admin it stores in the admin table if it's not stores in the user's table
        if email == 'admin':
            cursor.execute('INSERT INTO admins (email, password) VALUES (?, ?)', (email, password))
        else:
            cursor.execute('INSERT INTO users (email, password, address) VALUES (?, ?, ?)', (email, password, address))
        conn.commit()
        conn.close()
        QtWidgets.QMessageBox.information(self, "Account Created", "Account successfully created!")
        self.show_login_page()
    def forgot_password(self):
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("Forgot Password")

        layout = QtWidgets.QVBoxLayout()

        emailLabel = QtWidgets.QLabel("Email:")
        emailLineEdit = QtWidgets.QLineEdit()
        layout.addWidget(emailLabel)
        layout.addWidget(emailLineEdit)

        newPasswordLabel = QtWidgets.QLabel("New Password:")
        newPasswordLineEdit = QtWidgets.QLineEdit()
        newPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        layout.addWidget(newPasswordLabel)
        layout.addWidget(newPasswordLineEdit)

        confirmPasswordLabel = QtWidgets.QLabel("Confirm Password:")
        confirmPasswordLineEdit = QtWidgets.QLineEdit()
        confirmPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        layout.addWidget(confirmPasswordLabel)
        layout.addWidget(confirmPasswordLineEdit)

        submitButton = QtWidgets.QPushButton("Submit")
        # using lambda to change the password 
        submitButton.clicked.connect(lambda: self.update_password(emailLineEdit.text(), newPasswordLineEdit.text(), confirmPasswordLineEdit.text(), dialog))
        layout.addWidget(submitButton)
        # using the method below to make the user can't touch anything till he finish doing the new password
        dialog.setLayout(layout)
        dialog.exec_()
    def update_password(self, email, new_password, confirm_password, dialog):
        if new_password != confirm_password:
            QtWidgets.QMessageBox.warning(self, "Error", "Passwords do not match!")
            return

        conn = sqlite3.connect('game_shop.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE users SET password = ? WHERE email = ?', (new_password, email))
        # cursor.rowcount return the number for the rows have been affected by the change 
        if cursor.rowcount == 0:  # If no rows were updated, check the admins table
            cursor.execute('UPDATE admins SET password = ? WHERE email = ?', (new_password, email))
        if cursor.rowcount == 0:  # If still no rows were updated, user not found
            QtWidgets.QMessageBox.warning(self, "Error", "User not found!")
        else:
            conn.commit()
            QtWidgets.QMessageBox.information(self, "Password Updated", "Password successfully updated!")
            dialog.accept()
        conn.close()

    def search_games(self):
      search_text = self.searchLineEdit.text()
      selected_genre = self.genreComboBox.currentText()  # Get the selected genre

      conn = sqlite3.connect('game_shop.db')
      cursor = conn.cursor()

    # Construct the query with genre filter
      if selected_genre and selected_genre != "All":
        query = 'SELECT id, title, genre, price, rent_price FROM games WHERE title LIKE ? AND genre = ?'
        cursor.execute(query, ('%' + search_text + '%', selected_genre))
      else:
        query = 'SELECT id, title, genre, price, rent_price FROM games WHERE title LIKE ?'
        cursor.execute(query, ('%' + search_text + '%',))

      games = cursor.fetchall()
      self.gamesTableWidget.setRowCount(len(games))
      self.gamesTableWidget.setColumnCount(5)  # Ensure the column count includes rent_price
      self.gamesTableWidget.setHorizontalHeaderLabels(["ID", "Title", "Genre", "Price", "Rent Price"])  # Update header labels
      for row_num, game in enumerate(games):
        for col_num, data in enumerate(game):
            self.gamesTableWidget.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(data)))

      conn.close()
    # the one down do the same as up but just for the adminpage  
    def admin_search_games(self):
      search_text = self.adminLineEdit.text()
      selected_genre = self.adminComboBox.currentText()  # Get the selected genre

      conn = sqlite3.connect('game_shop.db')
      cursor = conn.cursor()

    # Construct the query with genre filter
      if selected_genre and selected_genre != "All":
        query = 'SELECT id, title, genre, price, rent_price FROM games WHERE title LIKE ? AND genre = ?'
        cursor.execute(query, ('%' + search_text + '%', selected_genre))
      else:
        query = 'SELECT id, title, genre, price, rent_price FROM games WHERE title LIKE ?'
        cursor.execute(query, ('%' + search_text + '%',))

      games = cursor.fetchall()
      self.adminTableWidget.setRowCount(len(games))
      self.adminTableWidget.setColumnCount(5)  # Ensure the column count includes rent_price
      self.adminTableWidget.setHorizontalHeaderLabels(["ID", "Title", "Genre", "Price", "Rent Price"])  # Update header labels
      for row_num, game in enumerate(games):
        for col_num, data in enumerate(game):
            self.adminTableWidget.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(data)))

      conn.close()


    def populate_genre_combobox(self):
      conn = sqlite3.connect('game_shop.db')
      cursor = conn.cursor()
      # takes only the genre row from the table
      cursor.execute('SELECT DISTINCT genre FROM games')
      genres = cursor.fetchall()
      self.genreComboBox.addItem("All")  # Option to show all games
      for genre in genres:
        self.genreComboBox.addItem(genre[0])
      conn.close()
    # the one below like the one up 
    def populate_admin_filter_combobox(self):
      conn = sqlite3.connect('game_shop.db')
      cursor = conn.cursor()
      cursor.execute('SELECT DISTINCT genre FROM games')
      genres = cursor.fetchall()
      self.adminFilterComboBox.addItem("All")  # Option to show all games
      for genre in genres:
        self.adminFilterComboBox.addItem(genre[0])
      conn.close()
      
    def show_search_page(self):
      print("Navigating to search page")
      self.load_games()  # Reload games to reflect any updates
      self.stackedWidget.setCurrentIndex(2)
      
    def show_wishlist_page(self):
        print("Navigating to wishlist page")
        self.stackedWidget.setCurrentIndex(5)

    def show_wishlist_view(self):
        print("Navigating to wishlist view page")
        self.load_wishlist()
        self.stackedWidget.setCurrentIndex(6)

    def show_cart_page(self):
        print("Navigating to cart page")
        self.stackedWidget.setCurrentIndex(3)  # Update the index to match your cart page index
        self.load_cart()  # Load cart items when showing the cart page

    def show_checkout_page(self):
        print("Navigating to checkout page")
        self.stackedWidget.setCurrentIndex(4)

    def show_admin_page(self):
        print("Navigating to admin page")
        self.load_admin_table()
        self.stackedWidget.setCurrentIndex(7)
    def show_user_admin_page(self):
      print("Navigating to user admin page")
      self.load_users_table()
      self.stackedWidget.setCurrentIndex(8)
    def show_wishlist_admin_page(self):
      self.load_admin_wishlist_table()  # Load the wishlist table
      self.stackedWidget.setCurrentIndex(9)  # Navigate to wishlistadminpage



    def add_to_wishlist(self):
        title = self.gameTitleLineEdit.text()
        genre = self.gameGenreLineEdit.text()
        conn = sqlite3.connect('game_shop.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO wishlist (title, genre, user_id) VALUES (?, ?, ?)', (title, genre, self.current_user_id))
        # the line below ensure that the changes made in the database
        conn.commit()
        conn.close()
        self.gameTitleLineEdit.clear()
        self.gameGenreLineEdit.clear()
        QtWidgets.QMessageBox.information(self, "Wishlist", "Game added to wishlist!")

    def add_to_cart(self):
        selected_items = self.gamesTableWidget.selectedItems()
        if not selected_items:
            QtWidgets.QMessageBox.warning(self, "Add to Cart", "Please select a game to add to cart.")
            return

        # Fetch the row of the selected item and get the row index of the selected item
        selected_row = selected_items[0].row()

        # Get the data from the row
        game_id = self.gamesTableWidget.item(selected_row, 0).text()
        title = self.gamesTableWidget.item(selected_row, 1).text()
        genre = self.gamesTableWidget.item(selected_row, 2).text()
        price = float(self.gamesTableWidget.item(selected_row, 3).text())
        rent_price = float(self.gamesTableWidget.item(selected_row, 4).text())

        conn = sqlite3.connect('game_shop.db')
        cursor = conn.cursor()

        # Check if the game already exists in the user's cart
        cursor.execute('SELECT quantity FROM cart WHERE user_id = ? AND game_id = ?', (self.current_user_id, game_id))
        result = cursor.fetchone()

        if result:
            # Update the quantity if the game already exists
            new_quantity = result[0] + 1
            cursor.execute('UPDATE cart SET quantity = ? WHERE user_id = ? AND game_id = ?', (new_quantity, self.current_user_id, game_id))
        else:
            # Insert a new row if the game does not exist in the cart
            cursor.execute('INSERT INTO cart (user_id, game_id, title, genre, price, rent_price, quantity) VALUES (?, ?, ?, ?, ?, ?, ?)', 
                           (self.current_user_id, game_id, title, genre, price, rent_price, 1))

        conn.commit()
        conn.close()
        QtWidgets.QMessageBox.information(self, "Cart", "Game added to cart!")

    def remove_from_wishlist(self):
        selected_items = self.wishlistTableWidget.selectedItems()
        if not selected_items:
            QtWidgets.QMessageBox.warning(self, "Remove Game", "No game selected for removal.")
            return

        # Fetch the row of the selected item
        selected_row = selected_items[0].row()

        # Get the data from the row by knowing the id
        wishlist_id = self.wishlistTableWidget.item(selected_row, 0).text()

        conn = sqlite3.connect('game_shop.db')
        cursor = conn.cursor()
        # remove the id that match the one in the table
        cursor.execute('DELETE FROM wishlist WHERE id = ?', (wishlist_id,))
        conn.commit()
        conn.close()
        self.load_wishlist()

    def remove_from_cart(self):
        selected_items = self.cartTableWidget.selectedItems()
        if not selected_items:
            QtWidgets.QMessageBox.warning(self, "Remove Game", "No game selected for removal.")
            return

        # Fetch the row of the selected item
        selected_row = selected_items[0].row()

        # Get the data from the row by knowing the id 
        cart_id = self.cartTableWidget.item(selected_row, 0).text()

        conn = sqlite3.connect('game_shop.db')
        cursor = conn.cursor()
        # reomve the id that match the id in the table
        cursor.execute('DELETE FROM cart WHERE id = ?', (cart_id,))
        conn.commit()
        conn.close()
        self.load_cart()
    def remove_user(self):
      selected_items = self.userTableWidget.selectedItems()
      if not selected_items:
        QtWidgets.QMessageBox.warning(self, "Remove User", "No user selected for removal.")
        return
      # gets the index of the selected item
      selected_row = selected_items[0].row()
      # takes the user id form the first coulum in the selected row
      user_id = self.userTableWidget.item(selected_row, 0).text()

      conn = sqlite3.connect('game_shop.db')
      cursor = conn.cursor()

      try:
        cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
        conn.commit()
        QtWidgets.QMessageBox.information(self, "Remove User", "User and related data removed successfully!")
        self.load_users_table()  # Refresh the users table
      except sqlite3.Error as e:
        QtWidgets.QMessageBox.warning(self, "Remove User", f"Error removing user: {e}")
      finally:
        conn.close()


    def clear_checkout_fields(self):
      self.cardNumberLineEdit.clear()
      self.expiryDateLineEdit.clear()
      self.cvvLineEdit.clear()


    def proceed_to_checkout(self):
        QtWidgets.QMessageBox.information(self, "Checkout", "Proceed to checkout!")

    def search_scroll_up(self):
        self.gamesTableWidget.verticalScrollBar().setValue(self.gamesTableWidget.verticalScrollBar().value() - 1)

    def search_scroll_down(self):
        self.gamesTableWidget.verticalScrollBar().setValue(self.gamesTableWidget.verticalScrollBar().value() + 1)

    def wishlist_scroll_up(self):
        self.wishlistTableWidget.verticalScrollBar().setValue(self.wishlistTableWidget.verticalScrollBar().value() - 1)

    def wishlist_scroll_down(self):
        self.wishlistTableWidget.verticalScrollBar().setValue(self.wishlistTableWidget.verticalScrollBar().value() + 1)

    def cart_scroll_up(self):
        self.cartTableWidget.verticalScrollBar().setValue(self.cartTableWidget.verticalScrollBar().value() - 1)

    def cart_scroll_down(self):
        self.cartTableWidget.verticalScrollBar().setValue(self.cartTableWidget.verticalScrollBar().value() + 1)

    def proceed_with_checkout(self):
    # Check which radio button is selected
      if self.rentRadioButton.isChecked():
        transaction_type = "Rent"
      elif self.buyRadioButton.isChecked():
        transaction_type = "Buy"
      else:
        QtWidgets.QMessageBox.warning(self, "Checkout", "Please select rent or buy.")
        return

    # Get payment information
      card_number = self.cardNumberLineEdit.text()
      expiry_date = self.expiryDateLineEdit.text()
      cvv = self.cvvLineEdit.text()

      if not card_number or not expiry_date or not cvv:
        QtWidgets.QMessageBox.warning(self, "Checkout", "Please fill all payment information.")
        return

      try:
        conn = sqlite3.connect('game_shop.db')
        cursor = conn.cursor()
        
        # Update the user's payment information in the database
        cursor.execute('''
            UPDATE users
            SET card_number = ?, expiry_date = ?, cvv = ?
            WHERE id = ?
        ''', (card_number, expiry_date, cvv, self.current_user_id))
        conn.commit()
        # ask for the weeks in order to rent
        if transaction_type == "Rent":
            weeks, ok = QtWidgets.QInputDialog.getInt(self, "Rent Duration", "Enter the number of weeks to rent:")
            if not ok:
                return
            rental_start_date = datetime.now().date()
            rental_end_date = rental_start_date + timedelta(weeks=weeks)

            # Fetch cart items and calculate the total rent cost
            cursor.execute('SELECT game_id, title, genre, rent_price, quantity FROM cart WHERE user_id = ?', (self.current_user_id,))
            cart_items = cursor.fetchall()
            # put the information in the rentals table
            for item in cart_items:
                game_id, title, genre, rent_price, quantity = item
                total_rent_price = rent_price * weeks * quantity
                cursor.execute('''
                    INSERT INTO rentals (user_id, game_id, title, genre, rent_price, quantity, total_rent_price, rental_start_date, rental_end_date)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (self.current_user_id, game_id, title, genre, rent_price, quantity, total_rent_price, rental_start_date, rental_end_date))

        elif transaction_type == "Buy":
            # Add the transaction to the transactions table
            cursor.execute('SELECT game_id, title, genre, price, quantity FROM cart WHERE user_id = ?', (self.current_user_id,))
            cart_items = cursor.fetchall()

            for item in cart_items:
                game_id, title, genre, price, quantity = item
                total_price = price * quantity
                cursor.execute('''
                    INSERT INTO transactions (user_id, game_id, title, genre, price, quantity, total_price, transaction_date)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (self.current_user_id, game_id, title, genre, price, quantity, total_price, datetime.now()))

        # Generate a receipt for the user
        self.generate_receipt(transaction_type, cart_items, weeks if transaction_type == "Rent" else None)

        # Clear the user's cart after checkout
        cursor.execute('DELETE FROM cart WHERE user_id = ?', (self.current_user_id,))
        conn.commit()

        # Show a confirmation message
        QtWidgets.QMessageBox.information(self, "Checkout", f"Transaction completed. Type: {transaction_type}")

      except sqlite3.OperationalError as e:
        print(f"Database error: {e}")
      finally:
        if conn:
            conn.close()

    def generate_receipt(self, transaction_type, cart_items, weeks=None):
      receipt = f"Receipt\nTransaction Type: {transaction_type}\n\n"
      total_cost = 0
      # see if the transaction is rent or not 
      if transaction_type == "Rent":
        rental_start_date = datetime.now().date()
        rental_end_date = rental_start_date + timedelta(weeks=weeks)
         # goes for all the items in the cart and calucate the rent price and do a receipt
        for item in cart_items:
            title, genre, rent_price, quantity = item[1], item[2], item[3], item[4]
            item_total = rent_price * weeks * quantity
            total_cost += item_total
            receipt += (f"Title: {title}\nGenre: {genre}\nRent Price: {rent_price}\nWeeks: {weeks}\n"
                        f"Quantity: {quantity}\nTotal: {item_total}\n\n")

        receipt += (f"Rental Start Date: {rental_start_date}\nRental End Date: {rental_end_date}\n"
                    f"Grand Total: {total_cost}")
      # goes for buy
      elif transaction_type == "Buy":
        for item in cart_items:
            title, genre, price, quantity = item[1], item[2], item[3], item[4]
            item_total = price * quantity
            total_cost += item_total
            receipt += (f"Title: {title}\nGenre: {genre}\nPrice: {price}\nQuantity: {quantity}\n"
                        f"Total: {item_total}\n\n")

        receipt += f"Grand Total: {total_cost}"

      QtWidgets.QMessageBox.information(self, "Receipt", receipt)



    def clear_cart(self):
        conn = sqlite3.connect('game_shop.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM cart WHERE user_id = ?', (self.current_user_id,))
        conn.commit()
        conn.close()

    def init_games_table(self):
      self.gamesTableWidget.setColumnCount(5)  # Updated to include rent_price
      self.gamesTableWidget.setHorizontalHeaderLabels(["Game ID", "Title", "Genre", "Price", "Rent Price"])
      self.load_games()


    def init_wishlist_table(self):
        self.wishlistTableWidget.setColumnCount(4)
        self.wishlistTableWidget.setHorizontalHeaderLabels(["Wishlist ID", "Title", "Genre", "User ID"])
        self.load_wishlist()

    def init_cart_table(self):
        self.cartTableWidget.setColumnCount(6)
        self.cartTableWidget.setHorizontalHeaderLabels(["Cart ID", "Title", "Genre", "Price", "Quantity", "Rent Price"])
        self.load_cart()

    def init_admin_table(self):
        self.adminTableWidget.setColumnCount(5)
        self.adminTableWidget.setHorizontalHeaderLabels(["Game ID", "Title", "Genre", "Price", "Rent Price"])
        self.load_admin_table()

    def load_games(self):
        conn = sqlite3.connect('game_shop.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, title, genre, price, rent_price FROM games')
        games = cursor.fetchall()
        self.gamesTableWidget.setRowCount(len(games))
        for row_num, game in enumerate(games):
            for col_num, data in enumerate(game):
                self.gamesTableWidget.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()
    def load_users_table(self):
      conn = sqlite3.connect('game_shop.db')
      cursor = conn.cursor()
      cursor.execute('SELECT id, email, address FROM users')
      users = cursor.fetchall()
      self.userTableWidget.setRowCount(len(users))
      self.userTableWidget.setColumnCount(3)
      self.userTableWidget.setHorizontalHeaderLabels(["User ID", "Email", "Address"])
      for row_num, user in enumerate(users):
        for col_num, data in enumerate(user):
            self.userTableWidget.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(data)))
      conn.close()


    def load_wishlist(self):
        conn = sqlite3.connect('game_shop.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, title, genre, user_id, game_id FROM wishlist WHERE user_id = ?', (self.current_user_id,))
        wishlist = cursor.fetchall()
        self.wishlistTableWidget.setRowCount(len(wishlist))
        for row_num, item in enumerate(wishlist):
            for col_num, data in enumerate(item):
                self.wishlistTableWidget.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()

    def load_cart(self):
        conn = sqlite3.connect('game_shop.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, title, genre, price, quantity, rent_price FROM cart WHERE user_id = ?', (self.current_user_id,))
        cart_items = cursor.fetchall()
        self.cartTableWidget.setRowCount(len(cart_items))
        for row_num, item in enumerate(cart_items):
            for col_num, data in enumerate(item):
                self.cartTableWidget.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()

    def load_admin_table(self):
        conn = sqlite3.connect('game_shop.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, title, genre, price, rent_price FROM games')
        games = cursor.fetchall()
        self.adminTableWidget.setRowCount(len(games))
        for row_num, game in enumerate(games):
            for col_num, data in enumerate(game):
                self.adminTableWidget.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()
    def load_admin_wishlist_table(self):
      conn = sqlite3.connect('game_shop.db')
      cursor = conn.cursor()
      cursor.execute('SELECT id, title, genre, user_id FROM wishlist')
      wishlist = cursor.fetchall()
      self.adminWishlistTable.setRowCount(len(wishlist))
      self.adminWishlistTable.setColumnCount(4)
      self.adminWishlistTable.setHorizontalHeaderLabels(["ID", "Title", "Genre", "User ID"])
      for row_num, item in enumerate(wishlist):
        for col_num, data in enumerate(item):
            self.adminWishlistTable.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(data)))
      conn.close()
    def prompt_add_game(self):
      # creates a popup dialog window
      dialog = QtWidgets.QDialog()
      dialog.setWindowTitle("Add Game from Wishlist")

      layout = QtWidgets.QVBoxLayout()

      titleLabel = QtWidgets.QLabel("Game Title:")
      titleLineEdit = QtWidgets.QLineEdit()
      layout.addWidget(titleLabel)
      layout.addWidget(titleLineEdit)

      genreLabel = QtWidgets.QLabel("Genre:")
      genreLineEdit = QtWidgets.QLineEdit()
      layout.addWidget(genreLabel)
      layout.addWidget(genreLineEdit)

      priceLabel = QtWidgets.QLabel("Price:")
      priceLineEdit = QtWidgets.QLineEdit()
      layout.addWidget(priceLabel)
      layout.addWidget(priceLineEdit)

      rentPriceLabel = QtWidgets.QLabel("Rent Price:")
      rentPriceLineEdit = QtWidgets.QLineEdit()
      layout.addWidget(rentPriceLabel)
      layout.addWidget(rentPriceLineEdit)

      submitButton = QtWidgets.QPushButton("Submit")
      submitButton.clicked.connect(lambda: self.add_game_from_prompt(titleLineEdit.text(), genreLineEdit.text(), priceLineEdit.text(), rentPriceLineEdit.text(), dialog))
      layout.addWidget(submitButton)

      dialog.setLayout(layout)
      dialog.exec_()
    def add_game_from_prompt(self, title, genre, price, rent_price, dialog):
      conn = sqlite3.connect('game_shop.db')
      cursor = conn.cursor()
      cursor.execute('INSERT INTO games (title, genre, price, rent_price) VALUES (?, ?, ?, ?)', (title, genre, price, rent_price))
      conn.commit()
      conn.close()
      self.load_admin_wishlist_table()
      QtWidgets.QMessageBox.information(self, "Add Game", "Game added to games table!")
      dialog.accept()

    def update_game(self):
      selected_items = self.adminTableWidget.selectedItems()
      if not selected_items:
        QtWidgets.QMessageBox.warning(self, "Update Game", "No game selected for update.")
        return
      # gets the index of the selected item
      selected_row = selected_items[0].row()
      #gets the game id from the first coulum in the selected row
      game_id = self.adminTableWidget.item(selected_row, 0).text()

    # Prompt for new details
      new_title, ok1 = QtWidgets.QInputDialog.getText(self, "Update Game", "Enter new title:", QtWidgets.QLineEdit.Normal, self.adminTableWidget.item(selected_row, 1).text())
      new_genre, ok2 = QtWidgets.QInputDialog.getText(self, "Update Game", "Enter new genre:", QtWidgets.QLineEdit.Normal, self.adminTableWidget.item(selected_row, 2).text())
      new_price, ok3 = QtWidgets.QInputDialog.getDouble(self, "Update Game", "Enter new price:", float(self.adminTableWidget.item(selected_row, 3).text()), 0, 1000, 2)
      new_rent_price, ok4 = QtWidgets.QInputDialog.getDouble(self, "Update Game", "Enter new rent price:", float(self.adminTableWidget.item(selected_row, 4).text()), 0, 1000, 2)
      # check if the oks were clicked or not
      if ok1 and ok2 and ok3 and ok4:
        conn = sqlite3.connect('game_shop.db')
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE games
            SET title = ?, genre = ?, price = ?, rent_price = ?
            WHERE id = ?
        ''', (new_title, new_genre, new_price, new_rent_price, game_id))
        conn.commit()
        conn.close()

        # Update the admin table
        self.load_admin_table()
        QtWidgets.QMessageBox.information(self, "Update Game", "Game updated successfully!")
      # if not a message will show and say it got canceled 
      else:
        QtWidgets.QMessageBox.warning(self, "Update Game", "Update cancelled.")
    def add_game(self):
    # Prompt for new game details
      title, ok1 = QtWidgets.QInputDialog.getText(self, "Add Game", "Enter game title:")
      genre, ok2 = QtWidgets.QInputDialog.getText(self, "Add Game", "Enter game genre:")
      price, ok3 = QtWidgets.QInputDialog.getDouble(self, "Add Game", "Enter game price:", 0, 0, 1000, 2)
      rent_price, ok4 = QtWidgets.QInputDialog.getDouble(self, "Add Game", "Enter game rent price:", 0, 0, 1000, 2)
    
      if ok1 and ok2 and ok3 and ok4:
        conn = sqlite3.connect('game_shop.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO games (title, genre, price, rent_price)
            VALUES (?, ?, ?, ?)
        ''', (title, genre, price, rent_price))
        conn.commit()
        conn.close()

        # Update the admin table
        self.load_admin_table()
        QtWidgets.QMessageBox.information(self, "Add Game", "Game added successfully!")
      else:
        QtWidgets.QMessageBox.warning(self, "Add Game", "Addition cancelled.")



    def remove_game(self):
        selected_items = self.adminTableWidget.selectedItems()
        if not selected_items:
            QtWidgets.QMessageBox.warning(self, "Remove Game", "No game selected for removal.")
            return
        # gets the index of the selected item and ensure that only one is selected
        selected_row = selected_items[0].row()
        #gets the game id from the first coulum in the selected row
        game_id = self.adminTableWidget.item(selected_row, 0).text()

        conn = sqlite3.connect('game_shop.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM games WHERE id = ?', (game_id,))
        conn.commit()
        conn.close()
        self.load_admin_table()



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())
