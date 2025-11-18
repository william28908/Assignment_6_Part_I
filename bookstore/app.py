from flask import Flask, render_template, request, redirect, url_for, make_response


# instantiate the app
app = Flask(__name__)

# Create a list called categories. The elements in the list should be lists that contain the following information in this order:
#   categoryId
#   categoryName
#   An example of a single category list is: [1, "Biographies"]
categories = [[1, "Hard Science Fiction"], [2, "Soft Science Fiction"], [3, "Space Opera"], [4, "Cyberpunk"]]

# Create a list called books. The elements in the list should be lists that contain the following information in this order:
#   bookId     (you can assign the bookId - preferably a number from 1-16)
#   categoryId (this should be one of the categories in the category dictionary)
#   title
#   author
#   isbn
#   price      (the value should be a float)
#   image      (this is the filename of the book image.  If all the images, have the same extension, you can omit the extension)
#   readNow    (This should be either 1 or 0.  For each category, some of the books (but not all) should have this set to 1.
#   An example of a single category list is: [1, 1, "Madonna", "Andrew Morton", "13-9780312287863", 39.99, "madonna.png", 1]
books = [
         [1, "Hard Science Fiction", "The Martian", "Andy Weir", "9780553418026", 19.00, "the_martian.jpg", 1], 
         [2, "Hard Science Fiction", "The Three-Body Problem", "Cixin Liu", "9780765382030", 18.99, "three_body_problem.jpg", 0],
         [3, "Hard Science Fiction", "Rendezvous with Rama", "Arthur C. Clarke", "9780553057140", 27.95, "rendezvous.jpg", 0],
         [4, "Hard Science Fiction", "Red Mars", "Kim Stanley Robinson", "9780593358825", 20.00, "red_mars.jpg", 1],
         [5, "Soft Science Fiction", "The Left Hand of Darkness", "Ursula K. Le Guin", "9780143111597", 19.00, "left_hand_of_darkness.jpg", 1],
         [6, "Soft Science Fiction", "The Handmaid's Tale", "Margaret Atwood", "9780385490818", 18.00, "handmaids_tale.jpg", 1],
         [7, "Soft Science Fiction", "Brave New World", "Aldous Huxley", "9780060850524", 18.99, "brave_new_world.jpg", 0],
         [8, "Soft Science Fiction", "Frankenstein", "Mary Shelley", "9780486282114", 14.95, "frankenstein.jpg", 0],
         [9, "Space Opera", "Hyperion", "Dan Simmons", "9780553283686", 18.99, "hyperion.jpg", 0],
         [10, "Space Opera", "Dune", "Frank Herbert", "9780441172719", 18.00, "dune.jpg", 1],
         [11, "Space Opera", "Ender's Game", "Orson Scott Card", "9780812550702", 18.99, "enders_game.jpg", 1],
         [12, "Space Opera", "Foundation", "Isaac Asimov", "9780553293357", 18.00, "foundation.jpg", 0],
         [13, "Cyberpunk", "Neuromancer", "William Gibson", "9780441569595", 20.00, "neuromancer.jpg", 0],
         [14, "Cyberpunk", "Snow Crash", "Neal Stephenson", "9780553380958", 5.99, "snow_crash.jpg", 1],
         [15, "Cyberpunk", "Synners", "Pat Cadigan", "9780575119543", 28.98, "synners.jpg", 0],
         [16, "Cyberpunk", "Hardwired", "Walter Jon Williams", "9781597800624", 17.09, "hardwired.jpg", 1],
        ]



# set up routes
@app.route('/')
def home():
    #Link to the index page.  Pass the categories as a parameter
    return render_template("index.html", categories=categories)

@app.route('/category')
def category():
    # Store the categoryId passed as a URL parameter into a variable
    selected_cat = request.args.get("categoryid")

    # Create a new list called selected_books containing a list of books that have the selected category
    selected_books = []
    for book in books:
          if book[1] == selected_cat:
                   selected_books.append(book)
                  

    # Link to the category page.  Pass the selectedCategory, categories and books as parameters
    return render_template("category.html", selectedCategory = selected_cat, categories = categories, books = selected_books)

@app.route('/search')
def search():
    #Link to the search results page.
    return render_template("search.html")

@app.errorhandler(Exception)
def handle_error(e):
    """
    Output any errors - good for debugging.
    """
    return render_template('error.html', error=e) # render the edit template


if __name__ == "__main__":
    app.run(debug = True)
